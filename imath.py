import numpy as np


class CartesianVals:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return CartesianVals(x, y)


def seg_intersection(line1_start, line1_end, line2_start, line2_end):
    stacked = np.vstack([line1_start, line1_end, line2_start, line2_end])
    homogeneous = np.hstack((stacked, np.ones((4, 1))))
    line1 = np.cross(homogeneous[0], homogeneous[1])
    line2 = np.cross(homogeneous[2], homogeneous[3])
    a, b, c = np.cross(line1, line2)

    return CartesianVals(a / c, b / c)


lflareloc = CartesianVals(0, 0)
rflareloc = CartesianVals(0, 0)
