# -*- coding: utf-8 -*-

# -- Sheet --

import serial

arduinoData= serial.Serial('com4',9600)

def led_on():
    arduinoData.write('1')

def led_off():
    arduinoData.write('0')

led_on()
print('done')


