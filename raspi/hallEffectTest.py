import time
import sys 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    try:
        #GPIO.wait_for_edge(12, GPIO.BOTH)
        print(GPIO.input(12))
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
