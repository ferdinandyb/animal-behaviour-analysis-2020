# animal-behaviour-analysis-2020
Source code and data for Ferdinandy et al. 2020, "Challenges of machine learning model validation using correlated behaviour data: evaluation of cross-validation strategies and accuracy measures"

The `figures_data` folder has the values used to create the figures, while the `.dat` files have the raw data by groups.

## Data file headers

- `animal`: see Supplementary Table 1 of manuscript for information about the animals
- `t0`: unix timestamp of the start of the segment
- `t1`: unix timestamp of the end of the segment
- `label`: see Supplementary Table 2 of manuscript for information about the labels

The columns after `label` are the various feature, which are explained in Supplementary Table 3 of the manuscript.

