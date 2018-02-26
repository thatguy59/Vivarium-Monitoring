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
from RPLCD import CharLCD
import traceback
import threading

myAPI = open('api').read().rstrip() 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getSensorData(pin):
    (RH, T) = Adafruit_DHT.read(Adafruit_DHT.DHT22, pin)
    return (str(RH), str(T))

def displaySensorData():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('H1:%.1f T1:%.1f' % (float(RH1), float(T1)))
    lcd.cursor_pos = (1, 0)
    lcd.write_string('H2:%.1f T2:%.1f' % (float(RH2), float(T2)))

def sensorLoop():   
    global RH1, RH2, T1, T2
    while True:
        # Get temps
        (RH1, T1) = getSensorData(17)
        (RH2, T2) = getSensorData(27)

        # Print to screen
        displaySensorData();

        # Send API message
        f = urllib2.urlopen(baseURL
                            + '&field1=%s&field2=%s&field3=%s&field4=%s'
                             % (RH1, T1, RH2, T2))
        print f.read()
        f.close()
        sleep(120)  # uploads DHT22 sensor values every 3 minutes

def buttonLoop():
    while True:
        input_state = GPIO.input(12)
        sleep(0.2)
        if input_state == False:
            print RH1, RH2, T1, T2

def main():
    try:
        print 'starting...'

        sensorThread = threading.Thread(target=sensorLoop)
        sensorThread.daemon = True
        sensorThread.start()

        buttonThread = threading.Thread(target=buttonLoop)
        buttonThread.daemon = True
        buttonThread.run()
        
        while True:
            sleep(120)
    except:
        traceback.print_exc()
        GPIO.cleanup()
        print "exiting."


# call main

if __name__ == '__main__':
    main()

			
