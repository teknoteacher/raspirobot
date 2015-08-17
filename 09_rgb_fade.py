#! /usr/bin/env python
#
# Fade an LED (or one color of an RGB LED) using GPIO's PWM capabilities.
#
# Usage:
#   sudo python fade.py
#
# @author Jeff Geerling, 2015

import time
import RPi.GPIO as GPIO

# LED pin mapping.
red = 16 
green = 20 
blue = 21 

# Set which LED to use for fading.
led = green

# GPIO Setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Use PWM to fade an LED.
fade = GPIO.PWM(led, 100)
fade.start(0)

# Set up variables for the fading effect.
value = 0
increment = 2
increasing = True
count = 0

while count < 1000:
    fade.ChangeDutyCycle(value)

    if increasing:
        value += increment
        time.sleep(0.002)
    else:
        value -= increment
        time.sleep(0.002)

    if (value >= 100):
        increasing = False

    if (value <= 20):
        increasing = True

    time.sleep(0.05)
    count = count + 1

GPIO.cleanup()

