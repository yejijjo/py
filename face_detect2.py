import cv2              
import mediapipe as mp

cap = cv2.VideoCapture('video2.mp4')  #웹캠은 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetecion = mpFaceDetection.FaceDetection(0.50)

while True:
    success, img = cap.read()
    if success:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetecion.process(imgRGB)
        if results.detections:      #얼굴 찾았으면
            for id, detection in enumerate(results.detection):
                mpDraw.draw_detection(img, detection)


        cv2.imshow('Image', img)
        if cv2.waitKey(25) & 0xFF == 27:     # 이미지는 0, 동영상은 20~25 지정
            break