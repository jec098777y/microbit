from microbit import *
import neopixel
np = neopixel.NeoPixel(pin16, 4)
while True:
    if display.read_light_level() > 100:
        display.show(Image.HEART)
        sleep(500)
        for pixel_id in range(0, len(np)):
            red = 255
            green = 255
            blue = 255
            np[pixel_id] = (0, 0, 0)


            np.show()

    else:




        for pixel_id in range(0, len(np)):
            red = 255
            green = 255
            blue = 255
            np[pixel_id] = (red, green, blue)


            np.show()
    sleep(50)