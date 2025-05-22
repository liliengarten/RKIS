def check_point(x, y, radius):
    if (x >= -radius and x <= radius) and (y >= -radius and y <= radius):
        return True

    return False