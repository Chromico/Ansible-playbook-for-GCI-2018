#!/usr/bin/python
import sys
import Adafruit_DHT
import time



delay=60*1
close_time=time.time()+delay

print time.strftime('%H:%M%p %Z on %b %d, %Y')

while close_time>time.time():

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)
    
  

      