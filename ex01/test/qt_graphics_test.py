import sys
import matplotlib
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QGridLayout, QGraphicsView, QGraphicsScene, QApplication, QMainWindow

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)

    def test(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        self.axes.plot(x, y)


class Mytest(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('My First App')
        self.setFixedSize(800, 600)

        # ===通过graphicview来显示图形
        self.graphicview = QGraphicsView()  # 第一步，创建一个QGraphicsView
        self.graphicview.setObjectName("graphicview")

        dr = Figure_Canvas()
        # 实例化一个FigureCanvas
        dr.test()  # 画图
        graphicscene = QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview
        # 控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicview.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicview.show()  # 最后，调用show方法呈现图形！Voila!!
        self.setCentralWidget(self.graphicview)
        self.graphicview.setFixedSize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_test = Mytest()

    my_test.show()
    app.exec_()
