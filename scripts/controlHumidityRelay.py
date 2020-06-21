#!/usr/bin/python3

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)

print(str(sys.argv[1]))

if str(sys.argv[1]) == 0:
    print("PowerOFF")
    GPIO.output(11, GPIO.HIGH)

if str(sys.argv[1]) == 1:
    print("PowerON")
    GPIO.output(11, GPIO.LOW)

