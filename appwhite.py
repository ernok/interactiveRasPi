#!/usr/bin/env python

from time import sleep
import pigpio
pi = pigpio.pi()

# set the mode for the pins
pi.set_mode(22, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)
pi.set_mode(25, pigpio.OUTPUT)
pi.set_mode(26, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)

# Read Pin
pi.read(22)
pi.read(23)
pi.read(27)
pi.read(25)
pi.read(26)
pi.read(24)

# Write Pin
pi.write(22, 1)
pi.write(23, 1)
pi.write(27, 1)
pi.write(25, 1)
pi.write(26, 1)
pi.write(24, 1)
sleep(3)
pi.write(22, 0)
pi.write(23, 0)
pi.write(27, 0)
pi.write(25, 0)
pi.write(26, 0)
pi.write(24, 0)

pi.stop()
