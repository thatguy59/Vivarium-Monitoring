# Raspberry Pi Vivarium Monitor

My personal project to create a remote way of monitoring the state of a vivarium that houses a Russian tortoise. I'm using this to teach myself Python and electronics so all feedback is welcome.

The goal is to use DHT22 sensors to log humidity and temperature somewhere that can be accessed remotely (currently thingspeak.com), and to display the information on a display near the vivarium (at the moment I'm using a 16x2 LCD).

## Running this yourself

I hope to provide a schematic at some point once it's stabilized, until then you'd have to reverse engineer it....so good luck!

Create a file called `api` with your ThingSpeak API key, this is `.gitignored` so that I don't publish my key.

## Future goals

With mixed levels of realism.....

* Get it off the breadboard on my desk and into the viv 
* Light sensor
* Track min/max over the last day and night
* Have buttons to change the mode of the display to show additional information
* Some way to have notifications if a sensor level goes out of a parameter

## Resources

* https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4
	* The initially code was built from this example
* http://www.instructables.com/id/Raspberry-PI-and-DHT22-temperature-and-humidity-lo/
* https://github.com/adafruit/Adafruit_Python_DHT/tree/master/examples
* https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png
* http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/
* https://pypi.python.org/pypi/CharLCD/0.5.1