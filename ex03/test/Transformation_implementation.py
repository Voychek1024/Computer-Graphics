import matplotlib.pyplot as plt
import numpy as np


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
    trans[2][2] = _t_vector[2]
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
        drawReference(ax, item, _center, 'g--')
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
        drawReference(ax, item, _center, 'g--')
        vec = np.append(np.array(item, dtype=float), [1])
        new_vec = trans @ vec
        result.append((new_vec[0], new_vec[1]))
        drawReference(ax, (new_vec[0], new_vec[1]), _center, 'r--')
    return result


if __name__ == '__main__':
    coords = [(50, 150), (50, 200), (100, 200), (100, 150), (50, 150)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.grid(True)
    drawLine(ax1, coords, 'g')
    trans_coords = translation(ax1, coords, [15, 15, 1])
    drawLine(ax1, trans_coords, 'y')
    scale_coords = scaling(ax1, coords, [0.5, 0.5], (5, 15))
    drawLine(ax1, scale_coords, 'b')
    rotate_coords = rotation(ax1, coords, 45, (0, 0))
    drawLine(ax1, rotate_coords, 'black')
    plt.show()
