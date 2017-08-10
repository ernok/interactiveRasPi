import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

GPIO.output(18,1)
GPIO.output(35,1)
GPIO.output(36,1)

time.sleep(3)
GPIO.cleanup()

