import serial
import time

ser = serial.Serial('COM12', baudrate=9600, timeout=1)
time.sleep(1)
numPoints = 5
dataList = [0]*numPoints

def getValues():
    ser.write(b'z')
    arduinoData = ser.readline().decode().split('\r\n')
    return arduinoData[0]


while True:

    userInput = input('Get data point?: ')

    if userInput == 'y':
        for i in range(0, numPoints):
            data = getValues()
            dataList[i] = data
        print(dataList)
