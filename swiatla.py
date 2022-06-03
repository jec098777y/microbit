from microbit import *
import neopixel
np = neopixel.NeoPixel(pin16, 4)

while True:


    sleep(2000)
    np[0] = (0, 0, 0)
    np.clear()
    red = 255
    green = 255
    blue = 0
    np[1] = (red, green, blue)
    np.show()
    sleep(2000)
    np[1] = (0, 0, 0)
    np.clear()
    red = 0
    green = 160
    blue = 0
    np[2] = (red, green, blue)
    np.show()
    sleep(2000)
    np[2] = (0, 0, 0)

    np.show()
