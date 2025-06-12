# Toxicity prediction across the Tox21 panel with semi-supervised learning

Toxicity prediction across the Tox21 panel from MoleculeNet, comprising 12 toxicity pathways. The model uses the Mean Teacher Semi-Supervised Learning (MT-SSL) approach to overcome the low number of data points experimentally annotated for toxicity tasks. For the MT-SSL, Tox21 (831 compounds and 12 different endpoints) was used as labeled data and a selection of 50K compounds from other MoleculeNet datasets was used as unlabeled data.

This model was incorporated on 2022-06-16.

## Information
### Identifiers
- **Ersilia Identifier:** `eos69p9`
- **Slug:** `ssl-gcn-tox21`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Tox21`, `Toxicity`, `MoleculeNet`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `12`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of toxicity across 12 tasks defined in Tox21

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| nr_ar | float | high | Probability of activation of the androgen receptor which indicates androgenic activity |
| nr_ar_lbd | float | high | Probability of binding to the androgen receptor ligand_binding domain indicating androgenic activity |
| nr_ahr | float | high | Probability of activation of the aryl hydrocarbon receptor involved in xenobiotic metabolism |
| nr_aromatase | float | high | Probability of inhibition of aromatase which is a key enzyme in estrogen biosynthesis |
| nr_er | float | high | Probability of activation of the estrogen receptor indicating estrogenic potential |
| nr_er_lbd | float | high | Probability of binding to the estrogen receptor ligand_binding domain indicating estrogenic activity |
| nr_ppar_gamma | float | high | Probability of activation of PPAR_gamma involved in fat metabolism and insulin sensitivity |
| sr_are | float | high | Probability of activation of antioxidant response element (ARE) linked to oxidative stress |
| sr_atad5 | float | high | Probability of DNA damage response via ATAD5 which is a marker for genomic instability |
| sr_hse | float | high | Probability of activation of the heat shock element pathway indicating cellular stress. |

_10 of 12 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos69p9](https://hub.docker.com/r/ersiliaos/eos69p9)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos69p9.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos69p9.zip)

### Resource Consumption
- **Model Size (Mb):** `23`
- **Environment Size (Mb):** `6146`


### References
- **Source Code**: [https://github.com/chen709847237/SSL-GCN](https://github.com/chen709847237/SSL-GCN)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00570-8](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00570-8)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos69p9
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos69p9
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
