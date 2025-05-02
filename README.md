# Virtual-Drag-Drop-using-opencv

This project demonstrates a simple application of hand tracking and gesture recognition using OpenCV and CVZone. It allows users to interact with rectangles on the screen by moving them with their fingertips. The rectangles can be dragged and repositioned based on the distance between two fingers (index and middle fingers).

Features:

Hand Tracking: Detects hands using CVZone's HandDetector module. Gesture Recognition: Recognizes the distance between the index and middle fingers to enable rectangle movement. Dynamic Interaction: Allows users to drag rectangles across the screen by pinching their fingers. Real-Time Processing: Captures video feed from a webcam and processes it in real-time.

Requirements: To run this project, you need the following: Python Libraries

1.OpenCV (cv2)
2.CVZone
3.NumPy

Steps to interact: Allow webcam access. Show your hand clearly in front of the camera. Pinch (touch index and middle fingers together) to activate the drag. Move your fingers to drag a rectangle. Press q to exit.
