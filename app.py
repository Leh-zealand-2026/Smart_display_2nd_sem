from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(27)  # GPIO27, pin 13.

# 2 Beeps and then turn off.
buzzer.on()
sleep(1)
buzzer.off()
sleep(1)
buzzer.on()
sleep(1)
buzzer.off()