import os
import torch
import joblib
import numpy as np
import pandas as pd
import dgl.backend as F
from dgl.data.utils import Subset
from argparse import ArgumentParser
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score
import shutil
import sys
from utils import init_featurizer,  load_dataset, get_self_configure, mkdir_p, collate_molgraphs, load_model, predict, data_unpack, load_ecfp_dataset

def predict_prob(args, exp_config, test_set):
    exp_config.update({
        'model': args['model'],
        'n_tasks': args['n_tasks'],
        'atom_featurizer_type': args['atom_featurizer_type'],
        'bond_featurizer_type': args['bond_featurizer_type']})
    if args['atom_featurizer_type'] != 'pre_train':
        exp_config['in_node_feats'] = args['node_featurizer'].feat_size()
    if args['edge_featurizer'] is not None and args['bond_featurizer_type'] != 'pre_train':
        exp_config['in_edge_feats'] = args['edge_featurizer'].feat_size()

    test_loader = DataLoader(dataset=test_set, batch_size=exp_config['batch_size'], collate_fn=collate_molgraphs, num_workers=args['num_workers'])
    model = load_model(exp_config).to(args['device'])
    model.load_state_dict(torch.load(args['model_data_path']+'/model.pth', map_location=torch.device('cpu'))['model_state_dict'])

    val_prob_list = []
    #val_target_list = []
    model.eval()
    with torch.no_grad():
        for batch_id, batch_data in enumerate(test_loader):
            smiles, bg, labels, masks = batch_data
            labels = labels.to(args['device'])
            logits = predict(args, model, bg)
            proba = torch.sigmoid(logits)
            val_prob_list.extend(proba.detach().cpu().data)
            #val_target_list.extend(labels.detach().cpu().data)
    #auc_score= roc_auc_score(val_target_list, val_prob_list)
    return val_prob_list
    

def txt_to_df(txt_file_path, task):
    df = pd.DataFrame()
    col3 = pd.read_csv(txt_file_path, header=None)
    col2 = pd.Series(np.arange(len(col3)))
    col1 = pd.Series(np.zeros(len(col3)))
    df[task] = col1.values
    df['mol_id'] = col2.values
    df['SMILES'] = col3.values
    return df

def tensor_to_list(prob_tensor):
    prob_list=[]
    for t in prob_tensor:
        prob_list.append(t.item())
    return prob_list


#output_data_folder = 'ssl_output_result'

def ssl_model_predict(data_file):
    #data_folder = 'predict_data/'
    root_model_folder = 'models/'
    model_files = os.listdir(root_model_folder)
    
    df_results = pd.read_csv(data_file, names=['SMILES'])
    for model_data_folder in model_files:
        task = model_data_folder
        print("task :   ", task)

        pretrain_folder_path = root_model_folder + model_data_folder
        #local_train_folder_path = output_data_folder + model_data_folder

        args = {'csv_path': data_file,
                    'cache_path': 'cache/' + task,
                    'task_names': task,
                    'smiles_column': 'SMILES',
                    'model': 'GCN',
                    'atom_featurizer_type': 'canonical',
                    'split': 'scaffold_smiles',
                    'split_ratio': '0.8,0.1,0.1',
                    'num_workers': 0,
                    'print_every': 3,
                    'metric': 'roc_auc_score',

                    'result_path': None,
                    'model_data_path': pretrain_folder_path,

                    'atom_featurizer_type': 'canonical',
                    'bond_featurizer_type': 'canonical'
                  }
        args = init_featurizer(args)
        if torch.cuda.is_available():
            args['device'] = torch.device(args['cuda_define'])
        else:
            args['device'] = torch.device('cpu')

        if args['task_names'] is not None:
            args['task_names'] = args['task_names'].split(',')
           
                
        df = txt_to_df(args['csv_path'],task)
            
        # This part removes the rows with NaN labels

        #df_label = df[args['task_names']].values
        #labels = F.zerocopy_from_numpy(np.nan_to_num(df_label, nan=-1).astype(np.float32))
        #label_idx = np.argwhere(np.array(labels).squeeze(1) != -1).squeeze(1)

        #label_df = df.iloc[label_idx]
            
        # **********************************************************************************
            
            
        lab_dataset = load_dataset(args, df)

        args['n_tasks'] = lab_dataset.n_tasks

        exp_config = get_self_configure(args['model_data_path'] + '/configure.json') 
        prob_tensor = predict_prob(args, exp_config, lab_dataset)
        prob_list = tensor_to_list(prob_tensor)
        result  = pd.Series(prob_list, name = task)
        df_results[task] = result
    shutil.rmtree('cache', ignore_errors=True)
    return df_results


# MAIN 

if __name__ == '__main__':
    smiles_file = str(sys.argv[1])
    print("Predicting Chemical toxicity using SSL-GCN Model")
    
    df_results = ssl_model_predict(smiles_file)
    df_results.to_csv('results.csv', index=False)
