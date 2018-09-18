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
