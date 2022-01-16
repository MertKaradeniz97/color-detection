import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.rectangle(frame,(200,200),(300,300),(255,0,0))
    x=frame[200:300,200:300]
    cv2.imshow("frame", frame)

    b,g,r = cv2.split(x)
    cv2.imshow("r", r) #kırmızı ton
    cv2.imshow("g", g) #yeşil ton
    cv2.imshow("b", b) #mavi ton

    print("----------------------------------")
    print("green",g.mean())
    print("----------------------------------")
    print("red",r.mean())
    print("----------------------------------")
    print("blue",b.mean())
    print("----------------------------------")
    if r.mean()>210:
        print("ANCA 3 DURDU!!!!")




    # if x[1][1] >150:
    #     print("yesil isik yaniyor")



    key = cv2.waitKey(1)
    if key == 27:
        break