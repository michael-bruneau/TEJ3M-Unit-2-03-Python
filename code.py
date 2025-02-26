"""
Created by: Michael Bruneau
Created on: Feb 2025
This module is a Raspberrypy Pico program that causes a LED to blink on for one second and off for one second
"""

# This program uses python

import board
import digitalio
import time
import busio

# varaibles
blink_delay = 1

print("hello world")

# setup
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

# loop
while True:
    # turns on LED and pauses for one second
    led.value = True
    time.sleep(blink_delay)

    # turns off LED and pauses for one second
    led.value = False
    time.sleep(blink_delay)
