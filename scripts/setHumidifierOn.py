#!/usr/bin/python3

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)

GPIO.output(11, GPIO.LOW)

