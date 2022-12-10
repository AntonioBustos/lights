import random

def sparkle(strip, strip_size, red, green, blue, delay):
    strip.clear()
    while (True):
        pixel = random.randint(0, strip_size)
        strip.setPixelColor(pixel, strip.Color(red, green, blue))
        strip.show()
        strip.delay(delay)
        strip.clear()


def snow_sparkle (strip, strip_size, red, green, blue, sparkle_delay, speed_delay):
  strip.fill(strip.Color(red, green, blue), 0, strip_size)
  while (True):
    pixel = random.randint(0, strip_size)
    strip.setPixelColor(pixel, strip.Color(0xff, 0xff, 0xff))
    strip.show()
    strip.delay(sparkle_delay);
    strip.setPixelColor(pixel, strip.Color(red, green, blue))
    strip.show()
    strip.delay(speed_delay)
