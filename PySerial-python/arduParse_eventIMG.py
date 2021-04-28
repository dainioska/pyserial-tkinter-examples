# example show IMAGE mouse click_event sent like intParse to ardu
# test LaserTag 2021-04-08
import numpy as np
import cv2
import serial
import time

arduino = serial.Serial('COM12', baudrate=9600)
time.sleep(2)


def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        xx = x
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 1)
        cv2.imshow('image', img)

        data = ("X{0:.0f}Y{1:.0f}Z".format(x, y))
        arduino.write(data.encode())
        print("output = '" + data + "'")
        # time.sleep(0.2)


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
