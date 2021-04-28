# example show Pyserial TEST String sent to ardu (while)
# test LaserTag 2021-04-08
import serial
import time

arduino = serial.Serial('COM12', baudrate=9600)
time.sleep(3)

xx = 10  # -- x pos min
yy = 10  # -- y pos min

while True:
    # data = "X{0:d}Y{1:d}".format(xx, yy)
    # arduino.write(b'data')
    xx += 20  # -- x pos step
    yy += 20  # -- y pos step

    data = ("X{0:.0f}Y{1:.0f}Z".format(xx, yy))
    arduino.write(data.encode())
    print("output = '" + data + "'")
    time.sleep(0.5)

    if xx > 600:  # -- x pos max
       xx = 10

    if yy > 600:  # -- y pos max
        yy = 10
