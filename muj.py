

from microbit import *
import neopixel
np = neopixel.NeoPixel(pin16, 4)
zielona = 0
zwiekszamy = True
while True:
    for pixel_id in range(0, len(np)):
        red = 0
        green = zielona
        blue = 0
        np[pixel_id] = (red, green, blue)
        if zwiekszamy == True:
            zielona += 1
        else:
            zielona -=  1
        if zielona == 0:
            zwiekszamy = True
        elif zielona == 180:
            zwiekszamy = False
        np.show()
    sleep(50)