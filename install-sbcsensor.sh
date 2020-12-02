#!/bin/bash

SBCServerIP=172.16.54.14
SBCSensorIP=172.16.54.15
DIR=/home/pi/

#Install packages
sudo apt-get update; sudo apt-get install -y python3-pip python-smbus i2c-tools wiringpi git

#Install pip3 modules
sudo pip3 install smbus2 RPi.bme280 RPi.GPIO

#Install and configure
cd ${DIR}; git clone https://github.com/rtUPM/SBCSensor
chmod u+x ${DIR}/SBCSensor/scripts/*



#Enable I2C Interface
sudo sed -i 's/#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/config.txt
sudo sed -i -e '$ai2c-dev' /etc/modules
sudo dtparam i2c_arm=on
sudo modprobe i2c-dev

#Change hostname and add SBCServer entry in /etc/hosts
sudo sed -i 's/raspberrypi/SBCSensor/' /etc/hosts
sudo sed -i 's/raspberrypi/SBCSensor/' /etc/hostname
sudo sed -i -e '$a'"${SBCServerIP}"'  SBCServer' /etc/hosts

#Reboot
sudo reboot
