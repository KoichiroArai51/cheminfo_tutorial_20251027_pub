# cheminfo_tutorial_20250127

## Overview
- Material for cheminformatics tutorial of CBI 2025.
- We will try to build GCN models and try to fine tune of foundation moldel.
- Please ignore warnings when you run the code on jupyter.
- 今回のチュートリアルにおいて、学習のEpochは非常に少なく設定してあります。GPUが利用できる環境下で参加される場合は適宜Epochsを増やしていただいて大丈夫です。CPUのみの環境で参加される方は、チュートリアル中は流れを把握していただく形にとどめていただくのが良いかと思います。

## Installation
#### *Please check network poricy of your organization if you would like to use your organization network.*
#### *Proxy settings are required for git, wget, conda etc. We can not support your organization network settings.*
#### **会社や大学のネットワークをご利用される場合プロキシー設定などをしていないと適切にパッケージのインストールができない可能性があります。Github、Conda、Pip、Wgetなど利用するものが問題なく通信できるか確認をお願いいたします。主催者側で参加される皆様の組織におけるネットワークポリシーに関する問題は対応できません。プロキシ関連の設定の情報を参考情報として最後に記載しておきます。**
- Install [git](https://git-scm.com/downloads)
- Gitのインストールをします。OSに応じて適宜コマンドを変更して下さい。
```sh
# Following example code is used for Linux
apt-get install git
```
- Get materials for the tutorial
- 今回のチュートリアルで使うコードをGithubからCloneします。Cloneができない場合はZipファイルとして入手し、利用していただいても大丈夫です。
```sh
# you can use git clone with SSH or Git CLI
# Following code is an example
git clone https://github.com/cbi-society/cheminfo_tutorial_20251027_pub.git
cd cheminfo_tutorial_20251027_pub 
```
- Install [miniforge](https://github.com/conda-forge/miniforge).
- After installing miniforge, mamba commad will be available. Please check more deitails in original [documentation](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
- Miniforgeをインストールします。既にご自身の環境下に同様のものをインストールされている場合はこの作業はスキップしていただいて構いません。mambaはcondaより高速に動作するので、condaしか使えない場合はmambaを使えるようにすることをお勧めいたします。
```sh
# Following example code is used for Linux
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```
- Make conda enviromnet for the tutorial
```sh
# you can use your own favorite env name
conda create -n cbi2025 python=3.12
```
- Install required packages
```sh
conda activate cbi2025
mamba install -c conda-forge datamol molfeat medchem splito
mamba install -c conda-forge jupyterlab
mamba install -c conda-forge notebook # if would like to use  jupyter notebook instead of jupyter-lab
mamba install -c conda-forge auroris polaris openpyxl gcsfs umap-learn ipywidgets
mamba install -c conda-forge chemprop tensorboard bokeh
mamba install -c conda-forge zarr"<3.0" # if your conda installed zarr >= 3.0
pip install -U ray[tune]
pip install hyperopt
```
- Install MolE in another environmet
```
# suitable python version is 3.9 or 3.10
cd ~/your_own_path
git clone https://github.com/recursionpharma/mole_public.git
cd mole_public
mamba create -n mole python=3.10
conda activate mole
mamba install -c conda-forge jupyter
# For Mac or CPU only:
pip install -r requirements/main_3.10.txt

# For CUDA:
pip install -r requirements/main_3.10_gpu.txt

pip install -e .
```
- Download pre-trained model(MolE_GaucaMol_27113.ckpt) checkpoint file from following URL. 
- The size of this ckpt file is about 1GB. Please download the file in advance.[ckpt file link](https://codeocean.com/capsule/2105466/tree/v1/data/MolE_GuacaMol_27113.ckpt)


## References and Links
- [Chemprop: A Machine Learning Package for Chemical Property Prediction](https://pubs.acs.org/doi/10.1021/acs.jcim.3c01250)
- [chemprop_githubrepo](https://github.com/chemprop/chemprop)
- [Descriptor-based Foundation Models for Molecular Property Prediction](https://arxiv.org/abs/2506.15792)
- [MolE: a foundation model for molecular graphs using disentangled attention](https://www.nature.com/articles/s41467-024-53751-y)
- [Recursion news](https://www.recursion.com/news/introducing-mole-a-new-model-for-predicting-molecular-properties-for-ai-drug-design-and-beyond)
- [MolE_githubrepo](https://github.com/recursionpharma/mole_public)
- [github proxy settings example](https://qiita.com/hidetzu/items/c2db95613ba594a2ef25)
- [wget proxy settings example](https://medium.com/@datajournal/wget-with-a-proxy-b8dfe3576ab3)
- [conda proxy settings example](https://www.anaconda.com/docs/getting-started/working-with-conda/reference/proxy)

## Requirements
Please check the documentation above.

## Contributing
Please post issue if you find

## License
ChemProp: MIT, MolE: Attribution-NonCommercial 4.0 International

## Contact
Please post question to (discussion)[https://github.com/cbi-society/cheminfo_tutorial_20251027_pub/discussions].

## Author
- Taka@iwatobipen
- Kazufumi Ohkawa
- Koichiro Arai
- Natsumi Miyano
- Kazutoshi Takahashi
