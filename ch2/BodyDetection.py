from djitellopy import tello
import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector(upBody=True)
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = detector.findPose(img, draw=True)
    lmList, bboxInfo = detector.findPosition(
        img, draw=True, bboxWithHands=False)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
