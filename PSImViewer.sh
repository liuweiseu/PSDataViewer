#! /bin/bash

# conda environment is necessary
source ~/Software/anaconda3/bin/activate
conda activate panoseti

cur_path=/home/wei/Projects/Panoseti/panoseti_data/PSImViewer
python $cur_path/PSImViewer.py
