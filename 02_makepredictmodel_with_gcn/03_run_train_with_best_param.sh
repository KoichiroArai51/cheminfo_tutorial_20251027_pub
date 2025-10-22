#!/usr/bin/bash
# https://chemprop.readthedocs.io/en/latest/tutorial/cli/hpopt.html
# train a model using the best hyperparameters found during hyperparameter optimization

chemprop train --data-path data.csv \
	--config-path hpopt_data/best_config.toml \
	--smiles-column MOL_smiles \
	--epochs 10 \
	--output-dir train_data_with_hopt

