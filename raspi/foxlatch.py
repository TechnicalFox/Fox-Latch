"""
Fox Latch: main program

Objective: detect status of door and lock, and change status
           of the lock.

This implementation by TechnicalFox.
"""
import sys
import time
import RPi.GPIO as GPIO

class foxlatch(object):
    
    """
    Called when object created, sets device pin locations,
    prepares the pins for I/O, and sets the servo pin to use PWM.
    """
    def __init__(self):
        self.hall_sensor = 11
        self.servo_pin = 12
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT) 
        GPIO.setup(self.hall_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.servo = GPIO.PWM(12, 200)
        
        status = open("~/.foxlatch", "r")
        self.lock_status = status.readline()
        status.close()
    """
    Writes two values to a file, each boolean.
    The first is True if the door is locked, the second
    is True if the door is closed.
    """
    def write_status(self):
        status = open("~/.foxlatch", "w")
        status.write(
