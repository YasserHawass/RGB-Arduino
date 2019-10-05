import serial

ser = serial.Serial('COM3', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
print(ser.name)         # check which port was really used
ser.write(b'80.80.80')     # write a string
print(ser)
# ser.close()             # close port