#!/usr/bin/env python

from time import sleep
import pigpio
pi = pigpio.pi()

# set the mode for the pins
pi.set_mode(26, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)
 
# Read Pin
pi.read(26)
pi.read(24)    
 
# Write Pin
pi.write(26, 1)
pi.write(24, 1) 
sleep(3)
pi.write(26, 0)
pi.write(24, 0)

pi.stop()
