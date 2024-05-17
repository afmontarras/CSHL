# CSHL

## Installation
### Environment Manager
If not already you need to install either:
- Anaconda/Miniconda: https://docs.anaconda.com/free/anaconda/install/index.html
- Mamba/Miniforge: https://github.com/conda-forge/miniforge (https://mamba.readthedocs.io/en/latest/index.html)
### Create your CSHL environment
You can use either `conda` or `mamba` commands.  
Write in your terminal:
```
cd <path to CSHL directory>
conda env create -n ENVNAME --file CSHL.yml
```
### Activate the CSHL env and launch jupyter lab
```
conda activate CSHL
jupyter lab
```
### Add aditional packages.
- pyABF : https://swharden.com/pyabf/
```
python -m pip install --upgrade pyabf
```
- Stimfit: https://github.com/neurodroid/stimfit/wiki/Stimfit / https://neurodroid.github.io/stimfit/stfio/index.html