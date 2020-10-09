def Bresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
    y = y1
    x_points = []
    y_points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        x_points.append(coord[0])
        y_points.append(coord[1])
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
    if swapped:
        return y_points, x_points
    return x_points, y_points


if __name__ == '__main__':
    print(Bresenham(1, 2, 8, 5))
