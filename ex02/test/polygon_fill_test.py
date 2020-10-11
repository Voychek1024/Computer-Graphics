import matplotlib.pyplot as plt
import numpy as np

m1, b1 = 0.1, 2.0  # slope & intercept (line 1)
m2, b2 = 2.0, -3.0  # slope & intercept (line 2)

x = np.linspace(-10, 10, 500)

plt.plot(x, x * m1 + b1, 'k')
plt.plot(x, x * m2 + b2, 'k')

plt.xlim(-2, 8)
plt.ylim(-2, 8)

plt.title('How to find the intersection of two straight lines ?', fontsize=8)

xi = (b1 - b2) / (m2 - m1)
yi = m1 * xi + b1

print('(xi,yi)', xi, yi)

plt.axvline(x=xi, color='gray', linestyle='--')
plt.axhline(y=yi, color='gray', linestyle='--')

plt.scatter(xi, yi, color='black')
plt.show()
# plt.savefig("two_straight_lines_intersection_point_03.png", bbox_inches='tight')
