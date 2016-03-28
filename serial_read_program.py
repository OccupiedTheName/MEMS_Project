import serial
import time
import json
import os

ser = serial.Serial('COM6',9600,timeout =1)

def PM_monitor():

    data = ser.read(10)
    pm25_low = int(data[2].encode('hex'),16)
    pm25_high = int(data[3].encode('hex'),16)
    pm25=((pm25_high*256) + pm25_low)/10
    pm10_low = int(data[4].encode('hex'),16)
    pm10_high = int(data[5].encode('hex'),16)
    pm10=((pm10_high*256) + pm10_low)/10
    #print pm25
    #print pm10
    return json.dumps({'PM2.5': pm25, 'PM10': pm10}, sort_keys=True,indent=4, separators=(',', ': '))

    #time.sleep(2)


def write_to_file():
    fp = open("data.json","a")
    while 1:
        data = PM_monitor()
        fp.write(data)
        fp.close()
write_to_file()