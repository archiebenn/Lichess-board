# serial_comms.py - for communications to the microcontroller/arduino from pi

import serial 
import time

# set serial comms 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)

# map chess file letters to LED indices 0-7
file_to_LED = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

###
# led_instruction function
###
def LED_instruction(origin, destination):
    """
    Sends LED command to Arduino over serial.
    Flashes the origin file then settles on destination file.
    origin/destination are strings like 'e2', 'e4' - we only use the file (first character)
    """

    # extract files from origin and destination and convert to indices
    origin_file = file_to_LED[origin[0]]
    destination_file = file_to_LED[destination[0]]

    # send flash command for origin, then settle command for destination
    # arduino will handle the timing of the flash
    ser.write(f"FLASH:{origin_file}\n".encode())
    time.sleep(0.5)
    ser.write(f"SETTLE:{destination_file}\n".encode())

    # this will output as LEDs eventually
    print(f"(LED): {origin} -> {destination}")