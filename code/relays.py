import RPi.GPIO as GPIO 
import time
import os

channel1 = 26

GPIO.setmode(GPIO.BCM) 
GPIO.setup(channel1,GPIO.OUT)

while 1:
    time.sleep(2)
    GPIO.output(channel1, GPIO.HIGH)

    time.sleep(2)

    GPIO.output(channel1, GPIO.LOW)
