# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QFileDialog
from retrieve import retrieve
import os
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 970)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 150, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 150, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: None;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 150, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 150, 30))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 150, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 150, 30))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 330, 150, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 370, 150, 150))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 530, 150, 30))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 570, 150, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 620, 100, 100))
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 620, 100, 100))
        self.label_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 620, 100, 100))
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 730, 100, 100))
        self.label_10.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 730, 100, 100))
        self.label_11.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(230, 730, 100, 100))
        self.label_12.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(230, 840, 100, 100))
        self.label_13.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(120, 840, 100, 100))
        self.label_14.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 840, 100, 100))
        self.label_15.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(340, 730, 100, 100))
        self.label_16.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(340, 840, 100, 100))
        self.label_17.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_17.setScaledContents(True)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(340, 620, 100, 100))
        self.label_18.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(450, 620, 100, 100))
        self.label_19.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(450, 730, 100, 100))
        self.label_20.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(450, 840, 100, 100))
        self.label_21.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 150, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 250, 150, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

         #########
        self.filebasepath = ''
        self.QueryImgPath = ''
        self.imgnum = 0
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.btn_clicked_filename_shot)
        self.pushButton_2.clicked.connect(self.btn_clicked_extractfeat_shot)
        self.pushButton_3.clicked.connect(self.btn_clicked_selectquery_shot)
        self.pushButton_4.clicked.connect(self.btn_retrieve_shot)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于VGG16的图像检索系统"))
        self.pushButton.setText(_translate("MainWindow", "选择检索的数据库路径"))
        self.label.setText(_translate("MainWindow", "图像检索系统"))
        self.label_2.setText(_translate("MainWindow", "第一步:"))
        self.label_3.setText(_translate("MainWindow", "第二步:"))
        self.pushButton_2.setText(_translate("MainWindow", "提取图片的特征"))
        self.label_4.setText(_translate("MainWindow", "第三步:"))
        self.pushButton_3.setText(_translate("MainWindow", "选择一张查询图片"))
        self.label_5.setText(_translate("MainWindow", "显示"))
        self.label_6.setText(_translate("MainWindow", "第四步:"))
        self.pushButton_4.setText(_translate("MainWindow", "开始检索"))
        self.label_7.setText(_translate("MainWindow", "显示"))
        self.label_8.setText(_translate("MainWindow", "显示"))
        self.label_9.setText(_translate("MainWindow", "显示"))
        self.label_10.setText(_translate("MainWindow", "显示"))
        self.label_11.setText(_translate("MainWindow", "显示"))
        self.label_12.setText(_translate("MainWindow", "显示"))
        self.label_13.setText(_translate("MainWindow", "显示"))
        self.label_14.setText(_translate("MainWindow", "显示"))
        self.label_15.setText(_translate("MainWindow", "显示"))
        self.label_16.setText(_translate("MainWindow", "显示"))
        self.label_17.setText(_translate("MainWindow", "显示"))
        self.label_18.setText(_translate("MainWindow", "显示"))
        self.label_19.setText(_translate("MainWindow", "显示"))
        self.label_20.setText(_translate("MainWindow", "显示"))
        self.label_21.setText(_translate("MainWindow", "显示"))

    def btn_clicked_filename_shot(self):
        self.filebasepath = QFileDialog.getExistingDirectory(None,
                                                      "选取文件夹",
                                                      "/home/zhen/DATASET")  # 起始路径

        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("MainWindow", self.filebasepath))

    def btn_clicked_extractfeat_shot(self):
        self.imgnum = os.listdir(self.filebasepath).__len__()  # 数据库图片数量

        ox = retrieve()
        print('标记')

        ImgData1 = ox.load_image(self.filebasepath,self.imgnum)
        net = ox.load_vgg16model()
        self.featall = ox.extract_vgg16feat(ImgData1)
        np.savetxt(os.path.split(self.filebasepath)[0]+'/featall.txt',self.featall)


        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_2.setText(_translate("MainWindow", '特征提取完成.....'))

    def btn_clicked_selectquery_shot(self):
        self.QueryImgPath = QFileDialog.getOpenFileName(None, "选择一个查询文件", ".",
                                                    "Image Files(*.jpg *.jpeg *.png)")[0]

        self.ImgName = sorted(os.listdir(self.filebasepath))#图片集合名字字符串列表
        self.QueryImg = os.path.split(self.QueryImgPath)[1]#查询图片名字字符串

        ##载入图片数据库文件的特征
        self.featall = np.loadtxt(os.path.split(self.filebasepath)[0]+'/featall.txt',dtype=np.float32)

        ##提取查询图片深度特征
        ox = retrieve()
        ImgData2 = ox.load_image(self.QueryImgPath, 1)#读取查询图片
        net = ox.load_vgg16model()
        self.feat = ox.extract_vgg16feat(ImgData2)
        print('查询图片特征提取完成',self.feat.shape)

        self.image = QImage(self.QueryImgPath)
        self.label_5.setPixmap(QPixmap.fromImage(self.image))
        self.label_5.setScaledContents(True)

    def btn_retrieve_shot(self):
        ox = retrieve()
        print(self.QueryImg)
        ranklist = ox.visual_result(self.filebasepath, self.QueryImg, self.ImgName,self.feat,self.featall)
        print(ranklist[:10])

        ##############

        self.image = QImage(self.filebasepath+'/'+ranklist[0])
        self.label_7.setPixmap(QPixmap.fromImage(self.image))
        self.label_7.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[1])
        self.label_8.setPixmap(QPixmap.fromImage(self.image))
        self.label_8.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[2])
        self.label_9.setPixmap(QPixmap.fromImage(self.image))
        self.label_9.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[5])
        self.label_10.setPixmap(QPixmap.fromImage(self.image))
        self.label_10.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[6])
        self.label_11.setPixmap(QPixmap.fromImage(self.image))
        self.label_11.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[7])
        self.label_12.setPixmap(QPixmap.fromImage(self.image))
        self.label_12.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[12])
        self.label_13.setPixmap(QPixmap.fromImage(self.image))
        self.label_13.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[11])
        self.label_14.setPixmap(QPixmap.fromImage(self.image))
        self.label_14.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[10])
        self.label_15.setPixmap(QPixmap.fromImage(self.image))
        self.label_15.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[8])
        self.label_16.setPixmap(QPixmap.fromImage(self.image))
        self.label_16.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[13])
        self.label_17.setPixmap(QPixmap.fromImage(self.image))
        self.label_17.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[3])
        self.label_18.setPixmap(QPixmap.fromImage(self.image))
        self.label_18.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[4])
        self.label_19.setPixmap(QPixmap.fromImage(self.image))
        self.label_19.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[9])
        self.label_20.setPixmap(QPixmap.fromImage(self.image))
        self.label_20.setScaledContents(True)

        self.image = QImage(self.filebasepath + '/' + ranklist[14])
        self.label_21.setPixmap(QPixmap.fromImage(self.image))
        self.label_21.setScaledContents(True)











if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())