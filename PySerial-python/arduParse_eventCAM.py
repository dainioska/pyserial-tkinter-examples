"""
example show VIDEO-CAP mouse click_event sent like intParse to ardu
test LaserTag 2021-04-08
"""
import serial
import time
import cv2

# arduino = serial.Serial('COM12', baudrate=9600, timeout=1)
arduino = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(2)
cap = cv2.VideoCapture(0)


def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        xx = x
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 1)
        cv2.imshow('img', img)

        data = ("X{0:.0f}Y{1:.0f}Z".format(x, y))
        arduino.write(data.encode())
        print("output = '" + data + "'")
        time.sleep(0.5)


while True:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500, 500)
    cv2.line(img, (500, 250), (0, 250), (0, 255, 0), 1)
    cv2.line(img, (250, 0), (250, 500), (0, 255, 0), 1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.setMouseCallback('img', click_event)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
