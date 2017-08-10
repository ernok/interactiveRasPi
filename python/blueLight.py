import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)

GPIO.output(13,1)
GPIO.output(33,1)
GPIO.output(32,1)

time.sleep(3)
GPIO.cleanup()
