def drawMidPoint(x1, y1, x2, y2):
    x_points = []
    y_points = []
    step_x = 1 if x2 > x1 else -1 if x2 < x1 else 0
    step_y = 1 if y2 > y1 else -1 if y2 < y1 else 0
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = False
    if dy > dx:
        steep = True
        x1, y1 = y1, x1
        dx, dy = dy, dx
        step_x, step_y = step_y, step_x
    d = dx - 2 * dy
    x = x1
    y = y1
    x_points.append(x)
    y_points.append(y)
    for i in range(dx):
        if d < 0:
            y += step_y
            d += 2 * dx
        x += step_x
        d -= 2 * dy
        x_points.append(x)
        y_points.append(y)
    if steep:
        return y_points, x_points
    return x_points, y_points


if __name__ == '__main__':
    X1 = 1
    Y1 = 2
    X2 = 8
    Y2 = 5
    print(drawMidPoint(X1, Y1, X2, Y2))