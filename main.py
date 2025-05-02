import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# Hand detector with confidence
detector = HandDetector(detectionCon=0.8)

# Class for draggable rectangles
class DrawRec():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size
        self.color = (255, 0, 0)

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # Check if cursor is inside rectangle
        if (cx - w // 2 < cursor[0] < cx + w // 2 and
                cy - h // 2 < cursor[1] < cy + h // 2):
            self.posCenter = cursor[0], cursor[1]

# Create multiple rectangles
rectList = []
for x in range(5):
    rectList.append(DrawRec([x * 250 + 150, 150]))

# Main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror image
    hands, img = detector.findHands(img)  # Detect hands

    if hands:
        lmList = hands[0]["lmList"]  # Landmark list

        point1 = lmList[8][:2]   # Index finger tip
        point2 = lmList[12][:2]  # Middle finger tip

        distance, info, img = detector.findDistance(point1, point2, img)
        print(distance)

        cursor = lmList[8]
        if distance < 37:
            for rect in rectList:
                rect.update(cursor)

    # Create new image for overlays
    imgNew = np.zeros_like(img, np.uint8)

    # Draw rectangles
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        color = rect.color
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), color, cv2.FILLED)

    # Blend the original image and new image with rectangles
    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    # Display output
    cv2.imshow("Image", out)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
