# Prediction of hepatocellular carcinoma following hepatitis C virus sustained virologic response using a random survival forest model

This repository contains the data for predicting the occurrence of hepatocellular carcinoma (HCC) following a sustained virologic response (SVR) in hepatitis C virus (HCV) patients using a Random Survival Forest (RSF) model.

## Overview

The aim of this project is to develop a predictive model for HCC in HCV patients who have achieved SVR. The RSF model takes into account several clinical variables to provide accurate predictions.　The model building script is contained in `model_building.py`.

## Dataset

The dataset used for model building contains the following columns:

- **Plt**: Platelet count (x10^4/µL)
- **gamma-GTP**: Gamma-glutamyl transpeptidase (IU/L)
- **male0**: Sex (male: 0, female: 1)
- **age**: Age (years)
- **ALT**: Alanine aminotransferase (IU/L)
- **Event**: HCC event (first occurrence) (with HCC: 1, without HCC: 0)
- **time**: Observation time (days)

### Example Dataset

| Plt | gamma-GTP | male0 | age | ALT | Event | time |
|-----|-----------|-------|-----|-----|-------|------|
| 15  | 20        | 1     | 55  | 20  | 0     | 365  |
| 20  | 40        | 0     | 60  | 35  | 1     | 730  |
| 18  | 35        | 0     | 50  | 18  | 0     | 540  |

## License

This project is licensed under the Creative Commons Attribution-NonCommercial (CC-By-NC) license. For more details, refer to the LICENSE file.