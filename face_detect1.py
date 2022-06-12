import cv2
import mediapipe as mp

cap = cv2.VideoCapture('img3.jpg')

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetecion = mpFaceDetection.FaceDetection(0.50)

success, img = cap.read()
if success:
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetecion.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detection):
            mpDraw.draw_detection(img, detection)


cv2.imshow('Image', img)
cv2.waitKey(0)