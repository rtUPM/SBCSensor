#!/bin/bash

#Install packages
sudo apt-get update; sudo apt-get install -y python3-pip python-smbus i2c-tools wiringpi git

#Install pip3 modules
sudo pip3 install smbus2 RPi.bme280 RPi.GPIO

#Install SBCSensor
cd /home/pi/; git clone https://github.com/rtUPM/SBCSensor
chmod u+x /home/pi/SBCSensor/scripts/*

#Enable I2C Interface
sudo sed -i 's/#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/config.txt
sudo sed -i -e '$ai2c-dev' /etc/modules
sudo dtparam i2c_arm=on
sudo modprobe i2c-dev

#Reboot
sudo reboot
