#!/usr/bin/python3

import socket
import RPi.GPIO as GPIO

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex(('172.16.54.134', 22))

if result == 0:
   print ("SBCServer is UP")
else:
   print ("SBCServer is DOWN")
   # use P1 header pin numbering convention
   GPIO.setmode(GPIO.BOARD)
   GPIO.setwarnings(False)
    
   GPIO.setup(11, GPIO.OUT)
   GPIO.setup(13, GPIO.OUT)

   GPIO.output(11, GPIO.HIGH)
   GPIO.output(13, GPIO.HIGH)

