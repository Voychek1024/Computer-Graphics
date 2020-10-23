import math
import random
import sys
from typing import Tuple

import numpy as np
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from ex02.ex02_ui import *


def change_shapes(shapes):
    _new_shapes = {}
    for i in range(len(shapes)):
        _l = len(shapes[i][1])
        _new_shapes[i] = np.zeros((_l, 2), dtype='int')
        for j in range(_l):
            _new_shapes[i][j, 0] = shapes[i][0][j]
            _new_shapes[i][j, 1] = shapes[i][1][j]
    return _new_shapes


class LineBuilder:
    def __init__(self, ax, color, canvas):
        self.line = ax
        self.ax = ax
        self.color = color
        self.xs = []
        self.ys = []
        self.cid = ax.figure.canvas.mpl_connect('button_press_event', self)
        self.counter = 0
        self.shape_counter = 0
        self.shape = {}
        self.precision = 10
        self.output = []
        self.canvas = canvas

    def __call__(self, event):
        if event.inaxes != self.line.axes:
            return
        if self.counter == 0:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
        if np.abs(event.xdata - self.xs[0]) <= self.precision and np.abs(
                event.ydata - self.ys[0]) <= self.precision and self.counter != 0:
            self.xs.append(self.xs[0])
            self.ys.append(self.ys[0])
            self.ax.scatter(self.xs, self.ys, s=120, color=self.color)
            self.ax.scatter(self.xs[0], self.ys[0], s=80, color='blue')
            self.ax.plot(self.xs, self.ys, color=self.color)
            self.line.figure.canvas.draw()
            self.shape[self.shape_counter] = [self.xs, self.ys]
            self.shape_counter = self.shape_counter + 1
            self.xs = []
            self.ys = []
            self.counter = 0
            self.output = list(change_shapes(self.shape)[0].tolist())
            print(self.output)
            ET_ = drawLine(self.ax, self.output)
            drawScanLine(self.ax, self.output, ET_)
            self.canvas.draw()
            self.output = []
            self.shape_counter = 0
            self.shape = {}
        else:
            if self.counter != 0:
                self.xs.append(event.xdata)
                self.ys.append(event.ydata)
            self.ax.scatter(self.xs, self.ys, s=100, color=self.color)
            self.ax.plot(self.xs, self.ys, color=self.color)
            self.line.figure.canvas.draw()
            self.counter = self.counter + 1


def create_shape_on_image(widget, ax, data):
    _ax = ax
    _ax.set_xlim(0, data[:, :, 0].shape[1])
    _ax.set_ylim(0, data[:, :, 0].shape[0])
    linebuilder = LineBuilder(ax, 'red', widget)
    widget.draw()
    print(linebuilder.output)


def drawLine(ax, coordinates: list):
    ET_ = []
    for i in range(len(coordinates) - 1):
        if coordinates[i] != coordinates[i + 1]:
            x_values = [coordinates[i][0], coordinates[i + 1][0]]
            y_values = [coordinates[i][1], coordinates[i + 1][1]]
            ax.plot(x_values, y_values, color='g')
            try:
                # edge = [ind, ymax, xofymin, slopeinverse]
                edge = [min(y_values), max(y_values), min([coordinates[i], coordinates[i + 1]], key=lambda t: t[1])[0],
                        1 / ((y_values[1] - y_values[0]) / (x_values[1] - x_values[0]))]
                if edge not in ET_:
                    ET_.append(edge)
            except ZeroDivisionError:
                if (y_values[1] - y_values[0]) == 0:
                    edge = [min(y_values), max(y_values), min(x_values), math.inf]
                    if edge not in ET_:
                        ET_.append(edge)
                elif (x_values[1] - x_values[0]) == 0:
                    edge = [min(y_values), max(y_values), min(x_values), 0]
                    if edge not in ET_:
                        ET_.append(edge)
        else:
            continue
    ET_.sort()
    print("ET: \n", np.array(ET_))
    return np.array(ET_)


def drawScanLine(ax, coordinates: list, ET_):
    x_, y_ = zip(*coordinates)
    ind, ymax, xofymin, slopeinverse = zip(*ET_)
    print(ind, ymax, xofymin, slopeinverse)
    AEL = []
    for i in range(min(y_), max(y_) + 1):
        y_values = [i, i]
        x_values = [min(x_), max(x_)]
        ax.plot(x_values, y_values, color='b', alpha=0.1)

    ind = np.array(ind)
    ymax = np.array(ymax)
    for y_scan in range(min(y_), max(y_)):
        print(y_scan, end=' ')

        if y_scan in ymax:
            print("Pop Process")
            b = np.where(ymax == y_scan)
            print(b)
            self_iter = 0
            for j in range(np.size(b)):
                print("j:{},a:{}".format(j, b[0][j]))
                try:
                    AEL.pop(b[0][j] - self_iter)
                    ymax = np.delete(ymax, b)
                    print(ymax)
                    self_iter += 1
                except IndexError:
                    continue
            print(np.array(AEL))

        if y_scan in ind:
            print("Append Process")
            a = np.where(ind == y_scan)
            for j in range(np.size(a)):
                print("j:{},a:{}".format(j, a[0][j]))
                AEL.append(ET_[a[0][j]])
                AEL = sorted(AEL, key=lambda a_entry: a_entry[2])
                ymax = np.array(AEL)[:, 1]
            print(np.array(AEL))

        # Do Filling
        for i in range(0, len(AEL), 2):
            try:
                print("Pair: ", AEL[i], AEL[i + 1])
                y_value = [y_scan, y_scan]
                if AEL[i][3] == math.inf or AEL[i + 1][3] == math.inf:
                    raise OverflowError
                if AEL[i][2] > AEL[i + 1][2]:
                    c = AEL[i][2]
                    x_value = [math.ceil(AEL[i + 1][2]), math.floor(c)]
                else:
                    c = AEL[i + 1][2]
                    x_value = [math.ceil(AEL[i][2]), math.floor(c)]
                print("plotting...", x_value, y_value)
                ax.plot(x_value, y_value, c='r')
            except IndexError:
                continue
            except OverflowError:
                # case 1: Horizontal, ind == ymax, serve once and skip it.
                # case 2: Vertical, ind != ymax, AEL["indices"][3]=0, do normally
                try:
                    b = np.where(np.array(AEL) == math.inf)
                    AEL.pop(b[0][0])
                    ymax = np.delete(ymax, b[0][0])
                except IndexError:
                    continue
                continue

        for i in range(0, len(AEL), 2):
            try:
                if AEL[i][3] != math.inf and AEL[i + 1][3] != math.inf:
                    AEL[i][2] += AEL[i][3]
                    AEL[i + 1][2] += AEL[i + 1][3]
                else:
                    raise OverflowError
            except IndexError:
                continue
            except OverflowError:
                continue


def cohen_sutherland(xmin: float, ymax: float, xmax: float, ymin: float, x1: float, y1: float, x2: float, y2: float
                     ) -> Tuple[float, float, float, float]:
    INSIDE, LEFT, RIGHT, LOWER, UPPER = 0, 1, 2, 4, 8

    def _get_clip(xa, ya):
        p = INSIDE
        # consider x
        if xa < xmin:
            p |= LEFT
        elif xa > xmax:
            p |= RIGHT
        # consider y
        if ya < ymin:
            p |= LOWER
        elif ya > ymax:
            p |= UPPER
        return p

    k1 = _get_clip(x1, y1)
    k2 = _get_clip(x2, y2)

    while (k1 | k2) != 0:
        if (k1 & k2) != 0:
            raise OverflowError
        opt = k1 or k2
        if opt & UPPER:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif opt & LOWER:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif opt & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif opt & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        else:
            raise RuntimeError('Undefined clipping state')
        if opt == k1:
            x1, y1 = x, y
            k1 = _get_clip(x1, y1)
        elif opt == k2:
            x2, y2 = x, y
            k2 = _get_clip(x2, y2)
    return x1, y1, x2, y2


def clip_line(_xmin, _xmax, _ymin, _ymax, x1, y1, x2, y2):
    _x1, _y1, _x2, _y2 = cohen_sutherland(xmin=_xmin, xmax=_xmax, ymin=_ymin, ymax=_ymax, x1=x1, y1=y1, x2=x2, y2=y2)
    _x_value = [_x1, _x2]
    _y_value = [_y1, _y2]
    return _x_value, _y_value


def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0])

    def computeIntersection():
        dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
        dp = [s[0] - e[0], s[1] - e[1]]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0]
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3]

    outputList = subjectPolygon
    cp1 = clipPolygon[-1]

    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]

        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                outputList.append(e)
            elif inside(s):
                outputList.append(computeIntersection())
            s = e
        cp1 = cp2
    return outputList


def drawLine_with_color(ax, coordinates: list, _color: str):
    for i in range(len(coordinates) - 1):
        if coordinates[i] != coordinates[i + 1]:
            x_values = [coordinates[i][0], coordinates[i + 1][0]]
            y_values = [coordinates[i][1], coordinates[i + 1][1]]
            ax.plot(x_values, y_values, color=_color)


class MainWindow(QMainWindow, Ui_Window_2):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        # QIntValidator
        self.onlyInt = QIntValidator()
        lineEdit_list = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_4, self.lineEdit_5,
                         self.lineEdit_6, self.lineEdit_7]
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
        self.pushButton_1.clicked.connect(self.plot_1)
        self.pushButton_2.clicked.connect(self.plot_2)
        self.radioButton_3.clicked.connect(self.initmap_1)
        self.radioButton_4.clicked.connect(self.disable_1)
        self.radioButton_1.clicked.connect(self.disable_2)
        self.radioButton_2.clicked.connect(self.disable_2)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics EX02")
        self.setWindowIcon(QIcon("ex02/02.png"))
        self.show()

    def disable_1(self):
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.lineEdit_1.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton_1.setEnabled(True)

    def disable_2(self):
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.pushButton_1.setEnabled(False)
        self.pushButton_2.setEnabled(True)

    def initmap_1(self):
        # Interactive Plotting implementation
        self.disable_1()
        self._static_ax_1.clear()
        img = np.full((100, 100, 3), 255, dtype='uint')
        create_shape_on_image(self.static_canvas_1, self._static_ax_1, img)
        self._static_ax_1.grid(True)
        self.static_canvas_1.draw()

    def plot_1(self):
        """
        plotting template: plot following widget draw(to update)
        self._static_ax_1.plot(...)
        self.static_canvas_1.draw()
        """
        if self.radioButton_4.isChecked():
            # Scan Line Filling Algorithm implementation
            self._static_ax_1.clear()
            try:
                vertices, coord_range = [int(self.lineEdit_1.text()), int(self.lineEdit_2.text())]
            except ValueError:
                return
            coords = [[random.randint(0, coord_range), random.randint(0, coord_range)] for _ in range(vertices)]
            coords.append(coords[0])
            ET = drawLine(self._static_ax_1, coords)
            drawScanLine(self._static_ax_1, coords, ET)
            self._static_ax_1.grid(True)
            self.static_canvas_1.draw()

    def plot_2(self):
        self._static_ax_2.clear()
        if self.radioButton_1.isChecked():
            # Cohen-Sutherland Algorithm implementation
            try:
                xmin, xmax, ymin, ymax = [int(self.lineEdit_4.text()), int(self.lineEdit_5.text()),
                                          int(self.lineEdit_6.text()), int(self.lineEdit_7.text())]
                coords = (xmin, xmax, ymin, ymax)
                clipper = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax), (xmin, ymin)]
                drawLine_with_color(self._static_ax_2, clipper, 'r')
                for i in range(10):
                    print("draw{}".format(i))
                    x1_, y1_, x2_, y2_ = (random.randint(min(coords) - 50, max(coords) + 50) for _ in range(4))
                    x_values = [x1_, x2_]
                    y_values = [y1_, y2_]
                    self._static_ax_2.plot(x_values, y_values, linewidth=2, alpha=0.7, color='b')
                    try:
                        x_value, y_value = clip_line(xmin, xmax, ymin, ymax, x1_, y1_, x2_, y2_)
                        self._static_ax_2.plot(x_value, y_value, linewidth=2, color='g')
                        print(x_value, y_value)
                        continue
                    except OverflowError:
                        print("not in area")
                        continue
                    except RuntimeError:
                        print("Unknown Error")
                        continue
                self._static_ax_2.grid(True)
                self.static_canvas_2.draw()
            except ValueError:
                return

        elif self.radioButton_2.isChecked():
            # Sutherland-Hodgman Algorithm implementation
            self._static_ax_2.clear()
            try:
                xmin, xmax, ymin, ymax = [int(self.lineEdit_4.text()), int(self.lineEdit_5.text()),
                                          int(self.lineEdit_6.text()), int(self.lineEdit_7.text())]
                coords = (xmin, xmax, ymin, ymax)
                clipper = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
                polygon = [(random.randint(min(coords) - 50, max(coords) + 50),
                            random.randint(min(coords) - 50, max(coords) + 50)) for _ in range(3)]
                try:
                    polygon_clipped = clip(polygon, clipper)
                    polygon_clipped.append(polygon_clipped[0])
                    clipper.append(clipper[0])
                    polygon.append(polygon[0])
                    drawLine_with_color(self._static_ax_2, polygon, 'b')
                    drawLine_with_color(self._static_ax_2, polygon_clipped, 'g')
                    drawLine_with_color(self._static_ax_2, clipper, 'r')
                except IndexError:
                    clipper.append(clipper[0])
                    polygon.append(polygon[0])
                    drawLine_with_color(self._static_ax_2, polygon, 'g')
                    drawLine_with_color(self._static_ax_2, clipper, 'b')

                self._static_ax_2.grid(True)
                self.static_canvas_2.draw()
            except ValueError:
                return


if __name__ == '__main__':
    app_2 = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.setStyleSheet('oxygen')
    mywin.show()
    sys.exit(app_2.exec_())
