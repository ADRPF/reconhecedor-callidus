from faceRecognition import labels_for_training_data, train_classifier

directory =  "trainingImages"
def init_func_training(directory):
    faces, faceID = labels_for_training_data(directory)
    face_recognizer = train_classifier(faces, faceID)
    face_recognizer.save('trainingData.yml')
    return face_recognizer
