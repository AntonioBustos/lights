oid CylonBounce(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay, int times) {
  for (int j = 0; j < times; j++) {
    for (int i = 0; i < LED_COUNT - EyeSize - 2; i++) {
      strip.clear();
      strip.setPixelColor(i, red / 10, green / 10, blue / 10);
      for (int j = 1; j <= EyeSize; j++) {
        strip.setPixelColor(i + j, red, green, blue);
      }
      strip.setPixelColor(i + EyeSize + 1, red / 10, green / 10, blue / 10);
      strip.show();
      delay(SpeedDelay);
    }

    delay(ReturnDelay);

    for (int i = LED_COUNT - EyeSize - 2; i > 0; i--) {
      strip.clear();
      strip.setPixelColor(i, red / 10, green / 10, blue / 10);
      for (int j = 1; j <= EyeSize; j++) {
        strip.setPixelColor(i + j, red, green, blue);
      }
      strip.setPixelColor(i + EyeSize + 1, red / 10, green / 10, blue / 10);
      strip.show();
      delay(SpeedDelay);
    }

    delay(ReturnDelay);
  }
}