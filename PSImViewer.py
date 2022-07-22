import sys,os
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import pyqtgraph as pg
import numpy as np
import pff, json
import datetime

cur_path = os.path.dirname(os.path.abspath(__file__))
uiclass, baseclass = pg.Qt.loadUiType(cur_path + "/qtviewer.ui")

## pff file class
class PFFfile(object):
    def __init__(self, filename):
        self.filename = filename
        dict = pff.parse_name(self.filename)
        self.dp = dict['dp']
        if self.dp == 'img16' or self.dp=='1':
            self.image_size = 32
            self.bytes_per_pixel = 2
            self.is_ph = False
        elif self.dp == 'ph16' or self.dp=='3':
            self.image_size = 16
            self.bytes_per_pixel = 2
            self.is_ph = True
        else:
            raise Exception("bad data product %s"%self.dp)
        self.fhandle = 0
        self.metadata = []
        self.data = []
        self.pktsize = []
        self.phdata = [0 for i in range(32*32)]

    def openpff(self):
        self.fhandle = open(self.filename, 'rb')

    def closepff(self):
        self.fhandle.close()

    # to-do: when reading ph packets, we need to show a 32x32 image
    def readimg(self):
        self.metadata = []
        self.data = []
        # reading data from im and ph file is different
        if(self.is_ph==False):
            try:
                metadata = pff.read_json(self.fhandle)
                self.metadata = json.loads(metadata)
                rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
                pktsize = len(metadata) + len(rawdata)*self.bytes_per_pixel + 2
                self.pktsize.append(pktsize)
                self.data = np.array(rawdata,dtype=float).reshape(self.image_size,self.image_size)
            except:
                return
        else:
            try:
                metadata = pff.read_json(self.fhandle)
                self.metadata = json.loads(metadata)
                q_rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
                quabo_id = self.metadata['quabo_num']
                self.phdata[quabo_id *16*16:(quabo_id+1)*16*16] = list(q_rawdata)
                rawdata = self.phdata
                print(rawdata)
                pktsize = len(metadata) + len(q_rawdata)*self.bytes_per_pixel + 2
                self.pktsize.append(pktsize)
                self.data = np.array(rawdata,dtype=float).reshape(32,32)
            except:
                return

    
    def readpreimg(self):
        self.metadata = []
        self.data = []
        try:
            self.fhandle.seek(-1*(self.pktsize[-1] + self.pktsize[-2]),1)
            self.pktsize.pop()
        except:
            return
        metadata = pff.read_json(self.fhandle)
        self.metadata = json.loads(metadata)
        rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
        self.data = np.array(rawdata,dtype=float).reshape(self.image_size, self.image_size)

## ImageVew class
class ImageView(object):
    def __init__(self):
        self.imv = pg.ImageView()
        colors = np.ones((256, 3))
        for i in range(0,256):
            colors[i,0] = i
            colors[i,1] = i
            colors[i,2] = 255-i
        cmap = pg.ColorMap(pos=np.linspace(0.0, 1.0, 256), color=colors)
        self.imv.setColorMap(cmap)
        self.imv.ui.roiBtn.setChecked(False)
        self.imv.roiClicked()
        self.imv.setImage(np.zeros((32,32)))

    def updateimg(self,d):
        self.imv.setImage(d)

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.win = ImageView()
        self.verticalLayout.addWidget(self.win.imv)
        self.filename = 'None'
        self.pff = 0
        self.FileNameLabel.setText(self.filename)

        # connect click operations to functions
        self.NextButton.clicked.connect(lambda:self.next())
        self.PreviousButton.clicked.connect(lambda:self.previous())
        self.SelectFileAction.triggered.connect(lambda:self.openfile())
    
    # connected functions
    def showimg(self):
        self.win.updateimg(self.pff.data)

    def next(self):
        self.pff.readimg()
        if(len(self.pff.metadata) == 0):
            QtWidgets.QMessageBox.warning(self,'Warning','This is the last image!')
        else:
            self.showimg()
            self.showmetadata()
    
    def previous(self):
        self.pff.readpreimg()
        if(len(self.pff.metadata) == 0):
            QtWidgets.QMessageBox.warning(self,'Warning','This is the first image!')
        else:
            self.showimg()
            self.showmetadata()

    def showmetadata(self):
        # metadata in im packets and ph packets are different
        for i in range(0,4):
            group_id = 'Quabo'+str(i)+'metadata'
            self.__dict__[group_id].setStyleSheet('QGroupBox:title {color: rgb(0, 0, 0);}')
        if(self.pff.is_ph==False):
            for i in range(0,4):
                quabo = 'quabo_' + str(i)
                for metadata in ['acq_mode','mod_num','pkt_num','pkt_utc','pkt_nsec']:
                    var = 'Q' + str(i) + '_' + metadata
                    self.__dict__[var].setText(str(self.pff.metadata[quabo][metadata]))
        else:
            quabo_id = self.pff.metadata['quabo_num']
            group_id = 'Quabo'+str(quabo_id)+'metadata'
            self.__dict__[group_id].setStyleSheet('QGroupBox:title {color: rgb(255, 0, 255);}')
            quabo = 'quabo_' + str(quabo_id)
            for metadata in ['acq_mode','mod_num','pkt_num','pkt_utc','pkt_nsec']:
                    var = 'Q' + str(quabo_id) + '_' + metadata
                    self.__dict__[var].setText(str(self.pff.metadata[metadata]))
        # to-do: add time convertion code
        # datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    def openfile(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self,  "Select","./", "All Files (*);;Text Files (*.pff)") 
        self.filename = directory[0]
        self.pff = PFFfile(self.filename)
        self.pff.openpff()
        self.pff.readimg()
        self.showmetadata()
        self.showimg()
        self.FileNameLabel.setText(self.filename)

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()

if __name__=='__main__':
    main()