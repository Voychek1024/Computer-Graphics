# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\final_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window_4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(20, 20, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_0.setFont(font)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 190, 271, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 120, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 120, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 260, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 330, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 400, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 230, 271, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 470, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 120, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 120, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 150, 271, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 530, 271, 161))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.label_4.setNum)
        self.horizontalSlider.valueChanged['int'].connect(self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.radioButton_1, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_0.setText(_translate("MainWindow", "Computer Graphics\n"
                                                      "Final Object"))
        self.label_1.setText(_translate("MainWindow", "Control Points"))
        self.label_2.setText(_translate("MainWindow", "1"))
        self.pushButton_1.setText(_translate("MainWindow", "Reset Points"))
        self.pushButton_2.setText(_translate("MainWindow", "Randomize Points"))
        self.pushButton_3.setText(_translate("MainWindow", "Read from file"))
        self.pushButton_4.setText(_translate("MainWindow", "Save Plot"))
        self.label_4.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "×"))
        self.radioButton_1.setText(_translate("MainWindow", "show"))
        self.radioButton_2.setText(_translate("MainWindow", "hide"))
        self.label.setText(_translate("MainWindow", "Guidance:\n"
                                                    "鼠标右键——旋转\n"
                                                    "鼠标中键——缩放\n"
                                                    "鼠标左键+滚轮——修改控制点\n"
                                                    "Q——开启GL光照（长按循环旋转）\n"
                                                    "E——关闭光照\n"
                                                    "L/K——下一个控制点（白色高亮）"))
