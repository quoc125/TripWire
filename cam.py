import cv2
frame = 10
class cam:
    def __init__(self, filename):
        self.filename = filename                    #sets the name of the picture file to send

    def takePic(self):
        camera = cv2.VideoCapture(0)
        #warm up the camera
        temp = camera.read()
        im = camera.read()
        cv2.imwrite(self.filename, im[1])
        del(camera)

