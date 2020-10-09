import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime

from main_ui import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.label_4.setText(QDateTime.currentDateTime().toString('yyyy.MM.dd'))
        self.pushButton_1.clicked.connect(self.execute_1)
        self.pushButton_2.clicked.connect(self.execute_2)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics Experiment")
        self.setWindowIcon(QIcon("001.png"))
        self.show()

    def execute_1(self):
        self.close()
        os.system("python3 ./ex01/start01.py")
        # TODO: bug exists ---- QIcon cannot display when called

    def execute_2(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
