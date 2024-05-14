# CSHL

## Installation
### Environment Manager
If not already you need to install either:
- Anaconda/Miniconda: https://docs.anaconda.com/free/anaconda/install/index.html
- Mamba/Miniforge (preferred): https://github.com/conda-forge/miniforge (https://mamba.readthedocs.io/en/latest/index.html)
### Create your CSHL environment
if you use the conda commands you can replace `mamba` with `conda`.  
Write in your terminal:
```
cd <path to CSHL directory>
mamba env create -n ENVNAME --file CSHL.yml
```
### Activate the CSHL env and launch jupyter lab
```
mamba activate CSHL
jupyter lab
```