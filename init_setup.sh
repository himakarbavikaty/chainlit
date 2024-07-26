echo [$(date)]: "START"
echo [$(date)]: "creating a conda env with python 3.10"
conda create -p ./env python=3.10 -y
echo [$(date)]: "created a conda env"
source activate ./env
echo [$(date)]: "activated the conda env"
echo [$(date)]: "installing required packages"
pip install -r requirements.txt
echo [$(date)]: "installed required packages"
echo [$(date)]: "END"


