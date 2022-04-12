# animal-behaviour-analysis-2020
Source code and data for Ferdinandy et al. 2020, "Challenges of machine learning model validation using correlated behaviour data: evaluation of cross-validation strategies and accuracy measures"



## Data

The `figures_data` folder has the values used to create the figures, while the `.dat` files have the raw data by groups.

### Data file headers

- `animal`: see Supplementary Table 1 of manuscript for information about the animals
- `t0`: unix timestamp of the start of the segment
- `t1`: unix timestamp of the end of the segment
- `label`: see Supplementary Table 2 of manuscript for information about the labels

The columns after `label` are the various feature, which are explained in Supplementary Table 3 of the manuscript.

## Citation

When using the data, please cite the repository and the journal paper as well:

Ferdinandy B, Gerencsér L, Corrieri L, Perez P, Újváry D, Csizmadia G, et al. (2020) Challenges of machine learning model validation using correlated behaviour data: Evaluation of cross-validation strategies and accuracy measures. PLoS ONE 15(7): e0236092. https://doi.org/10.1371/journal.pone.0236092

Bence Ferdinandy. (2020, July 21). ferdinandyb/animal-behaviour-analysis-2020: v1.1.2 (Version v1.1.2). Zenodo. http://doi.org/10.5281/zenodo.3887208

```
@article{Ferdinandy2020,
author = {Ferdinandy, Bence and Gerencs{\'{e}}r, Linda and Corrieri, Luca and Perez, Paula and {\'{U}}jv{\'{a}}ry, D{\'{o}}ra and Csizmadia, G{\'{a}}bor and Mikl{\'{o}}si, {\'{A}}d{\'{a}}m},
doi = {10.1371/journal.pone.0236092},
issn = {1932-6203},
journal = {PLOS ONE},
month = {jul},
number = {7},
pages = {e0236092},
publisher = {Public Library of Science},
title = {{Challenges of machine learning model validation using correlated behaviour data: Evaluation of cross-validation strategies and accuracy measures}},
url = {https://dx.plos.org/10.1371/journal.pone.0236092},
volume = {15},
year = {2020}
}

```

```
@software{bence_ferdinandy_2020_3953387,
  author       = {Bence Ferdinandy},
  title        = {{priestoferis/animal-behaviour-analysis-2020: 
                   v1.1.1}},
  month        = jul,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v1.1.1},
  doi          = {10.5281/zenodo.3953387},
  url          = {https://doi.org/10.5281/zenodo.3953387}
}
```

