#!/usr/bin/env python
# Chrisnel
# GrovePi using the Grove Temperature & Humidity Sensor (http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
# GrovePi+ & Grove Light Sensor & LED

import time
import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D3
# SIG,NC,VCC,GND
ultrasonic_ranger = 3

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND

light_sensor = 0

# grovepi_lcd_dht.py

# dht(pin,module_type), change module_type number to use other kind of dht
# module_type:
#             DHT11 0
#             DHT22 1
#             DHT21 2
#             DHT2301 3

import datetime
import random
import sys

grovepi.pinMode(light_sensor,"INPUT")

from grovepi import *
from grove_rgb_lcd import *

dht_sensor_port = 7		# Connect the DHt sensor to port 7


# Initial State settings
BUCKET_NAME = ":partly_sunny: Indoor Weather"
BUCKET_KEY = "dht012715"
ACCESS_KEY = "0eCJIIdSfLL9nZKDRbYr93deWqjBTuxI"
# Set the time between sensor reads
MINUTES_BETWEEN_READS = 1
CONVERT_TO_FAHRENHEIT = True
# ---------------------------------

sensor_value = 10

while True:
	try:
                # Get distance value
                distance = grovepi.ultrasonicRead(ultrasonic_ranger)
                
                # Get sensor value
                last_sensor_value = sensor_value
                sensor_value = grovepi.analogRead(light_sensor)
                if sensor_value == 0:
                        sensor_value = last_sensor_value # to prevent division by zero error
        
                # Calculate resistance of sensor in K
                resistance = (float)(1023 - sensor_value) * 10 / sensor_value

		[ temp,hum ] = dht(dht_sensor_port,0)		#Get the temperature and Humidity from the DHT sensor
		mydate = datetime.datetime.now()
		Z = mydate.strftime("%Z")
		A = mydate.strftime("%a")
		D = mydate.strftime("%d")
		O = mydate.strftime("%b")
		Y = mydate.strftime("%Y")

		H = '%02d' % mydate.hour
		M = '%02d' % mydate.minute
		S = '%02d' % mydate.second
		t = '%02d' % temp
		h = '%02d' % hum

		V = str(sensor_value)
		R = '%02d' % resistance

		d = str(distance)

		#sys.stdout = open('file5', 'a+')		
		#print A," ",D," ",O," ",Y,"    ",H,":",M,":",S,"\t",temp,"\t",hum, "\t",V,"\t",R		
		#setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		#setText(H + ":" + M + ":" + S + "\n" + A + " " + D + " " + O + " " + Y + " " + Z)	
		#time.sleep(5)
		setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		setText("tmp " +t + "C  " + "hum " + h + "%" + "\n" + "lig " + V + "u " + "dis " + d + "u")	
		time.sleep(1)



	except (IOError,TypeError) as e:
		print "Error"
