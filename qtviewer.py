# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtviewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 661, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label0.setObjectName("label0")
        self.FileNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.FileNameLabel.setGeometry(QtCore.QRect(80, 10, 601, 17))
        self.FileNameLabel.setObjectName("FileNameLabel")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(700, 600, 160, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PreviousButton = QtWidgets.QPushButton(self.splitter)
        self.PreviousButton.setObjectName("PreviousButton")
        self.NextButton = QtWidgets.QPushButton(self.splitter)
        self.NextButton.setObjectName("NextButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(680, 40, 191, 551))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.Quabo0metadata = QtWidgets.QGroupBox(self.groupBox)
        self.Quabo0metadata.setGeometry(QtCore.QRect(10, 30, 171, 121))
        self.Quabo0metadata.setObjectName("Quabo0metadata")
        self.label = QtWidgets.QLabel(self.Quabo0metadata)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Quabo0metadata)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Quabo0metadata)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Quabo0metadata)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Quabo0metadata)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 17))
        self.label_5.setObjectName("label_5")
        self.acq_mode = QtWidgets.QLabel(self.Quabo0metadata)
        self.acq_mode.setGeometry(QtCore.QRect(90, 20, 81, 17))
        self.acq_mode.setObjectName("acq_mode")
        self.mod_num = QtWidgets.QLabel(self.Quabo0metadata)
        self.mod_num.setGeometry(QtCore.QRect(90, 40, 81, 17))
        self.mod_num.setObjectName("mod_num")
        self.pkt_num = QtWidgets.QLabel(self.Quabo0metadata)
        self.pkt_num.setGeometry(QtCore.QRect(90, 60, 81, 17))
        self.pkt_num.setObjectName("pkt_num")
        self.pkt_utc = QtWidgets.QLabel(self.Quabo0metadata)
        self.pkt_utc.setGeometry(QtCore.QRect(90, 80, 81, 17))
        self.pkt_utc.setObjectName("pkt_utc")
        self.label_15 = QtWidgets.QLabel(self.Quabo0metadata)
        self.label_15.setGeometry(QtCore.QRect(90, 100, 81, 17))
        self.label_15.setObjectName("label_15")
        self.Quabo1metadata = QtWidgets.QGroupBox(self.groupBox)
        self.Quabo1metadata.setGeometry(QtCore.QRect(10, 160, 171, 121))
        self.Quabo1metadata.setObjectName("Quabo1metadata")
        self.label_6 = QtWidgets.QLabel(self.Quabo1metadata)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Quabo1metadata)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Quabo1metadata)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Quabo1metadata)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Quabo1metadata)
        self.label_10.setGeometry(QtCore.QRect(10, 100, 71, 17))
        self.label_10.setObjectName("label_10")
        self.acq_mode_2 = QtWidgets.QLabel(self.Quabo1metadata)
        self.acq_mode_2.setGeometry(QtCore.QRect(90, 20, 81, 17))
        self.acq_mode_2.setObjectName("acq_mode_2")
        self.mod_num_2 = QtWidgets.QLabel(self.Quabo1metadata)
        self.mod_num_2.setGeometry(QtCore.QRect(90, 40, 81, 17))
        self.mod_num_2.setObjectName("mod_num_2")
        self.pkt_num_2 = QtWidgets.QLabel(self.Quabo1metadata)
        self.pkt_num_2.setGeometry(QtCore.QRect(90, 60, 81, 17))
        self.pkt_num_2.setObjectName("pkt_num_2")
        self.pkt_utc_2 = QtWidgets.QLabel(self.Quabo1metadata)
        self.pkt_utc_2.setGeometry(QtCore.QRect(90, 80, 81, 17))
        self.pkt_utc_2.setObjectName("pkt_utc_2")
        self.label_16 = QtWidgets.QLabel(self.Quabo1metadata)
        self.label_16.setGeometry(QtCore.QRect(90, 100, 81, 17))
        self.label_16.setObjectName("label_16")
        self.Quabo2metadata = QtWidgets.QGroupBox(self.groupBox)
        self.Quabo2metadata.setGeometry(QtCore.QRect(10, 290, 171, 121))
        self.Quabo2metadata.setObjectName("Quabo2metadata")
        self.label_19 = QtWidgets.QLabel(self.Quabo2metadata)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Quabo2metadata)
        self.label_20.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Quabo2metadata)
        self.label_21.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Quabo2metadata)
        self.label_22.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Quabo2metadata)
        self.label_23.setGeometry(QtCore.QRect(10, 100, 71, 17))
        self.label_23.setObjectName("label_23")
        self.acq_mode_4 = QtWidgets.QLabel(self.Quabo2metadata)
        self.acq_mode_4.setGeometry(QtCore.QRect(90, 20, 81, 17))
        self.acq_mode_4.setObjectName("acq_mode_4")
        self.mod_num_4 = QtWidgets.QLabel(self.Quabo2metadata)
        self.mod_num_4.setGeometry(QtCore.QRect(90, 40, 81, 17))
        self.mod_num_4.setObjectName("mod_num_4")
        self.pkt_num_4 = QtWidgets.QLabel(self.Quabo2metadata)
        self.pkt_num_4.setGeometry(QtCore.QRect(90, 60, 81, 17))
        self.pkt_num_4.setObjectName("pkt_num_4")
        self.pkt_utc_4 = QtWidgets.QLabel(self.Quabo2metadata)
        self.pkt_utc_4.setGeometry(QtCore.QRect(90, 80, 81, 17))
        self.pkt_utc_4.setObjectName("pkt_utc_4")
        self.label_24 = QtWidgets.QLabel(self.Quabo2metadata)
        self.label_24.setGeometry(QtCore.QRect(90, 100, 81, 17))
        self.label_24.setObjectName("label_24")
        self.Quabo3metadata = QtWidgets.QGroupBox(self.groupBox)
        self.Quabo3metadata.setGeometry(QtCore.QRect(10, 420, 171, 121))
        self.Quabo3metadata.setObjectName("Quabo3metadata")
        self.label_25 = QtWidgets.QLabel(self.Quabo3metadata)
        self.label_25.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.Quabo3metadata)
        self.label_26.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Quabo3metadata)
        self.label_27.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Quabo3metadata)
        self.label_28.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Quabo3metadata)
        self.label_29.setGeometry(QtCore.QRect(10, 100, 71, 17))
        self.label_29.setObjectName("label_29")
        self.acq_mode_5 = QtWidgets.QLabel(self.Quabo3metadata)
        self.acq_mode_5.setGeometry(QtCore.QRect(90, 20, 81, 17))
        self.acq_mode_5.setObjectName("acq_mode_5")
        self.mod_num_5 = QtWidgets.QLabel(self.Quabo3metadata)
        self.mod_num_5.setGeometry(QtCore.QRect(90, 40, 81, 17))
        self.mod_num_5.setObjectName("mod_num_5")
        self.pkt_num_5 = QtWidgets.QLabel(self.Quabo3metadata)
        self.pkt_num_5.setGeometry(QtCore.QRect(90, 60, 81, 17))
        self.pkt_num_5.setObjectName("pkt_num_5")
        self.pkt_utc_5 = QtWidgets.QLabel(self.Quabo3metadata)
        self.pkt_utc_5.setGeometry(QtCore.QRect(90, 80, 81, 17))
        self.pkt_utc_5.setObjectName("pkt_utc_5")
        self.label_30 = QtWidgets.QLabel(self.Quabo3metadata)
        self.label_30.setGeometry(QtCore.QRect(90, 100, 81, 17))
        self.label_30.setObjectName("label_30")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 876, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionExit_2)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label0.setText(_translate("MainWindow", "Filename:"))
        self.FileNameLabel.setText(_translate("MainWindow", "test.pff"))
        self.PreviousButton.setText(_translate("MainWindow", "Previous"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.groupBox.setTitle(_translate("MainWindow", "Metadata"))
        self.Quabo0metadata.setTitle(_translate("MainWindow", "Quabo0"))
        self.label.setText(_translate("MainWindow", "acq_mode:"))
        self.label_2.setText(_translate("MainWindow", "mod_num:"))
        self.label_3.setText(_translate("MainWindow", "pkt_num:"))
        self.label_4.setText(_translate("MainWindow", "pkt_utc:"))
        self.label_5.setText(_translate("MainWindow", "pkt_nsec:"))
        self.acq_mode.setText(_translate("MainWindow", "0"))
        self.mod_num.setText(_translate("MainWindow", "0"))
        self.pkt_num.setText(_translate("MainWindow", "0"))
        self.pkt_utc.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.Quabo1metadata.setTitle(_translate("MainWindow", "Quabo1"))
        self.label_6.setText(_translate("MainWindow", "acq_mode:"))
        self.label_7.setText(_translate("MainWindow", "mod_num:"))
        self.label_8.setText(_translate("MainWindow", "pkt_num:"))
        self.label_9.setText(_translate("MainWindow", "pkt_utc:"))
        self.label_10.setText(_translate("MainWindow", "pkt_nsec:"))
        self.acq_mode_2.setText(_translate("MainWindow", "0"))
        self.mod_num_2.setText(_translate("MainWindow", "0"))
        self.pkt_num_2.setText(_translate("MainWindow", "0"))
        self.pkt_utc_2.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "0"))
        self.Quabo2metadata.setTitle(_translate("MainWindow", "Quabo2"))
        self.label_19.setText(_translate("MainWindow", "acq_mode:"))
        self.label_20.setText(_translate("MainWindow", "mod_num:"))
        self.label_21.setText(_translate("MainWindow", "pkt_num:"))
        self.label_22.setText(_translate("MainWindow", "pkt_utc:"))
        self.label_23.setText(_translate("MainWindow", "pkt_nsec:"))
        self.acq_mode_4.setText(_translate("MainWindow", "0"))
        self.mod_num_4.setText(_translate("MainWindow", "0"))
        self.pkt_num_4.setText(_translate("MainWindow", "0"))
        self.pkt_utc_4.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "0"))
        self.Quabo3metadata.setTitle(_translate("MainWindow", "Quabo3"))
        self.label_25.setText(_translate("MainWindow", "acq_mode:"))
        self.label_26.setText(_translate("MainWindow", "mod_num:"))
        self.label_27.setText(_translate("MainWindow", "pkt_num:"))
        self.label_28.setText(_translate("MainWindow", "pkt_utc:"))
        self.label_29.setText(_translate("MainWindow", "pkt_nsec:"))
        self.acq_mode_5.setText(_translate("MainWindow", "0"))
        self.mod_num_5.setText(_translate("MainWindow", "0"))
        self.pkt_num_5.setText(_translate("MainWindow", "0"))
        self.pkt_utc_5.setText(_translate("MainWindow", "0"))
        self.label_30.setText(_translate("MainWindow", "0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
