from signal import pause
from time import sleep

from gpiozero import Buzzer, MotionSensor


BUZZER_PIN = 27
MOTION_SENSOR_PIN = 22


def turn_on_buzzer():
    buzzer = Buzzer(BUZZER_PIN)
    buzzer.on()
    sleep(1)
    buzzer.off()
    buzzer.close()


def motion_detected():
    print("Motion")


def motion_stopped():
    print("No motion")


def start_motion_detector():
    sensor = MotionSensor(MOTION_SENSOR_PIN)

    sensor.when_motion = motion_detected
    sensor.when_no_motion = motion_stopped

    pause()


if __name__ == "__main__":
    start_motion_detector()