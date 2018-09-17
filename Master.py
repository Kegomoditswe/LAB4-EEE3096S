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

start_time = time.time()

def timer_string():
    global start_time
    now = time.time() - start_time

    # calculate h,m,s
    m,s = divmod(now,60)
    h,m = divmod(m,60)

    # timer string
    timer_str = "%02d:%02d:%02d"%(h,m,s)
    psec = str(now - int(now))
    pstr = psec[1:5]
    timer_str = timer_str + str(pstr)

    return timer_str
  
def data_print():

    #tstring = time_string()
    CH5 = 5
    CH6 = 6
    CH7 = 7
    CH5_Data = GetData(CH5)
    CH5_Temp = ConvertTemp(CH5_Data,2)
    CH6_Data = GetData(CH6)
    CH6_Light = LightPercent(CH6_Data,0)
    CH7_Data = GetData(CH7)
    CH7_Pot = PotVolts(CH7_Data,0)
    CH6_string = str(int(CH6_Light))+"%"
    sys.stdout.flush()
    
    data =("{CH7_Pot}V    {CH5_Temp}C    {CH6_string}".format(CH7_Pot=CH7_Pot,CH5_Temp=CH5_Temp,CH6_string=CH6_string))
    return data

# constructs the time string
def time_string():
    
    time_start = time.time()
    real_time = time.localtime()
    h = real_time.tm_hour
    m = real_time.tm_min
    s = real_time.tm_sec
    #current = datetime.now()
    tstring = "%02d:%02d:%02d"%(h,m,s)

    time_str = str(tstring)
    return time_str
    
# reset callback
def my_callback(push1):
    
    print("reset1")
    
    #set timer to zero
    global start_time
    start_time = time.time()
    
    #clear screne
    print("\n"*40)

#pause/play callback
def my_callback1(push2): 
    print("Stop switch pressed")
    global play
    play = not play
   
def my_callback2(push2): # frequency
    print("frequency button")
    global count
    global frequ
    print(frequ)
    count+=1
    
    if count > 3:
        count = 1

    if count ==1: # default frequency 
        frequ = 0.5

    elif count ==2: 
        frequ =1

    elif count ==3:
        frequ = 2

def my_callback3(push4): # display switch
    # check if stop swich was pressed
    global dataArray
    k = -1
    for t in range(0,5):
        global dataArray
        global i
        time_str = time_string()
        timer_str = timer_string()
        data = data_print()
        dataArray.append(data)
        dataArray.append(data)
        info = dataArray[0 + k]
        print("{time_str}     {timer_str}      {info} ".format(time_str=time_str,timer_str=timer_str , info = info))
        time.sleep(frequ)
        k -=1

def main():

    GPIO.setmode(GPIO.BCM)      #set up GPIO as BCM
    #set up SPI GPIOs
    MOSI = 10
    MISO = 9
    SCLK = 11
    CE0 = 8
    
    push1 = 2
    push2 = 3
    push3 = 4
    push4 = 21

    GPIO.setup(push1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(push2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(push3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(push4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(push1, GPIO.FALLING, callback=my_callback, bouncetime=500) 
    GPIO.add_event_detect(push2, GPIO.FALLING, callback=my_callback1, bouncetime=500)
    GPIO.add_event_detect(push3, GPIO.FALLING, callback=my_callback2, bouncetime=500)
    GPIO.add_event_detect(push4, GPIO.FALLING, callback=my_callback3, bouncetime=500)

    print("Time          Timer         Pot       Temp      Light")
    print("-------------------------------------------------------")
    
    while (True):     
        while (play):
            global dataArray
            global i
            time_str = time_string()
            timer_str = timer_string()
            data = data_print()
            dataArray.append(data)
            i += 1
            dataArray.append(data)
            info = dataArray[0 + i]
            print("{time_str}     {timer_str}      {info} ".format(time_str=time_str,timer_str=timer_str , info = info))
            time.sleep(frequ)

if __name__ == "__main__":
    main()
