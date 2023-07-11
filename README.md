# Toxicity prediction across the Tox21 panel with semi-supervised learning

Toxicity prediction across the Tox21 panel from MoleculeNet, comprising 12 toxicity pathways. The model uses the Mean Teacher Semi-Supervised Learning (MT-SSL) approach to overcome the low number of data points experimentally annotated for toxicity tasks. For the MT-SSL, Tox21 (831 compounds and 12 different endpoints) was used as labeled data and a selection of 50K compounds from other MoleculeNet datasets was used as unlabeled data.

## Identifiers

* EOS model ID: `eos69p9`
* Slug: `ssl-gcn-tox21`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Probability of toxicity across 12 tasks defined in Tox21

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00570-8)
* [Source Code](https://github.com/chen709847237/SSL-GCN)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos69p9)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00570-8) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!