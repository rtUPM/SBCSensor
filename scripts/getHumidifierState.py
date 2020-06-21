#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Set up the GPIO channels - one input and one output

GPIO.setup(11, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)

#time.sleep(2)
#GPIO.output(11, GPIO.LOW)
#time.sleep(2)
#GPIO.output(13, GPIO.HIGH)

#print(GPIO.input(13))

print(GPIO.input(11))



