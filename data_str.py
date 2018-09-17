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