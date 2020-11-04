import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from final.final_ui import *


class MainWindow(QMainWindow, Ui_Window_4):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.radioButton_1.toggled.connect(self.horizontalSlider.setEnabled)
        self.radioButton_2.toggled.connect(self.horizontalSlider.setDisabled)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics Final")
        self.setWindowIcon(QIcon("04.png"))
        self.show()


if __name__ == '__main__':
    app_4 = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.setStyleSheet('oxygen')
    mywin.show()
    sys.exit(app_4.exec_())
