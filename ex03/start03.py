import sys

import math
import random
import numpy as np

from PyQt5.QtGui import QIcon, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from ex03.ex03_ui import *


def de_casteljau(coordArr, i, j, _t):
    if j == 0:
        return coordArr[i]
    return de_casteljau(coordArr, i, j - 1, _t) * (1 - _t) + de_casteljau(coordArr, i + 1, j - 1, _t) * _t


def drawReference(ax, _item: tuple, _coord: tuple, _type_in_use: str):
    ax.scatter(_item[0], _item[1], s=10, c='r')
    ax.scatter(_coord[0], _coord[1], s=10, c='r')
    ax.plot([_item[0], _coord[0]], [_item[1], _coord[1]], _type_in_use, alpha=0.5)


def drawLine(ax, coordinates: list, _color: str):
    x, y = zip(*coordinates)
    ax.scatter(x, y, s=10, c='r')
    for i in range(len(coordinates) - 1):
        if coordinates[i] != coordinates[i + 1]:
            x_values = [coordinates[i][0], coordinates[i + 1][0]]
            y_values = [coordinates[i][1], coordinates[i + 1][1]]
            ax.plot(x_values, y_values, color=_color)
        else:
            continue


def translation(ax, _coords: list, _t_vector: list):
    result = []
    trans = np.identity(3, dtype=float)
    trans[0][2] = _t_vector[0]
    trans[1][2] = _t_vector[1]
    trans[2][2] = 1
    for item in _coords:
        vec = np.append(np.array(item, dtype=float), [1])
        new_vec = trans @ vec
        result.append((new_vec[0], new_vec[1]))
        drawReference(ax, (new_vec[0], new_vec[1]), item, 'r--')
    return result


def scaling(ax, _coords: list, _s_vector: list, _center: tuple):
    result = []
    trans = np.identity(3, dtype=float)
    trans[0][0] = _s_vector[0]
    trans[1][1] = _s_vector[1]
    trans[0][2] = _center[0] * (1 - _s_vector[0])
    trans[1][2] = _center[1] * (1 - _s_vector[0])
    for item in _coords:
        drawReference(ax, item, _center, 'b--')
        vec = np.append(np.array(item, dtype=float), [1])
        new_vec = trans @ vec
        result.append((new_vec[0], new_vec[1]))
        drawReference(ax, (new_vec[0], new_vec[1]), _center, 'r--')
    return result


def rotation(ax, _coords: list, _r_vector: float, _center: tuple):
    result = []
    trans = np.identity(3, dtype=float)
    cos_value = np.cos(_r_vector)
    sin_value = np.sin(_r_vector)
    trans[0][0] = cos_value
    trans[0][1] = -sin_value
    trans[0][2] = _center[0] * (1 - cos_value) + _center[1] * sin_value
    trans[1][0] = sin_value
    trans[1][1] = cos_value
    trans[1][2] = _center[1] * (1 - cos_value) - _center[0] * sin_value
    for item in _coords:
        drawReference(ax, item, _center, 'b--')
        vec = np.append(np.array(item, dtype=float), [1])
        new_vec = trans @ vec
        result.append((new_vec[0], new_vec[1]))
        drawReference(ax, (new_vec[0], new_vec[1]), _center, 'r--')
    return result


class MainWindow(QMainWindow, Ui_Window_3):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # setup variables
        self.trans_coords = []
        # setup UI
        self.setupUi(self)
        # QIntValidator
        self.double_check = QDoubleValidator()
        lineEdit_list = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
                         self.lineEdit_5, self.lineEdit_6, self.lineEdit_7]
        for line_item in lineEdit_list:
            line_item.setValidator(self.double_check)
        self.onlyInt = QIntValidator()
        lineEdit_list = [self.lineEdit_8, self.lineEdit_9, self.lineEdit_10]
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
        self.radioButton_1.clicked.connect(self.disable_1)
        self.radioButton_2.clicked.connect(self.disable_2)
        self.radioButton_3.clicked.connect(self.disable_3)
        self.pushButton_1.clicked.connect(self.plot_1)
        self.pushButton_2.clicked.connect(self.initmap_1)
        self.pushButton_3.clicked.connect(self.initmap_2)
        self.pushButton_4.clicked.connect(self.plot_2)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics EX03")
        self.setWindowIcon(QIcon("ex03/03.png"))
        self.show()

    def disable_1(self):
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_1.setEnabled(True)
        self.lineEdit_2.setEnabled(True)

    def disable_2(self):
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)

    def disable_3(self):
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)

    def plot_1(self):
        self._static_ax_1.clear()
        coordArrX = [random.randint(0, 500) for _ in range(4)]
        coordArrY = [random.randint(0, 500) for _ in range(4)]
        self._static_ax_1.plot(coordArrX, coordArrY, 'x--', lw=2, color='black', ms=10)
        positions = []
        numSteps = 10000
        for k in range(numSteps):
            t = float(k) / (numSteps - 1)
            x = float(de_casteljau(coordArrX, 0, 3, t))
            y = float(de_casteljau(coordArrY, 0, 3, t))
            positions.append((x, y))
        x_value, y_value = zip(*positions)
        self._static_ax_1.plot(x_value, y_value, lw=2)
        self._static_ax_1.grid(True)
        self.static_canvas_1.draw()

    def initmap_1(self):
        self._static_ax_1.clear()
        self.static_canvas_1.draw()

    def initmap_2(self):
        self._static_ax_2.clear()
        self.trans_coords = []
        try:
            vertices, range_start, range_end = [int(self.lineEdit_8.text()), int(self.lineEdit_9.text()),
                                                int(self.lineEdit_10.text())]
            coords = [(random.randint(range_start, range_end), random.randint(range_start, range_end))
                      for _ in range(vertices)]
            coords.append(coords[0])
            drawLine(self._static_ax_2, coords, 'g')
            self._static_ax_2.grid(True)
            self.static_canvas_2.draw()
            self.trans_coords = coords
        except ValueError:
            return

    def plot_2(self):
        if self.radioButton_1.isChecked():
            self._static_ax_2.clear()
            try:
                t_vector = [float(self.lineEdit_1.text()), float(self.lineEdit_2.text())]
                drawLine(self._static_ax_2, self.trans_coords, 'g')
                trans_coords = translation(self._static_ax_2, self.trans_coords, t_vector)
                drawLine(self._static_ax_2, trans_coords, 'y')
                self._static_ax_2.grid(True)
                self.static_canvas_2.draw()
            except ValueError:
                return
        elif self.radioButton_2.isChecked():
            self._static_ax_2.clear()
            try:
                s_vector = [float(self.lineEdit_3.text()), float(self.lineEdit_4.text())]
                reference_coord = (float(self.lineEdit_6.text()), float(self.lineEdit_7.text()))
                drawLine(self._static_ax_2, self.trans_coords, 'g')
                scale_coords = scaling(self._static_ax_2, self.trans_coords, s_vector, reference_coord)
                drawLine(self._static_ax_2, scale_coords, 'y')
                self._static_ax_2.grid(True)
                self.static_canvas_2.draw()
            except ValueError:
                return
        elif self.radioButton_3.isChecked():
            self._static_ax_2.clear()
            try:
                r_vector = math.radians(float(self.lineEdit_5.text()))
                reference_coord = (float(self.lineEdit_6.text()), float(self.lineEdit_7.text()))
                drawLine(self._static_ax_2, self.trans_coords, 'g')
                scale_coords = rotation(self._static_ax_2, self.trans_coords, r_vector, reference_coord)
                drawLine(self._static_ax_2, scale_coords, 'y')
                self._static_ax_2.grid(True)
                self.static_canvas_2.draw()
            except ValueError:
                return
        else:
            return


if __name__ == '__main__':
    app_3 = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.setStyleSheet('oxygen')
    mywin.show()
    sys.exit(app_3.exec_())
