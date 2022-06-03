
from microbit import *
import radio


radoi = 0

czy_drugafaza = False
radio.config(group=23)
radio.on()
while True:

    if button_a.is_pressed():
        czy_drugafaza = True
    elif czy_drugafaza == True:

        if radoi == 0:
            radio.send("czerwony")
            radoi += 1
        elif radoi == 1:

            radio.send("zielony")
            radoi += 1
        elif radoi == 2:

            radio.send("niebieski")
            radoi = 0
        czy_drugafaza = False





