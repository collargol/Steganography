# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Studia\Krypto\Steganography\gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import AudioImageProcessing
import threading

threads = []

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(722, 474)
        MainWindow.setMinimumSize(QtCore.QSize(722, 474))
        MainWindow.setMaximumSize(QtCore.QSize(721, 474))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Paomedia-Small-N-Flat-Key.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 30, 311, 271))
        self.label.setObjectName(_fromUtf8("label"))
        self.guiLog = QtGui.QTextBrowser(self.centralwidget)
        self.guiLog.setGeometry(QtCore.QRect(20, 301, 681, 121))
        self.guiLog.setObjectName(_fromUtf8("guiLog"))
        self.guiTabs = QtGui.QTabWidget(self.centralwidget)
        self.guiTabs.setGeometry(QtCore.QRect(20, 30, 351, 251))
        self.guiTabs.setObjectName(_fromUtf8("guiTabs"))
        self.guiTabToSound = QtGui.QWidget()
        self.guiTabToSound.setObjectName(_fromUtf8("guiTabToSound"))
        self.guiToSoundSoundDirButt = QtGui.QPushButton(self.guiTabToSound)
        self.guiToSoundSoundDirButt.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.guiToSoundSoundDirButt.setObjectName(_fromUtf8("guiToSoundSoundDirButt"))
        self.guiToSoundImDirButt = QtGui.QPushButton(self.guiTabToSound)
        self.guiToSoundImDirButt.setGeometry(QtCore.QRect(10, 80, 31, 21))
        self.guiToSoundImDirButt.setObjectName(_fromUtf8("guiToSoundImDirButt"))
        self.guiToSoundSoundDirEdit = QtGui.QLineEdit(self.guiTabToSound)
        self.guiToSoundSoundDirEdit.setGeometry(QtCore.QRect(50, 30, 281, 21))
        self.guiToSoundSoundDirEdit.setDragEnabled(False)
        self.guiToSoundSoundDirEdit.setReadOnly(True)
        self.guiToSoundSoundDirEdit.setObjectName(_fromUtf8("guiToSoundSoundDirEdit"))
        self.guiToSoundImageDirEdit = QtGui.QLineEdit(self.guiTabToSound)
        self.guiToSoundImageDirEdit.setGeometry(QtCore.QRect(50, 80, 281, 21))
        self.guiToSoundImageDirEdit.setDragEnabled(False)
        self.guiToSoundImageDirEdit.setReadOnly(True)
        self.guiToSoundImageDirEdit.setObjectName(_fromUtf8("guiToSoundImageDirEdit"))
        self.label_2 = QtGui.QLabel(self.guiTabToSound)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.guiTabToSound)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.guiToSoundChannelGroup = QtGui.QGroupBox(self.guiTabToSound)
        self.guiToSoundChannelGroup.setGeometry(QtCore.QRect(10, 110, 120, 101))
        self.guiToSoundChannelGroup.setObjectName(_fromUtf8("guiToSoundChannelGroup"))
        self.guiChannelsLeftB = QtGui.QRadioButton(self.guiToSoundChannelGroup)
        self.guiChannelsLeftB.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.guiChannelsLeftB.setObjectName(_fromUtf8("guiChannelsLeftB"))
        self.guiChannelsRightB = QtGui.QRadioButton(self.guiToSoundChannelGroup)
        self.guiChannelsRightB.setGeometry(QtCore.QRect(10, 70, 95, 20))
        self.guiChannelsRightB.setObjectName(_fromUtf8("guiChannelsRightB"))
        self.guiChannelsLRB = QtGui.QRadioButton(self.guiToSoundChannelGroup)
        self.guiChannelsLRB.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.guiChannelsLRB.setChecked(True)
        self.guiChannelsLRB.setObjectName(_fromUtf8("guiChannelsLRB"))
        self.guiBitsSlider = QtGui.QSlider(self.guiTabToSound)
        self.guiBitsSlider.setGeometry(QtCore.QRect(200, 140, 121, 22))
        self.guiBitsSlider.setMinimum(0)
        self.guiBitsSlider.setMaximum(3)
        self.guiBitsSlider.setPageStep(1)
        self.guiBitsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.guiBitsSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.guiBitsSlider.setTickInterval(0)
        self.guiBitsSlider.setObjectName(_fromUtf8("guiBitsSlider"))
        self.label_4 = QtGui.QLabel(self.guiTabToSound)
        self.label_4.setGeometry(QtCore.QRect(160, 110, 171, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.guiBitsEdit = QtGui.QLineEdit(self.guiTabToSound)
        self.guiBitsEdit.setGeometry(QtCore.QRect(160, 140, 31, 22))
        self.guiBitsEdit.setReadOnly(True)
        self.guiBitsEdit.setObjectName(_fromUtf8("guiBitsEdit"))
        self.guiEncodeButt = QtGui.QPushButton(self.guiTabToSound)
        self.guiEncodeButt.setGeometry(QtCore.QRect(160, 180, 161, 28))
        self.guiEncodeButt.setObjectName(_fromUtf8("guiEncodeButt"))
        self.guiTabs.addTab(self.guiTabToSound, _fromUtf8(""))
        self.guiTabFromSound = QtGui.QWidget()
        self.guiTabFromSound.setObjectName(_fromUtf8("guiTabFromSound"))
        self.label_8 = QtGui.QLabel(self.guiTabFromSound)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.guiFromSoundImageDirEdit = QtGui.QLineEdit(self.guiTabFromSound)
        self.guiFromSoundImageDirEdit.setGeometry(QtCore.QRect(50, 80, 281, 21))
        self.guiFromSoundImageDirEdit.setDragEnabled(False)
        self.guiFromSoundImageDirEdit.setReadOnly(True)
        self.guiFromSoundImageDirEdit.setObjectName(_fromUtf8("guiFromSoundImageDirEdit"))
        self.guiFromSoundSoundDirEdit = QtGui.QLineEdit(self.guiTabFromSound)
        self.guiFromSoundSoundDirEdit.setGeometry(QtCore.QRect(50, 30, 281, 21))
        self.guiFromSoundSoundDirEdit.setDragEnabled(False)
        self.guiFromSoundSoundDirEdit.setReadOnly(True)
        self.guiFromSoundSoundDirEdit.setObjectName(_fromUtf8("guiFromSoundSoundDirEdit"))
        self.guiFromSoundSoundDirButt = QtGui.QPushButton(self.guiTabFromSound)
        self.guiFromSoundSoundDirButt.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.guiFromSoundSoundDirButt.setObjectName(_fromUtf8("guiFromSoundSoundDirButt"))
        self.guiFromSoundImDirButt = QtGui.QPushButton(self.guiTabFromSound)
        self.guiFromSoundImDirButt.setGeometry(QtCore.QRect(10, 80, 31, 21))
        self.guiFromSoundImDirButt.setObjectName(_fromUtf8("guiFromSoundImDirButt"))
        self.label_9 = QtGui.QLabel(self.guiTabFromSound)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 151, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.guiEncodeButt_3 = QtGui.QPushButton(self.guiTabFromSound)
        self.guiEncodeButt_3.setGeometry(QtCore.QRect(160, 180, 161, 28))
        self.guiEncodeButt_3.setObjectName(_fromUtf8("guiEncodeButt_3"))
        self.guiTabs.addTab(self.guiTabFromSound, _fromUtf8(""))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(450, 430, 251, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.guiToSoundSoundDirButt.clicked.connect(self.toSoundSoundButtonClicked)
        self.guiToSoundImDirButt.clicked.connect(self.toSoundImageButtonClicked)
        self.guiFromSoundImDirButt.clicked.connect(self.fromSoundImageButtonClicked)
        self.guiFromSoundSoundDirButt.clicked.connect(self.fromSoundSoundButtonClicked)
        self.guiBitsEdit.setText(str(1))
        self.guiBitsSlider.valueChanged.connect(lambda e: self.guiBitsEdit.setText(str(2**e)))
        self.guiEncodeButt.clicked.connect(self.encodeStart)
        self.guiEncodeButt_3.clicked.connect(self.decodeStart) #decode button
        self.guiTabs.currentChanged.connect(self.tabChanged)

        t = threading.Thread(target=self.threadLogReader)
        threads.append(t)
        t.start()
        
        self.retranslateUi(MainWindow)
        self.guiTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Private Investigations", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/catty/catty.png\"/></p></body></html>", None))
        self.guiToSoundSoundDirButt.setText(_translate("MainWindow", "...", None))
        self.guiToSoundImDirButt.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Image file:", None))
        self.label_3.setText(_translate("MainWindow", "Sound file:", None))
        self.guiToSoundChannelGroup.setTitle(_translate("MainWindow", "Channel", None))
        self.guiChannelsLeftB.setText(_translate("MainWindow", "Left Only", None))
        self.guiChannelsRightB.setText(_translate("MainWindow", "Right Only", None))
        self.guiChannelsLRB.setText(_translate("MainWindow", "L+R", None))
        self.label_4.setText(_translate("MainWindow", "Image bits per sound sample", None))
        self.guiEncodeButt.setText(_translate("MainWindow", "Encode", None))
        self.guiTabs.setTabText(self.guiTabs.indexOf(self.guiTabToSound), _translate("MainWindow", "Encode", None))
        self.label_8.setText(_translate("MainWindow", "Sound file:", None))
        self.guiFromSoundSoundDirButt.setText(_translate("MainWindow", "...", None))
        self.guiFromSoundImDirButt.setText(_translate("MainWindow", "...", None))
        self.label_9.setText(_translate("MainWindow", "Image output directory:", None))
        self.guiEncodeButt_3.setText(_translate("MainWindow", "Decode", None))
        self.guiTabs.setTabText(self.guiTabs.indexOf(self.guiTabFromSound), _translate("MainWindow", "Decode", None))
        self.label_10.setText(_translate("MainWindow", "©2018 Piotr Mikołajek & Michał Trojnarski", None))

    #moves options between tabs
    def tabChanged(self, tab_ind):
        if tab_ind == 1 :
            new_parent = self.guiTabFromSound
        else:
            new_parent = self.guiTabToSound
        self.guiBitsSlider.setParent(new_parent)
        self.guiBitsSlider.show()
        self.guiToSoundChannelGroup.setParent(new_parent)
        self.guiToSoundChannelGroup.show()
        self.label_4.setParent(new_parent)
        self.label_4.show()
        self.guiBitsEdit.setParent(new_parent)
        self.guiBitsEdit.show()

    def logPrint(self, data):
        self.guiLog.append(time.ctime()+": " +data)
    def toSoundSoundButtonClicked(self):
        file = str(QtGui.QFileDialog.getOpenFileName(self.centralwidget, "Select File", 
         'c:\\',"Audio files (*.wav)"))
        self.guiToSoundSoundDirEdit.setText(file)
    def toSoundImageButtonClicked(self):
        file = str(QtGui.QFileDialog.getOpenFileName(self.centralwidget, "Select File", 
         'c:\\',"Image files (*.jpg)"))
        self.guiToSoundImageDirEdit.setText(file)
    def fromSoundSoundButtonClicked(self):
        file = str(QtGui.QFileDialog.getOpenFileName(self.centralwidget, "Select File", 
         'c:\\',"Audio files (*.wav)"))
        self.guiFromSoundSoundDirEdit.setText(file)
    def fromSoundImageButtonClicked(self):
        file = str(QtGui.QFileDialog.getExistingDirectory(self.centralwidget, "Select Directory"))
        self.guiFromSoundImageDirEdit.setText(file)
    def encodeStart(self):
        imageDir = self.guiToSoundImageDirEdit.text()
        if len(imageDir) < 3 :  
            self.logPrint("Improper input image file directory")
            return
        soundDir = self.guiToSoundSoundDirEdit.text()
        if len(soundDir) < 3 :  
            self.logPrint("Improper input sound file directory")
            return
        channel = []
        if self.guiChannelsLeftB.isChecked():
            channel = 'L'
        elif self.guiChannelsRightB.isChecked():
            channel = 'R'
        else:
            channel = 'L+R'
        bits = int(self.guiBitsEdit.text())

        self.logPrint('Starting encoding: \n - Audio File: ' + soundDir + '\n - Image File: ' + imageDir + '\n - Channels used: ' + channel + '\n - LSB used: '  + str(bits))

        outputDir = '/'.join(soundDir.split("/")[:-1]) + '/' + soundDir.split("/")[-1].split(".")[0] + "ENCODED.wav";

        print(outputDir)
        t = threading.Thread(target=AudioImageProcessing.AudioImageProcessing.encodeImageInSoundWithWriting ,  args=(soundDir,imageDir,outputDir,channel,bits,))
        threads.append(t)
        t.start()
    def decodeStart(self):
        imageDir = self.guiFromSoundImageDirEdit.text()
        if len(imageDir) < 3 :  
            self.logPrint("Improper output image file directory")
            return
        soundDir = self.guiFromSoundSoundDirEdit.text()
        if len(soundDir) < 3 :  
            self.logPrint("Improper input sound file directory")
            return
        channel = []
        if self.guiChannelsLeftB.isChecked():
            channel = 'L'
        elif self.guiChannelsRightB.isChecked():
            channel = 'R'
        else:
            channel = 'L+R'
        bits = int(self.guiBitsEdit.text())
 
        self.logPrint('Starting decoding: \n - Audio File: ' + soundDir + '\n - Output directory: ' + imageDir)
        t = threading.Thread(target=AudioImageProcessing.AudioImageProcessing.decodeImageFromAudio ,  args=(soundDir,imageDir+'\DECODED.jpg',channel,bits,))
        threads.append(t)
        t.start()
    def threadLogReader(self):
        while(1) :
            if AudioImageProcessing.AudioImageProcessing.logGet():
                for s in AudioImageProcessing.AudioImageProcessing.logGet() : self.logPrint(s)
                AudioImageProcessing.AudioImageProcessing.logClear()
            time.sleep(0.1)
            

import gui_z_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

