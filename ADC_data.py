import RPi.GPIO as GPIO
import spidev
import time
import os
import sys  
from datetime import datetime

spi = spidev.SpiDev()
spi.open(0,0)

# initialise variables
count = 1
frequ = 0.5
play = True
start_time = time.time()
dataArray = [0,0,0]
i = 0

def GetData(channel):
    spi.max_speed_hz = 1350000
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3)<<8)+adc[2]
    return data

#get voltage reading form the ADC
def ConvertVolts(data,places):
    volts = (data*3.3)/float(1023)
    volts = round(volts,places)
    return volts

def PotVolts(data,places):
    v = ConvertVolts(data,places)
    return v

#get voltage reading form the ADC
def ConvertTemp(data,places):
    volt = ConvertVolts(data,places)
    Temp = (volt-0.5)/0.01
    Temp = round(Temp,places)
    return Temp

#get voltage reading form the ADC
def LightPercent(data,places):
    V = ConvertVolts(data,places)
    Percent = (V/3)*100
    return Percent