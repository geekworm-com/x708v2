#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.OUT)
GPIO.setwarnings(False)

def my_callback(channel):
    if GPIO.input(6):     # if port 6 == 1
        print ("---AC Power Loss OR Power Adapter Failure---")
        print ("Shutdown in 5 seconds")
        time.sleep(5)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(13, GPIO.LOW)

#time.sleep(2)

    else:                  # if port 6 != 1
        print ("---AC Power OK,Power Adapter OK---")

GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
input("Testing Started")
