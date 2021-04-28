"""
test LED "on/off" from Pycharm terminal window over Pyserial
LED_default.ino from arduino
"""
import serial
import time

# arduino = serial.Serial('COM3', baudrate=9600, timeout=1)
arduino = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(2)

print(arduino.readline())
print("Enter 1 -- Enter 0")

while 1:

     var = input()
     print("You entered:", var)

     if(var == '1'):
         print(arduino.write(b'1'))
         print("LED turend ON")
         #time.sleep(1)

     if(var == '0'):
         print(arduino.write(b'0'))
         print("LED turned OFF")
         # time.sleep(1)
