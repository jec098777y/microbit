from microbit import *
import neopixel
np = neopixel.NeoPixel(pin14, 19)
kture_swiatlo = 0
lecimy_w_prawo = True
lecimy_w_lewo = False
zero = 0
trzy = 3

while True:
    for i in range(15):
        red = 0
        green = 0
        blue = 160
        np.clear()
        np[kture_swiatlo] = (red, green, blue)

        np.show()
        sleep(25)

        kture_swiatlo += 1
    kture_swiatlo = 14
    for i in range(15):
        red = 160
        green = 0
        blue = 0
        np.clear()
        np[kture_swiatlo] = (red, green, blue)

        np.show()
        sleep(25)
        kture_swiatlo -= 1
    kture_swiatlo = 0










