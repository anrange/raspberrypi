#!/usr/bin/python3
#import the GPIO and time package
import tm1637
import time
import RPi.GPIO as GPIO
import signal
import sys
import threading

GPIO.setmode(GPIO.BOARD)
mutex = threading.Lock()

LED = 36
BUTTON = 37
CLK = 40
DIO = 38
BRIGHTNESS = 4

#DEFINE THE LED DRIVER CLASS
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN, GPIO.PUD_UP) # make pin an input

display = tm1637.TM1637(CLK, DIO, BRIGHTNESS)

# loop through 50 times, on/off for 1 second
print ("Testing the button pressi,\nPress CTRL-C to exit")
GPIO.output(LED, False)

def button_callback(channel):
    mutex.acquire()
    GPIO.output(LED, True)
    display.displayIp(250)
    GPIO.output(LED, False)
    mutex.release()


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    GPIO.cleanup()
    sys.exit(0)


def loop():
    while (True):
        #for i in range(50):
        button_state = GPIO.input(BUTTON)
        if button_state == GPIO.HIGH:
            #display.Show([1,2,3,4])
            print ("Button is HIGH\nDisplaying 1,2,3,4")
            #GPIO.output(LED, False)
            #display.displayIp(500)
        else:
            print ("Button is LOW")
            #display.Show([2,4,5,6])
            GPIO.output(LED, True)
        time.sleep(1)

def main():
    GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_callback, bouncetime=300)
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    loop()

main()
