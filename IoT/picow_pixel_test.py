import time
from neopixel import Neopixel


# setting
numpix = 15
GPIO = 28
strip = Neopixel(numpix, 0, GPIO, "GRB")
strip.brightness(50)


# lighting up
yellow = (255, 100, 0)
black = (0, 0, 0)
i = 0
while True:
    i = i % numpix
    strip.set_pixel(i, yellow)
    strip.show()
    time.sleep(0.1)
    strip.set_pixel(i, black)
    strip.show()
    i += 1