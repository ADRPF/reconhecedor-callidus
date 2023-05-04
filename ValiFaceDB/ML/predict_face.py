import cv2 as cv
import os
from .faceRecognition import faceDetection
from pathlib import Path


PATH_TRAINING=Path(__file__).resolve().parent
PATH_TRAINING=os.path.join(PATH_TRAINING,"trainingData.yml")

def predict(img):
    LBPH_recognizer = cv.face.LBPHFaceRecognizer_create()
    LBPH_recognizer.read(PATH_TRAINING)

    faces_detected, gray_img = faceDetection(img)
    for face in faces_detected:
        (x, y, w, h) = face
        roi = gray_img[y:y+h, x:x+w]
        label, confidence = LBPH_recognizer.predict(gray_img)
        if confidence < 35:
            return label, confidence
        else:
            return -1, confidence
