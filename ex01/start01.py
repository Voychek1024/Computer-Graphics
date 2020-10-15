import sys

import pyqtgraph as pg
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow

from ex01.ex01_ui import *


class CircleItem(pg.GraphicsObject):
    def __init__(self, center, radius):
        pg.GraphicsObject.__init__(self)
        self.center = center
        self.radius = radius
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        p.drawEllipse(self.center[0], self.center[1], self.radius * 2, self.radius * 2)
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


def ROUND(a):
    return int(a + 0.5)


def drawDDA(x1, y1, x2, y2):
    x, y = x1, y1
    length = (x2 - x1) if (x2 - x1) > (y2 - y1) else (y2 - y1)
    dot_x = []
    dot_y = []
    dx = (x2 - x1) / float(length)
    dy = (y2 - y1) / float(length)
    dot_x.append(ROUND(x))
    dot_y.append(ROUND(y))
    for i in range(length):
        x += dx
        y += dy
        dot_x.append(ROUND(x))
        dot_y.append(ROUND(y))
    return dot_x, dot_y


def drawMidPoint(x1, y1, x2, y2):
    x_points = []
    y_points = []
    step_x = 1 if x2 > x1 else -1 if x2 < x1 else 0
    step_y = 1 if y2 > y1 else -1 if y2 < y1 else 0
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = False
    if dy > dx:
        steep = True
        x1, y1 = y1, x1
        dx, dy = dy, dx
        step_x, step_y = step_y, step_x
    d = dx - 2 * dy
    x = x1
    y = y1
    x_points.append(x)
    y_points.append(y)
    for i in range(dx):
        if d < 0:
            y += step_y
            d += 2 * dx
        x += step_x
        d -= 2 * dy
        x_points.append(x)
        y_points.append(y)
    if steep:
        return y_points, x_points
    return x_points, y_points


def drawBresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2.0)
    step_y = 1 if y1 < y2 else -1
    y = y1
    x_points = []
    y_points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        x_points.append(coord[0])
        y_points.append(coord[1])
        error -= abs(dy)
        if error < 0:
            y += step_y
            error += dx
    if swapped:
        return y_points, x_points
    return x_points, y_points


def drawCircle(x0, y0, r):
    x_array = []
    y_array = []
    f = 1 - r
    ddf_x = 1
    ddf_y = -2 * r
    x = 0
    y = r
    if r > 0:
        x_array.append(x0), y_array.append(y0 + r)
        x_array.append(x0), y_array.append(y0 - r)
        x_array.append(x0 + r), y_array.append(y0)
        x_array.append(x0 - r), y_array.append(y0)
        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x
            x_array.append(x0 + x), y_array.append(y0 + y)
            x_array.append(x0 - x), y_array.append(y0 + y)
            x_array.append(x0 + x), y_array.append(y0 - y)
            x_array.append(x0 - x), y_array.append(y0 - y)
            x_array.append(x0 + y), y_array.append(y0 + x)
            x_array.append(x0 - y), y_array.append(y0 + x)
            x_array.append(x0 + y), y_array.append(y0 - x)
            x_array.append(x0 - y), y_array.append(y0 - x)
        return x_array, y_array


class MainWindow(QMainWindow, Ui_Window_1):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onlyInt = QIntValidator()
        lineEdit_list = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_6,
                         self.lineEdit_7, self.lineEdit_8]
        for line_item in lineEdit_list:
            line_item.setValidator(self.onlyInt)
        self.pushButton.clicked.connect(self.draw)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Computer Graphics EX01")
        self.setWindowIcon(QIcon("01.png"))
        self.show()

    def draw(self):
        self.graphWidget.clear()
        if self.radioButton_1.isChecked():
            # DDA Algorithm implementation
            cords = eval("({},{},{},{})".format(self.lineEdit_1.text(), self.lineEdit_2.text(),
                                                self.lineEdit_3.text(), self.lineEdit_4.text()))
            x_0, y_0, x_1, y_1 = cords
            self.graphWidget.setXRange(min(cords) - 1, max(cords) + 1)
            self.graphWidget.setYRange(min(cords) - 1, max(cords) + 1)
            x, y = drawDDA(x_0, y_0, x_1, y_1)
            self.graphWidget.setTitle("DDA Algorithm", color='b', size="24pt")
            self.graphWidget.showGrid(True, True, 100)
            self.graphWidget.plot([x_0, x_1], [y_0, y_1], pen='w')
            self.graphWidget.plot(x, y, pen=None, symbol='s', symbolPen=None, symbolSize=50, symbolBrush=(255, 64, 64,
                                                                                                          100))
            self.graphWidget.plot(x, y, pen=None, symbol='o')

        elif self.radioButton_2.isChecked():
            # Mid-Point Algorithm implementation
            cords = eval("({},{},{},{})".format(self.lineEdit_1.text(), self.lineEdit_2.text(),
                                                self.lineEdit_3.text(), self.lineEdit_4.text()))
            x_0, y_0, x_1, y_1 = cords
            self.graphWidget.setXRange(min(cords) - 1, max(cords) + 1)
            self.graphWidget.setYRange(min(cords) - 1, max(cords) + 1)
            x, y = drawBresenham(x_0, y_0, x_1, y_1)
            self.graphWidget.setTitle("Mid-Point Algorithm", color='g', size="24pt")
            self.graphWidget.showGrid(True, True, 100)
            self.graphWidget.plot([x_0, x_1], [y_0, y_1], pen='w')
            self.graphWidget.plot(x, y, pen=None, symbol='s', symbolPen=None, symbolSize=50, symbolBrush=(127, 229, 240,
                                                                                                          100))
            self.graphWidget.plot(x, y, pen=None, symbol='o')

        elif self.radioButton_3.isChecked():
            # Bresenham Algorithm implementation
            cords = eval("({},{},{},{})".format(self.lineEdit_1.text(), self.lineEdit_2.text(),
                                                self.lineEdit_3.text(), self.lineEdit_4.text()))
            x_0, y_0, x_1, y_1 = cords
            self.graphWidget.setXRange(min(cords) - 1, max(cords) + 1)
            self.graphWidget.setYRange(min(cords) - 1, max(cords) + 1)
            x, y = drawBresenham(x_0, y_0, x_1, y_1)
            self.graphWidget.setTitle("Bresenham Algorithm", color='y', size="24pt")
            self.graphWidget.showGrid(True, True, 100)
            self.graphWidget.plot([x_0, x_1], [y_0, y_1], pen='w')
            self.graphWidget.plot(x, y, pen=None, symbol='s', symbolPen=None, symbolSize=50, symbolBrush=(151, 98, 162,
                                                                                                          100))
            self.graphWidget.plot(x, y, pen=None, symbol='o')

        elif self.radioButton_4.isChecked():
            # Mid-Point Circle Algorithm implementation
            x_0, y_0, rad = eval("({},{},{})".format(self.lineEdit_6.text(), self.lineEdit_7.text(),
                                                     self.lineEdit_8.text()))
            self.graphWidget.setXRange(x_0 - rad - 1, x_0 + rad + 1)
            self.graphWidget.setYRange(y_0 - rad - 1, y_0 + rad + 1)
            x, y = drawCircle(x_0, y_0, rad)
            self.graphWidget.setTitle("Mid-Point Circle Algorithm", color='r', size="24pt")
            self.graphWidget.showGrid(True, True, 100)
            item = CircleItem((x_0 - rad, y_0 - rad), rad)
            self.graphWidget.addItem(item)
            self.graphWidget.plot(x, y, pen=None, symbol='s', symbolPen=None, symbolSize=50, symbolBrush=(0, 128, 128,
                                                                                                          100))
            self.graphWidget.plot(x, y, pen=None, symbol='o')

        else:
            return


if __name__ == '__main__':
    app_1 = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app_1.exec_())
