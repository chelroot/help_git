#! /usr/bin/env python
# coding: utf-8


import serial, time

ser = serial.Serial("/dev/ttyACM0")
ser.baudrate = 9600

while True :
  ser.write('A')
  time.sleep(0.5)
  aa = ser.read()
  print(aa)
  time.sleep(0.5)
  ser.write('a')
  time.sleep(0.5)
  aa = ser.read()
  print(aa)

