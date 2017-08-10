#!/usr/bin/env python
from time import sleep
import pigpio
pi = pigpio.pi()

# set the mode for the pins
pi.set_mode(22, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)

# Read Pin
pi.read(22)
pi.read(23)    
 
# Write Pin
pi.write(22, 1)
pi.write(23, 1)
sleep(3)
pi.write(22, 0)
pi.write(23, 0)

pi.stop()
