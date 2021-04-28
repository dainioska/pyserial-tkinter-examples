import serial
import time

ser = serial.Serial('COM12', baudrate=9600, timeout=1)
time.sleep(1)
numPoints = 5
dataList = [0]*numPoints

def getValues():
    ser.write(b'z')
    arduinoData = ser.readline().decode().split('\r\n')

    print(type(arduinoData))
    print('arduinoData[0]:' + arduinoData[0])
    print(type(arduinoData[0]))
    print(' ')
    print('arduinoData[1]:' + arduinoData[1])
    print(type(arduinoData[1]))
    print('*')
    return arduinoData[0]


while (1):

    userInput = input('Get data point?: ')

    if userInput == 'y':
        for i in range(0, numPoints):
            data =getValues()
            dataList[i] = data
        print(dataList)
