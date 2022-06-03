
from microbit import *
import radio


radoi = 0

czy_drugafaza = False
radio.config(group=23)
radio.on()
while True:
    if button_a.is_pressed():
        radio.send("przud")
        sleep(500)
    elif button_b.is_pressed():
        radio.send("tyl")
        sleep(500)
