from signal import pause
from gpiozero import Buzzer, MotionSensor
from time import sleep


# Buzzer
buzzer = Buzzer(27)  # GPIO27, pin 13.

def turn_on_buzzer():
    buzzer.on()
    sleep(1)
    buzzer.off()


# Motion sensor
sensor = MotionSensor(22)  # GPIO22, pin 15

def motion_detected():
    print("Motion")

def motion_stopped():
    print("No motion")

sensor.when_motion = motion_detected
sensor.when_no_motion = motion_stopped

pause() # keep program running