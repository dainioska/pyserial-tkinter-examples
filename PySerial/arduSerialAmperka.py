import serial
import time

ser = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(1)


while(1):


    userInput = input('pyserial send data?: ')
    if(userInput=='y'):
        data = ser.write(b'123')
    else:
        data = ser.write(b'321')
        print("data sent: ")