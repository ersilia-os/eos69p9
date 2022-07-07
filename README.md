# Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network

## Model Identifiers
- Slug: ssl-gcn-tox21
- Ersilia ID: eos69p9
- Tags: 

## Model Description
Compound toxicity prediction using graph convolutional neural network (GCN) and semi-supervised learning (SSL). Mean Teacher as the SSL algorithm is used to improve the prediction performance of GCN on 12 toxicity prediction tasks from the Tox21 dataset.
- Input: SMILES
- Output: ROC-AUC score	Model performance score
- Model Type: Classification
- Mode of training: Pretrained
- Training data: 58,358	(https://github.com/chen709847237/SSL-GCN)
- Experimentally validated: No

## Source Code
Chen, J., Si, YW., Un, CW. et al. Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network. J Cheminform 13, 93 (2021). DOI: https://doi.org/10.1186/s13321-021-00570-8
- Code: https://github.com/chen709847237/SSL-GCN
- Checkpoints: https://github.com/chen709847237/SSL-GCN

## License
The GPL-v3 covers all parts of the repository. The model uses the external library "SSL-GCN" and is located at `/model`

## History


