import random
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)

x = [random.randint(1, 10) for i in range(10)]
# print(x)
_x = 0
_y = 0
data = []
for item in x:
    for i in range(item):
        # print("({},{})".format(_x, _y), end=' ')
        data.append([_x, _y])
        _x += 1
    _y += 1
    _x = 0
    # print()
# print(data)
x, y = zip(*data)

major_ticks = np.arange(-2, 12, 2)
minor_ticks = np.arange(-2, 12, 1)
ax1.set_xticks(major_ticks)
ax1.set_xticks(minor_ticks, minor=True)
ax1.set_yticks(major_ticks)
ax1.set_yticks(minor_ticks, minor=True)
ax1.grid(which='minor', alpha=0.2)
ax1.grid(which='major', alpha=0.5)
ax1.scatter(x, y, s=500, c='b', marker="D")
ax1.scatter(x, y, s=10, c='r')
plt.xlim([-2, 12])
plt.ylim([-2, 12])
plt.show()
