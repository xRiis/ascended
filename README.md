<img alt="Logo" src="https://i.imgur.com/GGWKjaS.png">

---

## ascended.py makes memes using facial recognition

This is done using three libraries: [numpy](https://github.com/numpy/numpy), [dlib](https://github.com/davisking/dlib), and [face-recognition](https://github.com/ageitgey/face_recognition). Numpy plays a minor role in array math, while dlib and face-recognition do the heavy lifting, working together to identify 68 major points on a face in a given image. This is achieved with a .dat file used as a base, contained in ascended\resources.

The script should work on any image containing a clear face. It calculates the center of both eyes in a portrait, and pastes two images at both places. The result is an "ascended" meme - lens flares edited onto the eyes of a subject as a joke - as seen in the logo.