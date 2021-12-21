import sys
import os
import json
import subprocess
import threading
import time
import win32file
import numpy as np
import cv2

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect
import main_ui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QResizeEvent, QImage, QPixmap

def openKinect(resolution, fps):
    subprocess.run(".\..\Debug\KinectCapture.exe %d %d"%(resolution, fps))

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
        self.StopKinect.clicked.connect(self.actionStopKinect)
        self.kinectThread = threading.Thread(target=openKinect, args=(self.resolutionval, self.fpsval))
        
    
    def actionStartKinect(self):
        if self.flag_start_kinect:
            pass
        else:
            self.flag_start_kinect = True
            self.kinectThread.start()
            print("Wait for thread to begin...")
            time.sleep(5)
            print("Suppose that Kinect is opened...")
            self.filehandle = win32file.CreateFile("\\\\.\\pipe\\mynamedpipe",
        win32file.GENERIC_READ | win32file.GENERIC_WRITE,
        0, None,
        win32file.OPEN_EXISTING,
        0, None)
            while(self.flag_start_kinect):
                request_msg = "Request color image"
                win32file.WriteFile(self.filehandle, request_msg.encode())
                # Read reply data, need to be in same order/size as how you write them in the pipe server in pipe_streaming_example/main.cpp
                color_data = win32file.ReadFile(self.filehandle, 1280 * 720 * 4)
                # Reshape for image visualization
                color_img_full = np.frombuffer(color_data[1], dtype=np.uint8).reshape(720, 1280, 4).copy()
                color_img_full_trans = cv2.cvtColor(color_img_full, cv2.COLOR_BGR2RGB)
                qt_color_img_full = QImage(color_img_full_trans.data, 1280, 720, QImage.Format_RGB888)
                self.ShowFigure.setPixmap(QPixmap.fromImage(qt_color_img_full))
                QApplication.processEvents()
    
    def actionStopKinect(self):
        self.flag_start_kinect = False
        request_msg = "X"
        win32file.WriteFile(self.filehandle, request_msg.encode())
        self.kinectThread = threading.Thread(target=openKinect, args=(self.resolutionval, self.fpsval))



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