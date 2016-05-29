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



from grovepi import *
from grove_rgb_lcd import *

dht_sensor_port = 7		# Connect the DHt sensor to port 7

while True:
	try:
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
		t = str(temp)
		h = str(hum)

		sys.stdout = open('file2', 'a+')		
		print A," ",D," ",O," ",Y,"    ",H,":",M,":",S,"\t",temp,"\t",hum	
		
		setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		setText(H + ":" + M + ":" + S + "\n" + A + " " + D + " " + O + " " + Y + " " + Z)	
		time.sleep(5)
		setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		setText("Temp    : " + t + "C" + "\n" + "Humidity: " + h + "%")	
		time.sleep(5)



	except (IOError,TypeError) as e:
		print "Error"
