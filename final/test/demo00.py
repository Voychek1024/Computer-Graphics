import random

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools


def casteljau_curve(points, t):
    """Use casteljau to compute a point of a Bezier curve given the control
       points and a fixed parametized t"""
    p, n = points, len(points)
    for r in range(1, n):
        for i in range(n - r):
            p[i] = (1 - t) * p[i] + t * p[i + 1]

    return p[0]


def casteljau_surface(points, u, v):
    """Given control points of a surface and fixing u and v, compute an
       interpolated 3d point of the surface"""
    xis = list()
    yis = list()
    zis = list()

    for ps in points:
        xis.append(casteljau_curve([j[0] for j in ps], u))
        yis.append(casteljau_curve([j[1] for j in ps], u))
        zis.append(casteljau_curve([j[2] for j in ps], u))

    return (casteljau_curve(xis, v), casteljau_curve(yis, v),
            casteljau_curve(zis, v))


def control_points(_nPts=2):
    """Generate control points for a spehere. Note that we use a naive
       algorithm for clarity"""
    _xMin, _xMax, _yMin, _yMax = -1.0, 1.0, -1.0, 1.0
    _xStep = (_xMax - _xMin) / (_nPts - 1)
    _yStep = (_yMax - _yMin) / (_nPts - 1)
    _control = [[[_yMin + y * _yStep, _xMin + x * _xStep, random.random() ** 2] for x in range(_nPts)] for y in range(_nPts)]
    _patch = [[[] for x in range(_nPts)] for y in range(_nPts)]
    return _control


if __name__ == "__main__":

    # Fetch control points for the two semi-speheres
    cp_up = control_points()
    xas = list()
    yas = list()
    zas = list()
    intervals_u_v = 3
    for u in np.linspace(0.0, 1.0, intervals_u_v):
        for v in np.linspace(0.0, 1.0, intervals_u_v):
            p = casteljau_surface(cp_up, u, v)
            xas.append(p[0])
            yas.append(p[1])
            zas.append(p[2])
    print(len(xas))
    # Draw the two aproximated surfaces
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    print()
    for i in range(0, len(xas)):
        if (i + 1) % intervals_u_v == 0:
            continue
        try:
            ax.plot([xas[i], xas[i + 1]], [yas[i], yas[i + 1]], [zas[i], zas[i + 1]], c='b')
        except IndexError:
            continue

    for j in range(0, len(xas)):
        for k in range(j, intervals_u_v * (intervals_u_v), intervals_u_v):
            try:
                ax.plot([xas[k], xas[k + intervals_u_v]], [yas[k], yas[k + intervals_u_v]],
                        [zas[k], zas[k + intervals_u_v]], c='b')
            except IndexError:
                continue

    # Draw control points
    cxs = list()
    cys = list()
    czs = list()

    for fila in itertools.chain(cp_up):
        for p in fila:
            cxs.append(p[0])
            cys.append(p[1])
            czs.append(p[2])

    ax.scatter(cxs, cys, czs, c='red')

    plt.show()
