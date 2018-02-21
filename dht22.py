""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib2 
import RPi.GPIO as GPIO
from RPLCD import CharLCD

myAPI = open('api').read().rstrip() 
def getSensorData(pin): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)  
   return (str(RH), str(T)) 
def main(): 
   print 'starting...' 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
   lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
   while True: 
       try:
           # Get temps
           RH1, T1 = getSensorData(17)
           RH2, T2 = getSensorData(27)
           # Print to screen
           lcd.clear()
           lcd.write_string("H1:%.1f T1:%.1f" % ( float(RH1), float(T1)  ))
           lcd.cursor_pos = (1, 0)
           lcd.write_string("H2:%.1f T2:%.1f" % ( float(RH2), float(T2)  ))
           # Send API message
           f = urllib2.urlopen(baseURL + 
                               "&field1=%s&field2=%s&field3=%s&field4=%s" % (RH1, T1, RH2, T2))
           print f.read() 
           f.close() 
           sleep(120) #uploads DHT22 sensor values every 5 minutes 
       except: 
           print 'exiting.'
           lcd.clear()
           lcd.write_string("INACTIVE")
           break 
# call main 
if __name__ == '__main__': 
   main()  
