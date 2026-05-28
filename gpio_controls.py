from time import sleep
from gpiozero import Buzzer


BUZZER_PIN = 27


def turn_on_buzzer():
    buzzer = Buzzer(BUZZER_PIN)
    buzzer.on()
    sleep(1)
    buzzer.off()
    buzzer.close()