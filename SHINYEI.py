import time
import RPi.GPIO as GPIO
import pigpio

#pin2 - 5V
#pin6 - GND
#pin8 - PM2.5
#pin10 - PM1


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
print 'GPIO mode is ', GPIO.getmode()

#GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(3, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)
pi1 = pigpio.pi()
i = 1
#for i in range(1,11):
while 1:
	print 'counter', i
	i += 1 
	print 'pin 8 (PM2.5) is', GPIO.input(8)
	print 'pin 10 (PM1) is', GPIO.input(10)
	print 'pin 12 is', GPIO.input(12)
	print 'pin 8 PWM (PM2.5) is', pi1.read(8)
	print 'pin 10 PWM (PM1) is', pi1.read(10)
	print 'pin 12 PWM is', pi1.read(12)
	#print 'pin 2 is', GPIO.input(2)
	#print 'pin 6 is', GPIO.input(6)
	#print 'pin 3 is', GPIO.input(3)
	#print 'pin 4 is', GPIO.input(4)
	time.sleep(1)
GPIO.cleanup()
 
