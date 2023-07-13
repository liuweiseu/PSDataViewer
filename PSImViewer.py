import sys,os
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import pyqtgraph as pg
import numpy as np
import pff, json
import datetime

cur_path = os.path.dirname(os.path.abspath(__file__))
uiclass, baseclass = pg.Qt.loadUiType(cur_path + "/qtviewer.ui")
             
def _cp_img(id,im0,im1):
    if(id == 0):
        sx = 0
        sy = 0
        im0 = np.rot90(im0,-1)
    elif(id == 1):
        sx = 16
        sy = 0
        im0 = np.rot90(im0,-2)
    elif(id == 3):
        sx = 0
        sy = 16 
    elif(id == 2):
        sx = 16
        sy = 16
        im0 = np.rot90(im0,-3)
    
    for i in range(16):
        for j in range(16):
            im1[sx+i,sy+j] = im0[i,j]

# tv_sec is the linux time, pkt_tai and pkt_nsec is from WR
def _caldate(tv_sec,pkt_tai,pkt_nsec):
    lo_t = datetime.datetime.fromtimestamp(tv_sec).strftime('%Y-%m-%d %H:%M:%S')
    sec = (tv_sec & 0xFFFFFFFFFFFFFC00) + pkt_tai
    wr_t = datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')
    #print('Linux time: ', lo_t)
    #print('WR time   : ', wr_t)
    return lo_t, wr_t

## pff file class
class PFFfile(object):
    def __init__(self, filename):
        self.filename = filename
        dict = pff.parse_name(self.filename)
        self.dp = dict['dp']
        if self.dp == 'img16' or self.dp =='1':
            self.image_size = 32
            self.bytes_per_pixel = 2
            self.is_ph = False
        elif self.dp == 'img8' or self.dp == '2':
            self.image_size = 32
            self.bytes_per_pixel = 1
            self.is_ph =False
        elif self.dp == 'ph256' or self.dp == 'ph16' or self.dp =='3':
            self.image_size = 16
            self.bytes_per_pixel = 2
            self.is_ph = True
        elif self.dp == 'ph1024':
            self.image_size = 32
            self.bytes_per_pixel = 2
            self.is_ph = True
        else:
            raise Exception("bad data product %s"%self.dp)
        self.fhandle = 0
        self.metadata = []
        self.data = []
        self.pktsize = []
        self.phdata = np.zeros((32,32),dtype=float)

    def openpff(self):
        self.fhandle = open(self.filename, 'rb')

    def closepff(self):
        self.fhandle.close()

    # to-do: when reading ph packets, we need to show a 32x32 image
    def readimg(self):
        self.metadata = []
        self.data = []
        # reading data from im and ph file is different
        if(self.is_ph==False or self.image_size==32):
            try:
                metadata = pff.read_json(self.fhandle)
                self.metadata = json.loads(metadata)
                rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
                if(self.is_ph == True):
                    rawdata = np.asarray(rawdata, dtype=np.int16)
                pktsize = len(metadata) + len(rawdata)*self.bytes_per_pixel + 2
                self.pktsize.append(pktsize)
                self.data = np.array(rawdata,dtype=float).reshape(self.image_size,self.image_size)
                self.data = np.transpose(self.data)
            except:
                return
        else:
            try:
                metadata = pff.read_json(self.fhandle)
                self.metadata = json.loads(metadata)
                rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
                #print(rawdata)
                if(self.is_ph == True):
                    rawdata = np.asarray(rawdata, dtype=np.int16)
                tmp = np.array(rawdata,dtype=float).reshape(self.image_size,self.image_size)
                tmp = np.transpose(tmp)
                quabo_id = self.metadata['quabo_num']
                _cp_img(quabo_id, tmp, self.phdata)
                pktsize = len(metadata) + len(rawdata)*self.bytes_per_pixel + 2
                self.pktsize.append(pktsize)
                self.data = self.phdata
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
        if(self.is_ph == False or self.image_size==32):
            metadata = pff.read_json(self.fhandle)
            self.metadata = json.loads(metadata)
            rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
            if(self.is_ph == True):
                    rawdata = np.asarray(rawdata, dtype=np.int16)
            self.data = np.array(rawdata,dtype=float).reshape(self.image_size, self.image_size)
            self.data = np.transpose(self.data)
        else:
            metadata = pff.read_json(self.fhandle)
            self.metadata = json.loads(metadata)
            rawdata = pff.read_image(self.fhandle, self.image_size, self.bytes_per_pixel)
            if(self.is_ph == True):
                    rawdata = np.asarray(rawdata, dtype=np.int16)
            tmp = np.array(rawdata,dtype=float).reshape(16,16)
            tmp = np.transpose(tmp)
            quabo_id = self.metadata['quabo_num']
            _cp_img(quabo_id, tmp, self.phdata)
            self.data = self.phdata

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
        self.imv.ui.roiBtn.setChecked(True)
        self.imv.ui.roiPlot.showGrid(x=True, y=True, alpha=0.5)
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
                for metadata in ['acq_mode','mod_num','pkt_num','pkt_tai','pkt_nsec']:
                    var = 'Q' + str(i) + '_' + metadata
                    if(metadata == 'pkt_tai'):
                        try:
                            self.__dict__[var].setText(str(self.pff.metadata[quabo]['pkt_tai']))
                        except:
                            self.__dict__[var].setText(str(self.pff.metadata[quabo]['pkt_utc']))
                        continue
                    self.__dict__[var].setText(str(self.pff.metadata[quabo][metadata]))
                tv_sec = self.pff.metadata[quabo]['tv_sec'] + 37
                pkt_tai = self.pff.metadata[quabo]['pkt_tai']
                pkt_nsec = self.pff.metadata[quabo]['pkt_nsec']
                if(tv_sec != 0):
                    [lo_t, wr_t] = _caldate(tv_sec, pkt_tai, pkt_nsec)
                    var = var = 'Q' + str(i) + '_' + 'lo_time'
                    self.__dict__[var].setText(lo_t.split(' ')[1])
                    var = var = 'Q' + str(i) + '_' + 'wr_time'
                    self.__dict__[var].setText(wr_t.split(' ')[1])
                    # lo_t.split(' ')[0] is the date, which should be the same as wr_t.split(' ')[0]
                    self.Q_date.setText(lo_t.split(' ')[0])
        elif(self.pff.image_size == 16):
            quabo_id = self.pff.metadata['quabo_num']
            group_id = 'Quabo'+str(quabo_id)+'metadata'
            self.__dict__[group_id].setStyleSheet('QGroupBox:title {color: rgb(255, 0, 255);}')
            quabo = 'quabo_' + str(quabo_id)
            for metadata in ['pkt_num','pkt_tai','pkt_nsec']:
                    var = 'Q' + str(quabo_id) + '_' + metadata
                    if(metadata == 'pkt_tai'):
                        try:
                            self.__dict__[var].setText(str(self.pff.metadata['pkt_tai']))
                        except:
                            self.__dict__[var].setText(str(self.pff.metadata['pkt_utc']))
                        continue
                    self.__dict__[var].setText(str(self.pff.metadata[metadata]))
            tv_sec = self.pff.metadata['tv_sec'] + 37
            try:
                pkt_tai = self.pff.metadata['pkt_tai']
            except:
                pkt_tai = self.pff.metadata['pkt_utc']
            pkt_nsec = self.pff.metadata['pkt_nsec']
            if(tv_sec != 0):
                    [lo_t, wr_t] = _caldate(tv_sec, pkt_tai, pkt_nsec)
                    var = var = 'Q' + str(quabo_id) + '_' + 'lo_time'
                    self.__dict__[var].setText(lo_t.split(' ')[1])
                    var = var = 'Q' + str(quabo_id) + '_' + 'wr_time'
                    self.__dict__[var].setText(wr_t.split(' ')[1])
                    # lo_t.split(' ')[0] is the date, which should be the same as wr_t.split(' ')[0]
                    self.Q_date.setText(lo_t.split(' ')[0])
        elif(self.pff.image_size == 32):
            for i in range(0,4):
                quabo = 'quabo_' + str(i)
                for metadata in ['pkt_num','pkt_tai','pkt_nsec']:
                    var = 'Q' + str(i) + '_' + metadata
                    if(metadata == 'pkt_tai'):
                        try:
                            self.__dict__[var].setText(str(self.pff.metadata[quabo]['pkt_tai']))
                        except:
                            self.__dict__[var].setText(str(self.pff.metadata[quabo]['pkt_utc']))
                        continue
                    self.__dict__[var].setText(str(self.pff.metadata[quabo][metadata]))
                tv_sec = self.pff.metadata[quabo]['tv_sec'] + 37
                pkt_tai = self.pff.metadata[quabo]['pkt_tai']
                pkt_nsec = self.pff.metadata[quabo]['pkt_nsec']
                if(tv_sec != 0):
                    [lo_t, wr_t] = _caldate(tv_sec, pkt_tai, pkt_nsec)
                    var = var = 'Q' + str(i) + '_' + 'lo_time'
                    self.__dict__[var].setText(lo_t.split(' ')[1])
                    var = var = 'Q' + str(i) + '_' + 'wr_time'
                    self.__dict__[var].setText(wr_t.split(' ')[1])
                    # lo_t.split(' ')[0] is the date, which should be the same as wr_t.split(' ')[0]
                    self.Q_date.setText(lo_t.split(' ')[0])
    def openfile(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self,  "Select","./", "All Files (*);;Text Files (*.pff)") 
        self.filename = directory[0]
        self.pff = PFFfile(self.filename)
        self.pff.openpff()
        self.pff.readimg()
        self.showmetadata()
        self.showimg()
        self.FileNameLabel.setText(self.filename.split('/')[-1])

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()

if __name__=='__main__':
    main()
