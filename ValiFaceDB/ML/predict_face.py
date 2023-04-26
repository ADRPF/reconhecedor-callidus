import cv2 as cv
from faceRecognition import faceDetection

def predict(img):
    LBPH_recognizer = cv.face.LBPHFaceRecognizer_create()
    LBPH_recognizer.read("trainingData.yml")

    faces_detected, gray_img = faceDetection(img)
    for face in faces_detected:
        (x, y, w, h) = face
        roi = gray_img[y:y+h, x:x+w]
        label, confidence = LBPH_recognizer.predict()
        if confidence < 35:
            return label, confidence
        else:
            return -1, confidence
