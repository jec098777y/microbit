ugabuga = 0
from microbit import *
import radio
radoi = None
radio.config(group=23)
radio.on()
import neopixel
np = neopixel.NeoPixel(pin16, 4)
while True:

    radoi = radio.receive()
    if radoi == "czerwony":
        display.show(Image.HEART)
        np.clear()
        red = 255
        green = 0
        blue = 0
        for ugabuga in range(0,4):
            np[ugabuga] = (red, green, blue)

        np.show()
    elif radoi == "zielony":
        display.show(Image.HEART)
        np.clear()
        red = 0
        green = 255
        blue = 0

        for(ugabuga) in range(0,4):
            np[ugabuga] = (red, green, blue)
        np.show()

    elif radoi == "niebieski":
        display.show(Image.HEART)

        np.clear()
        red = 0
        green = 0
        blue = 255

        for(ugabuga) in range(0,4):
            np[ugabuga] = (red, green, blue)
        np.show()












