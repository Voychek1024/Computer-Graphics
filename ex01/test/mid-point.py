def midPoint(x1, y1, x2, y2):
    x_points = []
    y_points = []
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)
    swapped = False
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        swapped = True
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    d = dy - dx / 2
    x = x1
    y = y1
    x_points.append(x)
    y_points.append(y)
    while x < x2:
        x += 1
        if d < 0:
            d += dy
        else:
            d += (dy - dx)
            y += 1
        x_points.append(x)
        y_points.append(y)
    if swapped:
        return y_points, x_points
    return x_points, y_points


if __name__ == '__main__':
    X1 = 2
    Y1 = 1
    X2 = 5
    Y2 = 8
    print(midPoint(X1, Y1, X2, Y2))
