#!/usr/bin/python3
#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
LED = 36
BUTTON = 37
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN, GPIO.PUD_UP) # make pin an input
# loop through 50 times, on/off for 1 second
print ("Testing the button pressi,\nPress CTRL-C to exit")
GPIO.output(LED, False)
while (True):
#for i in range(50):
    button_state = GPIO.input(BUTTON)
    if button_state == GPIO.HIGH:
        print ("Button is HIGH")
        GPIO.output(LED, False)
    else:
        print ("Button is LOW")
        GPIO.output(LED, True)
    time.sleep(1)
GPIO.cleanup()

