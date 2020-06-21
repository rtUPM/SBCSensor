#!/usr/bin/python3

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)

GPIO.output(13, GPIO.LOW)

