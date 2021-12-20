import sys
import os
import json

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect
import main_ui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QResizeEvent

class MainWindowClass(QMainWindow, main_ui.Ui_KinectCapture):
    def __init__(self, parent = None):

        super(MainWindowClass, self).__init__(parent)
        self.setupUi(self)
        
        self.ResolutionBox.currentIndexChanged.connect(self.actionResolutionChange)
        self.FPSBox.currentIndexChanged.connect(self.actionFPSChange)
        self.resolutionval = 0
        self.fpsval = 0
        self.flag_start_kinect = False
        self.flag_start_capture = False

        self.StartCollect.setEnabled(False)
        self.StartKinect.setEnabled(False)

        self.StartKinect.clicked.connect(self.actionStartKinect)

    def actionStartKinect(self):
        if self.flag_start_kinect:
            pass
        else:
            self.flag_start_kinect = True
            os.system(".\..\Debug\KinectCapture.exe %d %d"%(self.resolutionval, self.fpsval))

    def actionFPSChange(self, i):
        print("FPS changed to option:"+str(i))
        self.fpsval = i
        if self.fpsval != 0 and self.resolutionval != 0:
            self.StartKinect.setEnabled(True)
        else:
            self.StartKinect.setEnabled(False)

    def actionResolutionChange(self, i):
        print("Resolution changed to option:"+str(i))
        self.resolutionval = i
        if self.fpsval != 0 and self.resolutionval != 0:
            self.StartKinect.setEnabled(True)
        else:
            self.StartKinect.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindowClass()
    main_window.show()
    sys.exit(app.exec_())