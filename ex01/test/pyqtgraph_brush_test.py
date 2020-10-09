from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800, 800)
view = pg.GraphicsLayoutWidget()
mw.setCentralWidget(view)
mw.setWindowTitle('pyqtgraph example: ScatterPlot')
w1 = view.addPlot()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 8, 6, 4, 2, 20, 18, 16, 14, 12]
s1 = pg.ScatterPlotItem(x, y, size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
s1.setBrush(['r'] * 10, mask=None)
w1.addItem(s1)
mw.show()
