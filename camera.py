import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.rectangle(frame,(200,200),(300,300),(255,0,0))

    low_red = np.array([0, 100, 100])
    high_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv_frame, low_red, high_red)
    low_green = np.array([40, 40,40])
    high_green = np.array([70, 255,255])
    mask_green = cv2.inRange(hsv_frame, low_green, high_green)
    low_blue = np.array([100,150,0])
    high_blue = np.array([140,255,255])
    mask_blue = cv2.inRange(hsv_frame, low_blue, high_blue)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red mask", mask_red)
    cv2.imshow("Green mask", mask_green)
    cv2.imshow("Blue mask", mask_blue)
    print("----------------------------------")
    print("red", mask_red.mean())
    print("----------------------------------")
    print("green", mask_green.mean())
    print("----------------------------------")
    print("blue", mask_blue.mean())

    # if x[1][1] >150:
    #     print("yesil isik yaniyor"  
    key = cv2.waitKey(1)
    if key == 27:
        break


