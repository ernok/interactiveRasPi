import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

GPIO.output(15,1)
GPIO.output(16,1)
GPIO.output(37,1)
GPIO.output(18,1)
GPIO.output(40,1)
GPIO.output(29,1)
GPIO.output(35,1)
GPIO.output(36,1)

time.sleep(3)
GPIO.cleanup()

