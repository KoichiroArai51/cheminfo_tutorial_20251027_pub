# MOLE tutorial

### Data set link
- Pre trained model ckpt file can be downloaded from following URL.
  - [check point file](https://codeocean.com/capsule/2105466/tree/v1/data/MolE_GuacaMol_27113.ckpt)
  - [related discussion](https://github.com/recursionpharma/mole_public/issues/2)
  - [all dataset](https://codeocean.com/capsule/2105466/tree/v1)

### Modify your config file before running the code
- please change config file of MOLE
- yourenv/mole_public/mole/training/configs/models/finetune.yaml
```
# Line 13~
# Default setting of epochs will take long time.
 data:
    trainer:
      #max_epochs: 100
      max_epochs: 20 # or more smaller
```

### Code link
- [github link](https://github.com/recursionpharma/mole_public)
