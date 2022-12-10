import random

def meteor_drop(strip, red, green, blue, wait, times):

    rainSize = 15
    stripSize = 120
    dropSize = 12
    strips = int(stripSize / rainSize)

    strip.clear()
    for i in range(0, times):
        for j in range(0, rainSize + rainSize):
            if j < rainSize:
                for k in range(0, strips):
                    strip.setPixelColor((k * rainSize) + j, strip.Color(red, green, blue))
            if j >= dropSize:
                for k in range(0, strips):
                    strip.setPixelColor(((k * rainSize) + j) - dropSize, strip.Color(0, 0, 0))
            strip.show()
            strip.delay(wait)
  
def meteor_drop_reverse(strip, red, green, blue, wait, times):
    rainSize = 15
    stripSize = 120
    dropSize = 12
    strips = int(stripSize / rainSize)

    strip.clear()
    for i in range(0, times):
        for j in range(0, rainSize + rainSize):
            if j < rainSize:
                for k in range(0, strips):
                    strip.setPixelColor((k * rainSize) + (rainSize - j - 1), strip.Color(red, green, blue))
            if j >= dropSize:
                for k in range(0, strips):
                    strip.setPixelColor(((k * rainSize) + (rainSize - j - 1)) + dropSize, strip.Color(0, 0, 0))
            strip.show()
            strip.delay(wait)

def meteor_rain(strip, red, green, blue, meteor_size, meteor_decay, meteor_random_recay, delay, qty):

  rainSize = 15
  stripSize = 135
  strips = [ 0, 15, 30, 45, 60, 75, 90, 105, 120 ]
  strip.clear()

  while True:
    selectedStrips = [ 0, 0, 0 ]

    for i in range(0, qty):
        selectedStrips[i] = (strips[random.randint(0, 8)])



    for i in range (0, int(rainSize * 3)):
        for k in range(0, len(selectedStrips)):
            selectedStrip = selectedStrips[k]
            for j in range(0, rainSize):
                if (not meteor_random_recay) or (random.randint(0, 10) > 5):
                    fadeToBlack(strip, j + selectedStrip, meteor_decay)

            for j in range(0, meteor_size):
                if (i - j < rainSize) and (i - j >= 0):
                    strip.setPixelColor((i - j) + selectedStrip, strip.Color(red, green, blue))
        strip.show()
        strip.delay(delay)



def fadeToBlack(strip, ledNo, fadeValue):
#ifdef ADAFRUIT_NEOPIXEL_H
    
    oldColor = strip.getPixelColor(ledNo)
    r = oldColor[0]
    g = oldColor[1]
    b = oldColor[2]

    r = 0 if (r <= 10)  else int(r) - (r * fadeValue / 256)
    g = 0 if (g <= 10)  else int(g) - (g * fadeValue / 256)
    b = 0 if (b <= 10)  else int(b) - (b * fadeValue / 256)

    strip.setPixelColor(ledNo, strip.Color(r, g, b))

    