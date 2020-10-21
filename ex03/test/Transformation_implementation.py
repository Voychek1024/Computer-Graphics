import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


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


def translation(_coords: list, _vector: list, _reversed=False):
    result = []
    if not _reversed:
        trans = np.identity(3, dtype=float)
        trans[0][2] = _vector[0]
        trans[1][2] = _vector[1]
        trans[2][2] = _vector[2]
        for item in _coords:
            vec = np.append(np.array(item, dtype=float), [1])
            new_vec = trans @ vec
            result.append((new_vec[0], new_vec[1]))
        return result


if __name__ == '__main__':
    coords = [(50, 150), (50, 200), (100, 200), (100, 150), (50, 150)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.grid(True)
    drawLine(ax1, coords, 'g')
    trans_coords = translation(coords, [15, 15, 1])
    drawLine(ax1, trans_coords, 'y')
    plt.show()
