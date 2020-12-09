#!/usr/bin/python3

import smbus2
import bme280
import RPi.GPIO as GPIO
import time

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

heater = GPIO.input(13)
humidifier = GPIO.input(11)

if heater == 1:
    heater = 0
else:
    heater =1

if humidifier == 1:
    humidifier = 0
else:
    humidifier =1

print("%.1f %.1f %d %d" % (data.temperature,data.humidity,heater,humidifier))
