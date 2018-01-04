"""
    program to read data from Novafitness SDS101
    http://aqicn.org/sensor/sds011/
    Nils Jacob Berland
    njberland@gmail.com / njberland@sensar.io
    +47 40800410
    The numbers produced are microgram pr m^3 of particles
"""
import serial
import os
import csv
import datetime
import time

# check for the existence of /dev/tty**** !!!
# drivers may be based on the CH34x USB SERIAL CHIP:
# https://tzapu.com/making-ch340-ch341-serial-adapters-work-under-el-capitan-os-x/
# http://www.microcontrols.org/arduino-uno-clone-ch340-ch341-chipset-usb-drivers/
#
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, stopbits=1, parity="N",  timeout=2)

#Find the appropriate number to assign to the filename
files = os.listdir('/home/pi/OpticalParticleCounters/DATA/NovaData')

number=1
for i in range(0, len(files)):
    string = files[i] 
    string = string[:-4] #eliminate the .csv at the end
    index = 0
    for letter in string:
        if not letter.isalpha():
            index = index*10 + int(float(letter)) #make sure the tens and hundreds places are accounted for
            if index >= number:
                number = index + 1
                
file_name = '/home/pi/OpticalParticleCounters/DATA/NovaData/NOVAdata%s.csv' % (number)
file_csv = open(file_name,'w')
csv = csv.writer(file_csv, delimiter=',')                
#
PM25 = 0 #initialize PM25 and PM10
PM10 = 0
counter = 0
timestart = time.time()
timer = 0
csv.writerows([["Counter", "Time", "PM2.5", "PM10"]]) #make sure to use two square brackets when using csv.writerows

while True:
    s = ser.read(1)        
    if ord(s) == int("AA",16):
        s = ser.read(1)
        if ord(s) == int("C0",16):
            s = ser.read(7)
            a = []
            for i in s:
                a.append(i)
            #print(a)
            pm2hb= s[0]
            pm2lb= s[1]
            pm10hb= s[2]
            pm10lb= s[3]
            cs = s[6]
            counter = counter + 1
            timer = time.time() - timestart
            PM25 = float(pm2hb + pm2lb*256)/10.0
            PM10 = float(pm10hb + pm10lb*256)/10.0
            datarow = [counter,timer,PM25,PM10]
            csv.writerows([datarow])
            # we should verify the checksum... it is the sum of bytes 1-6 truncated...

            try:
                print("PM2.5 - ", float(pm2hb + pm2lb*256)/10.0 ," PM10 - ", float(pm10hb + pm10lb*256)/10.0)
            except:
                pass
    else:
        pass
        
