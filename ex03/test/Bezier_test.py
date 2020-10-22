import random
from matplotlib import patches
from matplotlib.path import Path
import matplotlib.pyplot as plt


def de_casteljau(coordArr, i, j, _t):
    if j == 0:
        return coordArr[i]
    return de_casteljau(coordArr, i, j - 1, _t) * (1 - _t) + de_casteljau(coordArr, i + 1, j - 1, _t) * _t


coordArrX = [random.randint(0, 500) for _ in range(4)]
coordArrY = [random.randint(0, 500) for _ in range(4)]
points = list(zip(coordArrX, coordArrY))
fig, ax = plt.subplots()
ax.plot(coordArrX, coordArrY, 'x--', lw=2, color='black', ms=10)

positions = []

numSteps = 10000
for k in range(numSteps):
    t = float(k) / (numSteps - 1)
    x = float(de_casteljau(coordArrX, 0, 3, t))
    y = float(de_casteljau(coordArrY, 0, 3, t))
    positions.append((x, y))

x_value, y_value = zip(*positions)
ax.plot(x_value, y_value)
ax.grid(True)
plt.show()
