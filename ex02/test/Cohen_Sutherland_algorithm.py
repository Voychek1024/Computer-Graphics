import random
from typing import Union, Tuple
import matplotlib.pyplot as plt
from matplotlib import patches
import math


def drawLine_with_color(ax, coordinates: list, _color: str):
    for i in range(len(coordinates) - 1):
        if coordinates[i] != coordinates[i + 1]:
            x_values = [coordinates[i][0], coordinates[i + 1][0]]
            y_values = [coordinates[i][1], coordinates[i + 1][1]]
            ax.plot(x_values, y_values, color=_color)


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


if __name__ == '__main__':
    fig, ax = plt.subplots(1)
    xmin, xmax, ymin, ymax = (100, 300, 100, 300)
    coords = (xmin, xmax, ymin, ymax)
    clipper = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    clipper.append(clipper[0])
    drawLine_with_color(ax, clipper, 'r')
    for i in range(10):
        print("draw{}".format(i))
        x1_, y1_, x2_, y2_ = (random.randint(min(coords) - 50, max(coords) + 50) for j in range(4))
        x_values = [x1_, x2_]
        y_values = [y1_, y2_]
        ax.plot(x_values, y_values, linewidth=2, alpha=0.7, color='b')
        try:
            x_value, y_value = clip_line(xmin, xmax, ymin, ymax, x1_, y1_, x2_, y2_)
            ax.plot(x_value, y_value, linewidth=2, color='g')
            print(x_value, y_value)
            continue
        except OverflowError:
            print("not in area")
            continue
        except RuntimeError:
            print("Unknown Error")
            continue
    ax.grid(True)
    plt.show()
