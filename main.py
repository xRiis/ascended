import imath
import iload
import face_recognition
from numpy import array
import dlib


predictor_points = "resources/shape_predictor_68_face_landmarks.dat"
image = face_recognition.load_image_file("resources/image.png")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_points)

detection = detector(image)

for k, d in enumerate(detection):
    shape = predictor(image, d)


def find_coords(n):
    xc = shape.part(n).x
    yc = shape.part(n).y

    return array([xc, yc])


coords_37 = find_coords(37)
coords_39 = find_coords(39)
coords_40 = find_coords(40)
coords_41 = find_coords(41)

coords_43 = find_coords(43)
coords_45 = find_coords(45)
coords_46 = find_coords(46)
coords_47 = find_coords(47)

foff = iload.flare.coff()

lflareavg = imath.seg_avg(coords_37, coords_40, coords_41, coords_39)
rflareavg = imath.seg_avg(coords_43, coords_46, coords_45, coords_47)

imath.lflareloc = lflareavg - foff
imath.rflareloc = rflareavg - foff

intlflarelocx = int(imath.lflareloc.x)
intlflarelocy = int(imath.lflareloc.y)
intrflarelocx = int(imath.rflareloc.x)
intrflarelocy = int(imath.rflareloc.y)

ileftflareloc = (intlflarelocx, intlflarelocy)
irightflareloc = (intrflarelocx, intrflarelocy)

iload.background.open.paste(iload.flare.open, ileftflareloc, iload.flare.open.convert('RGBA'))
iload.background.open.paste(iload.flare.open, irightflareloc, iload.flare.open.convert('RGBA'))
iload.background.open.save("resources/new_image_modified.png")