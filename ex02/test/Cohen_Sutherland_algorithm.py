from typing import Union, Tuple
import matplotlib.pyplot as plt
from matplotlib import patches
import math


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
            return math.inf, math.inf, math.inf, math.inf
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


if __name__ == '__main__':
    fig, ax = plt.subplots(1)
    rect = patches.Rectangle((-0.5, 0), 1.5, 1, linewidth=2, edgecolor='r', facecolor='none', alpha=0.5)
    x1_, y1_, x2_, y2_ = (-1, -0.5, 2, 2)
    x_values = [x1_, x2_]
    y_values = [y1_, y2_]
    ax.grid(True)
    ax.plot(x_values, y_values, linewidth=2, alpha=0.7, color='b')
    ax.add_patch(rect)
    x1_, y1_, x2_, y2_ = cohen_sutherland(xmin=-0.5, xmax=1, ymin=0, ymax=1, x1=x1_, y1=y1_, x2=x2_, y2=y2_)
    # TODO: parameter connection is still go...
    #   rect(start_point, length, width)->(xmin, xmax, ymin, ymax)
    #   line(start_point, end_point)->plot(x_values, y_values)
    #   idea --- make patch movable??
    x_value = [x1_, x2_]
    y_value = [y1_, y2_]
    ax.plot(x_value, y_value, linewidth=2, color='g')
    plt.show()
