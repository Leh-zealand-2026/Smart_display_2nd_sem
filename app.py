from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(27)  # GPIO27, pin 13.

buzzer.on()
sleep(3)
buzzer.off()