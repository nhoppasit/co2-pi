'''
Created on Jul 3, 2018

@author: Nhoppasit-PC2
'''

#!/usr/bin/python
import sys
import time
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 5

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        time.sleep(2)
    else:
        print 'Failed to get reading. Try again!'
    