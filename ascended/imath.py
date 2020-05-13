# It's easy (and fun) to do math with custom objects as opposed to arrays and tuples, so each necessary point will
# be assigned to a Cartesian coordinate that fits somewhere on the pixel array
class CartesianVals:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # At some point, we subtract two Cartesian coordinates against each other
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return CartesianVals(x, y)


# Calculate the average between the midpoints of two lines
# Basically a centroid, but without doing a bunch of weird linear algebra stuff with numpy
def seg_avg(line1_start, line1_end, line2_start, line2_end):

    # Calculate midpoints in each dimension for each line
    line1_x_mp = (line1_start[0] + line1_end[0]) / 2
    line1_y_mp = (line1_start[1] + line1_end[1]) / 2
    line2_x_mp = (line2_start[0] + line2_end[0]) / 2
    line2_y_mp = (line2_start[1] + line2_end[1]) / 2

    # Calculate the average between each midpoint
    x_avg = (line1_x_mp + line2_x_mp) / 2
    y_avg = (line1_y_mp + line2_y_mp) / 2

    return CartesianVals(x_avg, y_avg)


# Load two empty Cartesian coordinates for now, to be used in main.py
l_flare_loc = CartesianVals(0, 0)
r_flare_loc = CartesianVals(0, 0)