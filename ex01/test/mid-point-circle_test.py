def drawCircle(x0, y0, r):
    x_array = []
    y_array = []
    f = 1 - r
    ddf_x = 1
    ddf_y = -2 * r
    x = 0
    y = r
    if r > 0:
        x_array.append(x0), y_array.append(y0 + r)
        x_array.append(x0), y_array.append(y0 - r)
        x_array.append(x0 + r), y_array.append(y0)
        x_array.append(x0 - r), y_array.append(y0)
        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x
            x_array.append(x0 + x), y_array.append(y0 + y)
            x_array.append(x0 - x), y_array.append(y0 + y)
            x_array.append(x0 + x), y_array.append(y0 - y)
            x_array.append(x0 - x), y_array.append(y0 - y)
            x_array.append(x0 + y), y_array.append(y0 + x)
            x_array.append(x0 - y), y_array.append(y0 + x)
            x_array.append(x0 + y), y_array.append(y0 - x)
            x_array.append(x0 - y), y_array.append(y0 - x)
        return x_array, y_array


if __name__ == '__main__':
    print(drawCircle(0, 0, 5))
