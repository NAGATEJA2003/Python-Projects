import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.7, maxHands=2)


while(True):
    success, img = cap.read()
    hands, img = detector.findHands(img)

    # hands = detector.findHands(img, draw=False)

    if hands:
        # For First Hand
        hand1 = hands[0]
        lmlist1 = hand1['lmList']
        bbox1 = hand1['bbox']
        center1 = hand1['center']
        handtype1 = hand1['type']
        fingers1 = detector.fingersUp(hand1)
        

        if(len(hands)==2):
            hand2 = hands[1]
            lmlist2 = hand2['lmList']
            bbox2 = hand2['bbox']
            center2 = hand2['center']
            handtype2 = hand2['type']
            fingers2 = detector.fingersUp(hand2)

            length, info, img = detector.findDistance(center1, center2, img)


    cv2.imshow("Your Video", img)
    cv2.waitKey(1)