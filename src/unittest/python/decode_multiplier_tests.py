import unittest
from resistor import *


class TestDecodeToleranceTests(unittest.TestCase):

    def testDecodeMultiplierFiveBandWhenMultiplierBandIsBlack(self):
        colors = ['black', 'brown', 'red', 'black', 'brown']
        self.assertEquals((1, ''), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsBrown(self):
        colors = ['black', 'brown', 'red', 'brown', 'brown']
        self.assertEquals((10, ''), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsRed(self):
        colors = ['black', 'brown', 'red', 'red', 'brown']
        self.assertEquals((100, ''), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsOrange(self):
        colors = ['black', 'brown', 'red', 'orange', 'brown']
        self.assertEquals((1, 'K'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsYellow(self):
        colors = ['black', 'brown', 'red', 'yellow', 'brown']
        self.assertEquals((10, 'K'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsGreen(self):
        colors = ['black', 'brown', 'red', 'green', 'brown']
        self.assertEquals((100, 'K'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsBlue(self):
        colors = ['black', 'brown', 'red', 'blue', 'brown']
        self.assertEquals((1, 'M'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsViolet(self):
        colors = ['black', 'brown', 'red', 'violet', 'brown']
        self.assertEquals((10, 'M'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsGrey(self):
        colors = ['black', 'brown', 'red', 'grey', 'brown']
        self.assertEquals((100, 'M'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsWhite(self):
        colors = ['black', 'brown', 'red', 'white', 'brown']
        self.assertEquals((1, 'G'), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsGold(self):
        colors = ['black', 'brown', 'red', 'gold', 'brown']
        self.assertEquals((0.1, ''), decodeMultiplier(colors))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsSilver(self):
        colors = ['black', 'brown', 'red', 'silver', 'brown']
        self.assertEquals((.01, ''), decodeMultiplier(colors))
