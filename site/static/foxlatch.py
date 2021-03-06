"""
Fox Latch: main program

Objective: detect status of door and lock, and change status
           of the lock.

This implementation by TechnicalFox.
"""

import os
import sys
import time
import RPi.GPIO as GPIO

class foxlatch(object):
    
    """
    Called when object created, sets device pin locations,
    prepares the pins for I/O, and sets the servo pin to use PWM.
    """
    def __init__(self):
        try:
            setup = open("/home/pi/.foxlatch/setup_complete", "r")
            setup.close()
        except IOError:
            sys.exit("You have not run the foxlatch_setup.py file or something went wrong.")

        self.hall_sensor = 11
        self.servo_pin = 12
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT) 
        GPIO.setup(self.hall_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.servo = GPIO.PWM(12, 200)
        
        status = open("/home/pi/.foxlatch/status", "r")
        #True when locked
        if status.readline() == '1': self.lock_status = False
        else: self.lock_status = True
        status.close()
        
        #True when closed
        if GPIO.input(11) == 1: self.door_status = False
        else: self.door_status = True

    """
    Writes an integer to a status file.
    0 if the door is locked, 1 if not.
    """
    def update_status(self):
        status = open("/home/pi/.foxlatch/status", "w")
        if self.lock_status: status.write('0')
        else: status.write('1')
        status.close()
    
    """ Prints the status of lock and door to terminal. """
    def print_status(self):
        GPIO.cleanup()
        if self.door_status: door = "Door is closed"
        else: door = "Door is open, can't toggle lock"
        if self.lock_status: lock = " and locked."
        else: lock = "."
        sys.exit(door + lock)

    """ Locks the door if unlocked, unlocks if locked. Only when door is closed. """
    def toggle_lock(self):
        if self.door_status:
            if self.lock_status:
                #rough estimate, needs testing
                self.servo.start(14)
                time.sleep(0.5)
                self.servo.stop()
            else:
                #rough estimate, needs testing
                self.servo.start(35)
                time.sleep(0.5)
                self.servo.stop()
        else:
            GPIO.cleanup()
            sys.exit()
        
        self.lock_status = not self.lock_status
        self.update_status()
        GPIO.cleanup()
        sys.exit()

##########################
### END foxlatch class ###
##########################

"""
Main function that takes an argument either 'stat' or 'lock' to print the status
of the lock and door, or to lock/unlock the door. It only works if run as root
and closes if not. It also closes if no args are passed.
"""
if __name__ == "__main__":
    if not os.geteuid() == 0: sys.exit('foxlatch.py must be run as root.')
    foxlatch = foxlatch()
    try:
        if sys.argv[1] == 'stat': foxlatch.print_status()
        elif sys.argv[1] == 'lock': foxlatch.toggle_lock()
    except IndexError:
        GPIO.cleanup()
        sys.exit("You must specify a command ('stat' or 'lock').")
