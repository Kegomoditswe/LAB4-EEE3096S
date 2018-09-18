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