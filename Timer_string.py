import os    
import time    
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
    