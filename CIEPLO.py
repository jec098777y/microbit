from microbit import *
import neopixel
np = neopixel.NeoPixel(pin16, 4)


while True:
    uga = temperature()
    for pixel_id in range(0, len(np)):
        red = 0
        green = 0
        blue = 0
        if uga < 25:
            red = 0
            green = 0
            blue = 160
        elif uga > 30:
            red = 160
            green = 0
            blue = 0
        else:
            red = 0
            green = 160
            blue = 0
        np[pixel_id] = (red,green,blue)

        np.show()
    sleep(50)
