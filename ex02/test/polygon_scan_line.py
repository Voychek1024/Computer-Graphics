import random
import matplotlib.pyplot as plt
import math
import numpy as np
from termcolor import cprint


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
                edge = [min(y_values), max(y_values), min(x_values), math.inf]
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
        ax.plot(x_values, y_values, color='b')

    ind = np.array(ind)
    ymax = np.array(ymax)
    for y_scan in range(min(y_), max(y_)):
        print(y_scan, end=' ')

        if y_scan in ymax:
            print("Pop Process")
            b = np.where(ymax == y_scan)
            for j in range(np.size(b)):
                print("j:{},a:{}".format(j, b[0][j]))
                try:
                    AEL.pop(b[0][j])
                except IndexError:
                    continue
            print(np.array(AEL))

        if y_scan in ind:
            print("Append Process")
            a = np.where(ind == y_scan)
            for j in range(np.size(a)):
                print("j:{},a:{}".format(j, a[0][j]))
                AEL.append(ET_[a[0][j]])
            print(np.array(AEL))

        # Do Filling
        for i in range(0, len(AEL), 2):
            try:
                print("Pair: ", AEL[i], AEL[i + 1])
                y_value = [y_scan, y_scan]
                if AEL[i][3] == math.inf or AEL[i + 1][3] == math.inf:
                    raise OverflowError
                if AEL[i][2] > AEL[i + 1][2]:
                    x_value = [math.ceil(AEL[i + 1][2]), math.floor(AEL[i][2])]
                else:
                    x_value = [math.ceil(AEL[i][2]), math.floor(AEL[i + 1][2])]
                print("plotting...", x_value, y_value)
                ax.plot(x_value, y_value, c='r')
            except IndexError:
                continue
            except OverflowError:
                # TODO: inf error,
                #  case 1: Horizontal, ind == ymax, just skip it.
                #  case 2: Vertical, ind != ymax, x_value start === xofymin, end = math.floor(AEL["indices"][3])
                y_value = [y_scan, y_scan]
                x_value = []
                print("need exception")

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


if __name__ == '__main__':
    # coords = [[random.randint(0, 100), random.randint(0, 50)] for i in range(3)]
    # coords.append(coords[0])
    coords = [[55, 41], [32, 42], [32, 23], [55, 41]]
    print(coords)
    x, y = zip(*coords)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.grid(True)
    ax1.scatter(x, y, s=10, c='r')
    ET = drawLine(ax1, coords)
    drawScanLine(ax1, coords, ET)
    plt.show()
