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
