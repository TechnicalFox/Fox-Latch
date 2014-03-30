import time
import sys 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = GPIO.input(11)
if state == 0: print('Magnet detected.')
else: print('No magnet detected.')

while True:
    try:
        curState = GPIO.input(11)
        if curState != state:
            if curState == 0: print('Magnet detected.')
            else: print('No magnet detected.')
        state = curState
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
