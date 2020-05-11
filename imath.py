class CartesianVals:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return CartesianVals(x, y)


def seg_avg(line1_start, line1_end, line2_start, line2_end):
    line1_x_mp = (line1_start[0] + line1_end[0]) / 2
    line1_y_mp = (line1_start[1] + line1_end[1]) / 2
    line2_x_mp = (line2_start[0] + line2_end[0]) / 2
    line2_y_mp = (line2_start[1] + line2_end[1]) / 2

    x_avg = (line1_x_mp + line2_x_mp) / 2
    y_avg = (line1_y_mp + line2_y_mp) / 2

    return CartesianVals(x_avg, y_avg)


lflareloc = CartesianVals(0, 0)
rflareloc = CartesianVals(0, 0)