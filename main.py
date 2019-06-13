from PIL import Image, ImageDraw
import face_recognition
import numpy as np
from numpy import array, empty_like
from matplotlib.path import Path
import dlib

predictor_points = "shape_predictor_68_face_landmarks.dat"
image = face_recognition.load_image_file("image.png")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_points)

detection = detector(image)

for k, d in enumerate(detection):
    shape = predictor(image, d)


def create_path(a, b):
    x1 = shape.part(a).x
    y1 = shape.part(a).y

    x2 = shape.part(b).x
    y2 = shape.part(b).y

    return Path([[x1, y1], [x1, y2], [x2, y2], [x2, y1]])


def find_coords(n):
    xc = shape.part(n).x
    yc = shape.part(n).y

    print(array([xc, yc]))
    return array([xc, yc])


def perp(c):
    d = empty_like(c)
    d[0] = -c[1]
    d[1] = c[0]

    return d


coords_38 = find_coords(38)
coords_39 = find_coords(39)
coords_41 = find_coords(41)
coords_42 = find_coords(42)

coords_44 = find_coords(44)
coords_45 = find_coords(45)
coords_47 = find_coords(47)
coords_48 = find_coords(48)


def seg_intersection(line1_start, line1_end, line2_start, line2_end):
    stacked = np.vstack([line1_start, line1_end, line2_start, line2_end])
    homogeneous = np.hstack((stacked, np.ones((4, 1))))
    line1 = np.cross(homogeneous[0], homogeneous[1])
    line2 = np.cross(homogeneous[2], homogeneous[3])
    a, b, c = np.cross(line1, line2)

    return (a / c, b / c)


print(seg_intersection(coords_38, coords_41, coords_42, coords_39))
print(seg_intersection(coords_44, -coords_47, -coords_48, coords_45))

pil_image = Image.fromarray(image)
