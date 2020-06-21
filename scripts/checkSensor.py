#!/usr/bin/python3

import socket
import RPi.GPIO as GPIO

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex(('172.16.54.15', 22))

if result == 0:
    print("SBCSensor is UP")
else:
    print("SBCSensor is DOWN")
