# PANOSETI Data Viewer
The software is used for checking [pff](https://github.com/panoseti/panoseti/wiki/Data-file-format) file. It's based on [pyqtgraph](https://www.pyqtgraph.org), so you have to install pyqtgraph.  
I suggest you install [miniconda](https://docs.conda.io/en/latest/miniconda.html) first, and then create python3.9 environment.  
* create python3.9 environment, and then activate the environment.
```
    conda create -n PSDataViewer python==3.9
    conda activate PSDataViewer 
```
* install necessary packages
```
    pip install pyqt5
    pip install pyqtgraph
    pip install numpy
```
Then you should be able to run the software by using the following command:
```
    python PSImViewer.py
```