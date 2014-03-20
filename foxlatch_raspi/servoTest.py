import time
import sys
import RPi.GPIO as GPIO

class servo_test(object):
    
    def __init__(self, pin):
        self.pin = pin
        self.commandList = [1000, 100, 1000, 100 \
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100,\
        1000, 100, 1000, 100, 1000, 100, 1000, 100]

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.microSecond = 0.000001

    def pulse(self, direction):

        GPIO.output(self.pin, GPIO.HIGH)
        
        if direction == 0: count = 0 else: count = 1
        for pulseTime in commandList:
            if count % 2 != 0:
                GPIO.output(self.pin, GPIO.HIGH)
            else:
                GPIO.output(self.pin, GPIO.LOW)

            time.sleep(pulseTime * self.microSecond)

            count += 1

            GPIO.output(self.pin, GPIO.HIGH)

x = servo_test(12)
x.pulse(0)
GPIO.cleanup()
