import time

from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.my_complexion
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25, count=1):
        """
        Blinks the smiley's eyes

         :param delay: Delay between blinks (in seconds)
         :param count: Number of blinks the face does
        """
        i = 0
        while i < count:
            self.draw_eyes(wide_open=False)
            self.show()
            time.sleep(delay)
            self.draw_eyes(wide_open=True)
            self.show()
            time.sleep(delay)
            i += 1