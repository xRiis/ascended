import imath
from PIL import Image


class Picture:
    def __init__(self, name):
        self.name = name
        self.open = Image.open(self.name, 'r')
        self.xdim, self.ydim = self.open.size
        self.cx = (self.xdim / 2)
        self.cy = (self.ydim / 2)

    def coff(self):
        return imath.CartesianVals(self.cx, self.cy)


background = Picture("resources/image.png")
flare = Picture("resources/flare.png")

background.open
flare.open