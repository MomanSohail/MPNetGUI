# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updated.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import argparse
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

import Encoder.encoder as en
import Train.train as tr



class UiMainWindow(object):
    def __init__(self):
        self.dimension = None
        self.dataset_path = None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(939, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 310, 901, 531))
        self.frame_3.setStyleSheet("background:rgb(114, 159, 207)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 881, 45))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnLoadEnvironment = QtWidgets.QPushButton(self.frame_6)
        self.btnLoadEnvironment.setObjectName("btnLoadEnvironment")
        self.horizontalLayout_3.addWidget(self.btnLoadEnvironment)
        self.btnLoadObstacle = QtWidgets.QPushButton(self.frame_6)
        self.btnLoadObstacle.setObjectName("btnLoadObstacle")
        self.horizontalLayout_3.addWidget(self.btnLoadObstacle)
        self.btnQuery = QtWidgets.QPushButton(self.frame_6)
        self.btnQuery.setObjectName("btnQuery")
        self.horizontalLayout_3.addWidget(self.btnQuery)
        self.btnComputePath = QtWidgets.QPushButton(self.frame_6)
        self.btnComputePath.setObjectName("btnComputePath")
        self.horizontalLayout_3.addWidget(self.btnComputePath)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 881, 501))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 70, 901, 191))
        self.frame_4.setStyleSheet("background:rgb(211, 215, 207)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.EncodingProgressBar = QtWidgets.QProgressBar(self.frame_4)
        self.EncodingProgressBar.setGeometry(QtCore.QRect(20, 90, 861, 25))
        self.EncodingProgressBar.setProperty("value", 24)
        self.EncodingProgressBar.setObjectName("EncodingProgressBar")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(20, 20, 861, 61))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoadData = QtWidgets.QPushButton(self.frame_5)
        self.btnLoadData.setObjectName("btnLoadData")
        self.btnLoadData.clicked.connect(self.load_dataset)
        self.horizontalLayout.addWidget(self.btnLoadData)
        self.btnSelectType = QtWidgets.QPushButton(self.frame_5)
        self.btnSelectType.setObjectName("btnSelectType")
        self.btnSelectType.clicked.connect(self.select_dimensions)
        self.horizontalLayout.addWidget(self.btnSelectType)
        self.btnStartTraining = QtWidgets.QPushButton(self.frame_5)
        self.btnStartTraining.setObjectName("btnStartTraining")
        self.btnStartTraining.clicked.connect(self.start_train)
        self.horizontalLayout.addWidget(self.btnStartTraining)
        self.TrainingProgressBar = QtWidgets.QProgressBar(self.frame_4)
        self.TrainingProgressBar.setGeometry(QtCore.QRect(20, 140, 861, 25))
        self.TrainingProgressBar.setProperty("value", 0)
        self.TrainingProgressBar.setObjectName("TrainingProgressBar")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 151, 31))
        self.label_6.setStyleSheet("color:rgb(0, 0, 0);\n"
                                   "font: 75 italic 20pt \"Ubuntu\";\n"
                                   "background:rgb(243, 243, 243);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 151, 31))
        self.label_7.setStyleSheet("color:rgb(0, 0, 0);\n"
                                   "font: 75 italic 20pt \"Ubuntu\";\n"
                                   "background:rgb(186, 189, 182);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClick = QtWidgets.QAction(MainWindow)
        self.actionClick.setObjectName("actionClick")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame_3.setAccessibleName(_translate("MainWindow", "QFTrainer"))
        self.btnLoadEnvironment.setText(_translate("MainWindow", "Load Environment"))
        self.btnLoadObstacle.setText(_translate("MainWindow", "Load Obstacle"))
        self.btnQuery.setToolTip(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#a40000;\">Configure number of paths and environments</span></p></body></html>"))
        self.btnQuery.setText(_translate("MainWindow", "Query"))
        self.btnComputePath.setText(_translate("MainWindow", "Compute Path"))
        self.frame_4.setAccessibleName(_translate("MainWindow", "QFEncoder"))
        self.btnLoadData.setText(_translate("MainWindow", "Load Data"))
        self.btnSelectType.setText(_translate("MainWindow", "Select Type"))
        self.btnStartTraining.setText(_translate("MainWindow", "Start Training"))
        self.label_6.setText(_translate("MainWindow", "Train Model"))
        self.label_7.setText(_translate("MainWindow", "Neural Planner"))
        self.actionClick.setText(_translate("MainWindow", "Click"))
        self.actionClick.setToolTip(_translate("MainWindow", "on click"))
        self.actionClick.setShortcut(_translate("MainWindow", "Ctrl+L"))

    def load_dataset(self):
        self.dataset_path = self.browse_directory()

    def select_dimensions(self):
        self.dimension = QInputDialog.getInt(None, 'selection Dialog', 'select Dimension:', min=2, max=3)
        print(self.dimension[0])

    @staticmethod
    def browse_directory():
        path = QFileDialog.getExistingDirectory(None, "select folder")
        return path

    @staticmethod
    def browse_files():
        return QFileDialog.getOpenFileName(None, "select file", os.getcwd(), filter="All Files (*);;")

    def start_train(self):
        en.main(self.dataset_path, self.dimension[0], self.EncodingProgressBar)
        tr.main(self.dataset_path, self.dimension[0], self.EnProgressBar)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
