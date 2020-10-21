import sys

from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from ex03.ex03_ui import *


class MainWindow(QMainWindow, Ui_Window_3):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # QIntValidator
        self.onlyInt = QIntValidator()
        lineEdit_list = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5]
        for line_item in lineEdit_list:
            line_item.setValidator(self.onlyInt)
        # init canvas_1
        self.static_canvas_1 = FigureCanvas(Figure(figsize=(5, 3)))
        QtWidgets.QVBoxLayout(self.widget_1).addWidget(self.static_canvas_1)
        self.addToolBar(NavigationToolbar(self.static_canvas_1, self))
        self._static_ax_1 = self.static_canvas_1.figure.subplots()
        # init canvas_2
        self.static_canvas_2 = FigureCanvas(Figure(figsize=(5, 3)))
        QtWidgets.QVBoxLayout(self.widget_2).addWidget(self.static_canvas_2)
        self.addToolBar(NavigationToolbar(self.static_canvas_2, self))
        self._static_ax_2 = self.static_canvas_2.figure.subplots()
        # slot connections

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics EX03")
        self.setWindowIcon(QIcon("03.png"))
        self.show()


if __name__ == '__main__':
    app_3 = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.setStyleSheet('oxygen')
    mywin.show()
    sys.exit(app_3.exec_())
