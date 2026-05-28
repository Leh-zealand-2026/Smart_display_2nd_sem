from time import sleep, time
from gpiozero import MotionSensor


sensor = MotionSensor(22)

BRIGHTNESS_FILE = "/sys/class/backlight/10-0045/brightness"

FULL_BRIGHTNESS = "255"
DIM_BRIGHTNESS = "40"
OFF_BRIGHTNESS = "0"

DIM_AFTER = 15
OFF_AFTER = 3600


def set_brightness(value):
    with open(BRIGHTNESS_FILE, "w") as file:
        file.write(value)


last_motion_time = time()
screen_state = "on"

set_brightness(FULL_BRIGHTNESS)

while True:
    if sensor.motion_detected:
        last_motion_time = time()

        if screen_state != "on":
            set_brightness(FULL_BRIGHTNESS)
            screen_state = "on"

    seconds_without_motion = time() - last_motion_time

    if seconds_without_motion >= OFF_AFTER and screen_state != "off":
        set_brightness(OFF_BRIGHTNESS)
        screen_state = "off"

    elif seconds_without_motion >= DIM_AFTER and screen_state == "on":
        set_brightness(DIM_BRIGHTNESS)
        screen_state = "dim"

    sleep(1)