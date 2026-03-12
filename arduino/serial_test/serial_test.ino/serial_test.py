# testing serial comms between arduino and pi
import serial
import time

# set/open arduino serial comms
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# wait for arduino to reset
time.sleep(2)

# send test message to arduino
# b'' means sending bytes, \n is the newline the arduino reads until
ser.write(b'hello\n')

# read arduino's response and decode it from bytes to a string
response = ser.readline().decode().strip()

print(response)