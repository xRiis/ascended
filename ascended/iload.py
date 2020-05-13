import imath
from PIL import Image


# For the sake of exercise, I'm creating an object to be used by images in a separate file
class Picture:
    def __init__(self, name):
        self.name = name
        self.open = Image.open(self.name, 'r') # Open with 'r' for some masking requirement, allowing transparency
        self.xdim, self.ydim = self.open.size # Width and height of each image, assuming the image is square

        # Calculate the center for each image
        self.cx = (self.xdim / 2)
        self.cy = (self.ydim / 2)

    # Determine the offset for each image
    def coff(self):
        return imath.CartesianVals(self.cx, self.cy)


# Assign each image to a Picture
background = Picture("resources/image.png")
flare = Picture("resources/flare.png")

background.open
flare.open