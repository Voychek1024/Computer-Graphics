# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 251, 71))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 210, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 270, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 330, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Computer Graphics\n"
                                                      "Experiments"))
        self.label_2.setText(_translate("MainWindow", "Group 10"))
        self.label_3.setText(_translate("MainWindow", "组长: 李嘉琪\n"
                                                      "组员: 李沛迪\n"
                                                      "朱舒倩"))
        self.pushButton_1.setText(_translate("MainWindow", "EX01"))
        self.pushButton_2.setText(_translate("MainWindow", "EX02"))
        self.pushButton_3.setText(_translate("MainWindow", "……"))
        self.label_4.setText(_translate("MainWindow", "2020.10.09"))
        self.label_5.setText(_translate("MainWindow", "ver 0.1.2"))