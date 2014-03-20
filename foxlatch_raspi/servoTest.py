import time
import sys
import RPi.GPIO as GPIO
  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) 
servo = GPIO.PWM(12, 200) #freq (Hz)

while True:
    servo.start(14)
    time.sleep(1.2)
    
    servo.ChangeDutyCycle(48)
    time.sleep(1.2)

#200Hz @ 5v:
#1 top / full left = 48% 
#2 top = 30%
#3 top = 14%
#full right = 9%

servo.stop()
GPIO.cleanup()
