import sys

import math
import random
import numpy as np

from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from ex02.ex02_ui import *


class LineBuilder:
    def __init__(self, line, ax, color):
        self.line = line
        self.ax = ax
        self.color = color
        self.xs = []
        self.ys = []
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.counter = 0
        self.shape_counter = 0
        self.shape = {}
        self.precision = 10

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
        else:
            if self.counter != 0:
                self.xs.append(event.xdata)
                self.ys.append(event.ydata)
            self.ax.scatter(self.xs, self.ys, s=120, color=self.color)
            self.ax.plot(self.xs, self.ys, color=self.color)
            self.line.figure.canvas.draw()
            self.counter = self.counter + 1


def create_shape_on_image(data):
    def change_shapes(shapes):
        new_shapes = {}
        for i in range(len(shapes)):
            l = len(shapes[i][1])
            new_shapes[i] = np.zeros((l, 2), dtype='int')
            for j in range(l):
                new_shapes[i][j, 0] = shapes[i][0][j]
                new_shapes[i][j, 1] = shapes[i][1][j]
        return new_shapes
    # TODO: Unresolved reference 'plt'
    #   convert normal call to method call
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('click to include shape markers (10 pixel precision to close the shape)')
    line = ax.imshow(data)
    ax.set_xlim(0, data[:, :, 0].shape[1])
    ax.set_ylim(0, data[:, :, 0].shape[0])
    linebuilder = LineBuilder(line, ax, 'red')
    plt.gca().invert_yaxis()
    plt.show()
    new_shapes = change_shapes(linebuilder.shape)
    return new_shapes


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
            except ZeroDivisionError:
                if (y_values[1] - y_values[0]) == 0:
                    edge = [min(y_values), max(y_values), min(x_values), math.inf]
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
    # this_ran = False
    for i in range(min(y_), max(y_) + 1):
        y_values = [i, i]
        x_values = [min(x_), max(x_)]
        ax.plot(x_values, y_values, color='b', alpha=0.2)

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
                    # AEL = np.delete(np.array(AEL), b[0]).tolist()
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
                    """
                    if c.is_integer():
                        print("Integer Process:{}->".format(c), end='')
                        c -= 1
                        print(c)
                    """
                    x_value = [math.ceil(AEL[i + 1][2]), math.floor(c)]
                else:
                    c = AEL[i + 1][2]
                    """
                    if c.is_integer():
                        print("Integer Process:{}->".format(c), end='')
                        c -= 1
                        print(c)
                    """
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

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics EX02")
        self.setWindowIcon(QIcon("02.png"))
        self.show()

    def plot_1(self):
        """
        plotting template: plot following widget draw(to update)
        t = np.linspace(0, 10, 501)
        self._static_ax_1.plot(t, np.tan(t), ".-")
        self.static_canvas_1.draw()
        self._static_ax_2.plot(t, np.sin(t), "*-")
        self.static_canvas_2.draw()
        """
        self._static_ax_1.clear()
        if self.radioButton_4.isChecked():
            try:
                vertices, coord_range = [int(self.lineEdit_1.text()), int(self.lineEdit_2.text())]
            except ValueError:
                return
            coords = [[random.randint(0, coord_range), random.randint(0, coord_range)] for i in range(vertices)]
            coords.append(coords[0])
        elif self.radioButton_3.isChecked():
            pass
        ET = drawLine(self._static_ax_1, coords)
        drawScanLine(self._static_ax_1, coords, ET)
        self._static_ax_1.grid(True)
        self.static_canvas_1.draw()


if __name__ == '__main__':
    app_2 = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.setStyleSheet('oxygen')
    mywin.show()
    sys.exit(app_2.exec_())
