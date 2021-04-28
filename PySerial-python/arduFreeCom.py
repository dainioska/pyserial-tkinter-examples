import serial

# ser = serial.Serial('COM12', baudrate=9600, timeout=1)
ser = serial.Serial("/dev/ttyUSB0", 9600)
while 1:
    #arduData = ser.readline()
    # arduData = ser.readline()
    arduData = ser.readline().decode('ascii')
    # arduData = ser.readline().decode('utf-8')
    print(arduData)
