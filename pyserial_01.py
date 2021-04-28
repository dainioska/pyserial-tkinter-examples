# ---pyserial part01
# ---https://github.com/WaveShapePlay
import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:
    # arduinoData = ser.readline()
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)