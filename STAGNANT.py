#!/usr/bin/env python3
#Originally from D.H.Hagan https://github.com/dhhagan
#Changes made by Jared Blanchard jaredb711@gmail.com

#Importing necessary packages
import usbiss
import opc
import argparse
import sys
import os
import time
import csv
import datetime
import serial

#Initiating the OPCN2
try:
    #time.sleep(5)
    #Open an SPI connection
    spi = usbiss.USBISS("/dev/ttyACM0", 'spi', spi_mode = 2, freq = 500000)
    time.sleep(5)
    alpha = opc.OPCN2(spi)
except Exception as e:
    print ("Startup Error: {}".format(e))
    sys.exit(1)
    
#Turn on the OPC
alpha.on()

#Wait for five seconds to allow the sensor to boot up
time.sleep(5)

#change firmware to correct version   
alpha.firmware = {'major': 18, 'version': 18.2, 'minor': 2}

#Find the appropriate number to assign to the filename
files = os.listdir('/home/pi/OpticalParticleCounters/DATA/OPCData')
number=1
for i in range(0, len(files)):
    string = files[i] 
    string = string[:-4] #eliminate the .csv at the end
    index = 0
    for letter in string:
		if not letter.isalpha():
			try:
				index = index*10 + int(float(letter)) #make sure the tens and hundreds places are accounted for
			except:
				print("Error: Please close all open files in the DATA directory and try again")
				quit()
			if index >= numberOPC:
				numberOPC = index + 1

#Create a .csv file with the appropriate number in its name
file_name = '/home/pi/OpticalParticleCounters/DATA/OPCData/OPCdata%s.csv' % (number)
file_csv = open(file_name,'w')
csv = csv.writer(file_csv, delimiter=',')

i = 0
timestart = time.time()
for j in range(1,19):
	for k in range(1,11):

        #print the file number at the beginning of each histogram
		file_number = 'file number: %s' % (number)
		print (file_number)
    
		i += 1
		keys = ['time','counter']
		data = [time.time()-timestart,i]
        #Read the histogram and print to console
        #change histogram to show integer values instead of #/cc in bins
		alpha.histogram(number_concentration=False).items()
		for key, value in alpha.histogram(number_concentration = False).items():
            #separated by commas
			data.append(value)
			keys.append(key)            
			print ("i: {}\tKey: {}\tValue: {}".format(i, key, value))
		if i == 1:
			csv.writerows([keys])
		csv.writerows([data])
		time.sleep(0.5)
	alpha.toggle_fan(0)
	time.sleep(599)
	alpha.toggle_fan(1)
	time.sleep(1)
"""
Other values that can be read from the OPC-N2
n = alpha.sn() #Serial Number
print(n)
alpha.read_firmware()
"""

#close the file
file_csv.close()

#Shut down the opc
alpha.off()

