#!/usr/bin/env python
import serial

port = "/dev/ttyACM0"
rate = 9600

s1 = serial.Serial(port,rate)
s1.flushInput()

while True:
    if s1.inWaiting()>0:
        inputValue=s1.readline().decode("utf-8")[:-2]
        inputValue = int(inputValue)
                
        if inputValue>550:
            print("Dry", inputValue)
        if inputValue<350:
            print("wet", inputValue)
        