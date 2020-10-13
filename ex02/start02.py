import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from ex02.ex02_ui import *


class MainWindow(QMainWindow, Ui_Window_2):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics EX01")
        self.setWindowIcon(QIcon("02.png"))
        self.show()


if __name__ == '__main__':
    app_2 = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.show()
    sys.exit(app_2.exec_())
