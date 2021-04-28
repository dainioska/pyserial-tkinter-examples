import serial
import time

# ser = serial.Serial('COM12', baudrate=9600, timeout=1)
ser = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(1)


def getValues():
    ser.write(b'z')
    arduData = ser.readline().decode('ascii')
    # arduData = ser.readline().decode().split('\r\n')
    return arduData

while True:
    userInput = input('Get data point?: ')
    if userInput == 'y':
        print(getValues())