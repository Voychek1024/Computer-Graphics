import math


def line_Bresenham(x_0, y_0, x_1, y_1):
    dx = math.fabs(x_1 - x_0)
    dy = math.fabs(y_1 - y_0)
    p = 2 * dy - dx
    p_1 = 2 * dy
    p_2 = 2 * (dy - dx)
    x_array = []
    y_array = []
    if x_0 > x_1:
        x = x_1
        y = y_1
        x_1 = x_0
    else:
        x = x_0
        y = y_0
    x_array.append(x)
    y_array.append(y)
    while x < x_1:
        x += 1
        if p < 0:
            p += p_1
        else:
            y += 1
            p += p_2
        x_array.append(x)
        y_array.append(y)
    return x_array, y_array


if __name__ == '__main__':
    print(line_Bresenham(1, 2, 8, 5))
