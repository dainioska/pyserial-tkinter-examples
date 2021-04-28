"""
Arduino board( UNO/nano) communication to PC(Win10/Ubuntu) over pyserial example.
Init to Arduino boards arduinoFreeCom.ino before.
Read Arduino analog port data and send over pyserial.
Print data list.
"""
import serial
import time

# ser = serial.Serial('COM12', baudrate=9600, timeout=1)
ser = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(2)
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


while True:

    userInput = input('Get data point?: ')

    if userInput == 'y':
        for i in range(0, numPoints):
            data =getValues()
            dataList[i] = data
        print(dataList)
