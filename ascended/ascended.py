import imath
import iload
import face_recognition
from numpy import array
import dlib


# Load necessary resources
# predictor_points is a collection of points that the predictor places around a face
# image is a picture read by the predictor to place those points
predictor_points = "resources/shape_predictor_68_face_landmarks.dat"
image = face_recognition.load_image_file("resources/image.png")

# Load detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_points)
detection = detector(image)

# Place points
for k, d in enumerate(detection):
    shape = predictor(image, d)

# Function to find coordinates of those points in the image using shape
def find_coords(n):
    xc = shape.part(n).x
    yc = shape.part(n).y

    return array([xc, yc])

# Assign each necessary coordinate for our project to a variable
# This is written with respect to the viewer -- the left eye in this case is the right eye of the subject
l_eye_l_corner = find_coords(37)
l_eye_upper = find_coords(38)
l_eye_r_corner = find_coords(40)
l_eye_lower = find_coords(41)

# There seems to be more accuracy using perfect symmetry between the points, rather than translating them, so the
# setup here is a little different
r_eye_l_corner = find_coords(43)
r_eye_upper = find_coords(44)
r_eye_r_corner = find_coords(46)
r_eye_lower = find_coords(47)

# Calculate image placement offset
flare_offset = iload.flare.coff()

# Compute a point near the center of each eye for the image to be placed
l_flare_avg = imath.seg_avg(l_eye_l_corner, l_eye_r_corner, l_eye_lower, l_eye_upper)
r_flare_avg = imath.seg_avg(r_eye_l_corner, r_eye_r_corner, r_eye_upper, r_eye_lower)

# Compute the position to place each image
# By default, images are placed beginning at their upper-left corner
imath.l_flare_loc = l_flare_avg - flare_offset
imath.r_flare_loc = r_flare_avg - flare_offset

# Convert the flare locations to single integers
int_l_flare_locx = int(imath.l_flare_loc.x)
int_l_flare_locy = int(imath.l_flare_loc.y)
int_r_flare_locx = int(imath.r_flare_loc.x)
int_r_flare_locy = int(imath.r_flare_loc.y)

# Convert flare locations to tuples -- we cannot use arrays for image placement
i_l_flare_loc = (int_l_flare_locx, int_l_flare_locy)
i_r_flare_loc = (int_r_flare_locx, int_r_flare_locy)

# Load the base portrait, paste the lens flares, and save the new image
iload.background.open.paste(iload.flare.open, i_l_flare_loc, iload.flare.open.convert('RGBA'))
iload.background.open.paste(iload.flare.open, i_r_flare_loc, iload.flare.open.convert('RGBA'))
iload.background.open.save("resources/new_image_modified.png")