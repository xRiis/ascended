from PIL import Image, ImageDraw
import face_recognition

image = face_recognition.load_image_file("image.png")

face_landmarks_list = face_recognition.face_landmarks(image)
face_landmarks_index = OrderedDict([
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48))
])

pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    d.polygon(face_landmarks['left_eye'], fill=(150, 0, 0, 256))
    d.polygon(face_landmarks['right_eye'], fill=(150, 0, 0, 256))

    pil_image.save("image_modified.png")
