#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import LED

red = LED(20)
green = LED(13)

GPIO.setwarnings(False)

# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")

reader = SimpleMFRC522()
# This loop checks for chips. If one is near it will get the UID
try:
    while True:
        # Scan for cards
        id, text = reader.read()
        
        #print(id)
        #print(text)
        
        if id == 763695804830:
            green.blink(on_time=.2, off_time=.2, n=4, background=False)
        else:
            red.blink(on_time=.2, off_time=.2, n=4, background=False)
except KeyboardInterrupt:
    GPIO.cleanup()
