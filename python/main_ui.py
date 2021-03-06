# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KinectCapture(object):
    def setupUi(self, KinectCapture):
        KinectCapture.setObjectName("KinectCapture")
        KinectCapture.resize(1300, 880)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(KinectCapture.sizePolicy().hasHeightForWidth())
        KinectCapture.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(KinectCapture)
        self.centralwidget.setObjectName("centralwidget")
        self.StartCollect = QtWidgets.QPushButton(self.centralwidget)
        self.StartCollect.setGeometry(QtCore.QRect(500, 810, 220, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.StartCollect.setFont(font)
        self.StartCollect.setObjectName("StartCollect")
        self.ResolutionBox = QtWidgets.QComboBox(self.centralwidget)
        self.ResolutionBox.setGeometry(QtCore.QRect(10, 740, 200, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.ResolutionBox.setFont(font)
        self.ResolutionBox.setObjectName("ResolutionBox")
        self.ResolutionBox.addItem("")
        self.ResolutionBox.addItem("")
        self.ResolutionBox.addItem("")
        self.ResolutionBox.addItem("")
        self.ResolutionBox.addItem("")
        self.ResolutionBox.addItem("")
        self.ResolutionBox.addItem("")
        self.FPSBox = QtWidgets.QComboBox(self.centralwidget)
        self.FPSBox.setGeometry(QtCore.QRect(10, 810, 200, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.FPSBox.setFont(font)
        self.FPSBox.setObjectName("FPSBox")
        self.FPSBox.addItem("")
        self.FPSBox.addItem("")
        self.FPSBox.addItem("")
        self.FPSBox.addItem("")
        self.StartKinect = QtWidgets.QPushButton(self.centralwidget)
        self.StartKinect.setGeometry(QtCore.QRect(220, 740, 220, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.StartKinect.setFont(font)
        self.StartKinect.setObjectName("StartKinect")
        self.ChoosePath = QtWidgets.QPushButton(self.centralwidget)
        self.ChoosePath.setGeometry(QtCore.QRect(500, 740, 220, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.ChoosePath.setFont(font)
        self.ChoosePath.setObjectName("ChoosePath")
        self.CaptureTime = QtWidgets.QLabel(self.centralwidget)
        self.CaptureTime.setGeometry(QtCore.QRect(730, 810, 160, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.CaptureTime.setFont(font)
        self.CaptureTime.setObjectName("CaptureTime")
        self.CapturedPicsNum = QtWidgets.QLabel(self.centralwidget)
        self.CapturedPicsNum.setGeometry(QtCore.QRect(900, 810, 160, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.CapturedPicsNum.setFont(font)
        self.CapturedPicsNum.setObjectName("CapturedPicsNum")
        self.StopKinect = QtWidgets.QPushButton(self.centralwidget)
        self.StopKinect.setGeometry(QtCore.QRect(220, 810, 220, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.StopKinect.setFont(font)
        self.StopKinect.setObjectName("StopKinect")
        self.StopCollect = QtWidgets.QPushButton(self.centralwidget)
        self.StopCollect.setGeometry(QtCore.QRect(1070, 810, 220, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.StopCollect.setFont(font)
        self.StopCollect.setObjectName("StopCollect")
        self.ShowFigure = QtWidgets.QLabel(self.centralwidget)
        self.ShowFigure.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.ShowFigure.setFont(font)
        self.ShowFigure.setFrameShape(QtWidgets.QFrame.Box)
        self.ShowFigure.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ShowFigure.setText("")
        self.ShowFigure.setObjectName("ShowFigure")
        self.PathLabel = QtWidgets.QLabel(self.centralwidget)
        self.PathLabel.setGeometry(QtCore.QRect(730, 740, 560, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.PathLabel.setFont(font)
        self.PathLabel.setWordWrap(True)
        self.PathLabel.setObjectName("PathLabel")
        KinectCapture.setCentralWidget(self.centralwidget)

        self.retranslateUi(KinectCapture)
        QtCore.QMetaObject.connectSlotsByName(KinectCapture)

    def retranslateUi(self, KinectCapture):
        _translate = QtCore.QCoreApplication.translate
        KinectCapture.setWindowTitle(_translate("KinectCapture", "Kinect Capture by Van"))
        self.StartCollect.setText(_translate("KinectCapture", "开始采集"))
        self.ResolutionBox.setItemText(0, _translate("KinectCapture", "分辨率"))
        self.ResolutionBox.setItemText(1, _translate("KinectCapture", "3072P(4096*3072)"))
        self.ResolutionBox.setItemText(2, _translate("KinectCapture", "2160P(3840*2160)"))
        self.ResolutionBox.setItemText(3, _translate("KinectCapture", "1536P(2048*1536)"))
        self.ResolutionBox.setItemText(4, _translate("KinectCapture", "1440P(2560*1440)"))
        self.ResolutionBox.setItemText(5, _translate("KinectCapture", "1080P(1920*1080)"))
        self.ResolutionBox.setItemText(6, _translate("KinectCapture", "720P(1280*720)"))
        self.FPSBox.setItemText(0, _translate("KinectCapture", "帧数"))
        self.FPSBox.setItemText(1, _translate("KinectCapture", "30FPS"))
        self.FPSBox.setItemText(2, _translate("KinectCapture", "15FPS"))
        self.FPSBox.setItemText(3, _translate("KinectCapture", "5FPS"))
        self.StartKinect.setText(_translate("KinectCapture", "启动Kinect"))
        self.ChoosePath.setText(_translate("KinectCapture", "选择路径"))
        self.CaptureTime.setText(_translate("KinectCapture", "Time: 00:00"))
        self.CapturedPicsNum.setText(_translate("KinectCapture", "Nums: 0"))
        self.StopKinect.setText(_translate("KinectCapture", "关闭Kinect"))
        self.StopCollect.setText(_translate("KinectCapture", "结束采集"))
        self.PathLabel.setText(_translate("KinectCapture", "PATH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KinectCapture = QtWidgets.QMainWindow()
    ui = Ui_KinectCapture()
    ui.setupUi(KinectCapture)
    KinectCapture.show()
    sys.exit(app.exec_())
