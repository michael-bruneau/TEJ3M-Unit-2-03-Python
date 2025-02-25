"""
Created by: Michael Bruneau
Created on: Feb 2025
This module is a Raspberrypy Pico program that causes a LED to blink on for one second and off for one second
"""

# This program uses python

import board
import digitalio
import time

# varaibles
blink_delay

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# loop
while True:
    # turns on LED and pauses for one second
    led.value = True
    time.sleep(blink_delay)

    # turns off LED and pauses for one second
    led.value = False
    time.sleep(blink_delay)
