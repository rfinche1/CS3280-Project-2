import unittest
from resistor import *


class TestDecodeToleranceTests(unittest.TestCase):

    def testDecodeMultiplierWhenMultiplierBandIsBlack(self):
        colors = ['black', 'brown', 'red', 'black', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, ''))

    def testDecodeMultiplierWhenMultiplerBandIsBrown(self):
        colors = ['black', 'brown', 'red', 'brown', 'brown']
        self.assertEquals(decodeMultiplier(colors), (10, ''))

    def testDecodeMultiplierWhenMultiplerBandIsRed(self):
        colors = ['black', 'brown', 'red', 'red', 'brown']
        self.assertEquals(decodeMultiplier(colors), (100, ''))

    def testDecodeMultiplierWhenMultiplerBandIsOrange(self):
        colors = ['black', 'brown', 'red', 'orange', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, 'K'))

    def testDecodeMultiplierWhenMultiplerBandIsYellow(self):
        colors = ['black', 'brown', 'red', 'yellow', 'brown']
        self.assertEquals(decodeMultiplier(colors), (10, 'K'))

    def testDecodeMultiplierWhenMultiplerBandIsGreen(self):
        colors = ['black', 'brown', 'red', 'green', 'brown']
        self.assertEquals(decodeMultiplier(colors), (100, 'K'))

    def testDecodeMultiplierWhenMultiplerBandIsBlue(self):
        colors = ['black', 'brown', 'red', 'blue', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, 'M'))

    def testDecodeMultiplierWhenMultiplerBandIsViolet(self):
        colors = ['black', 'brown', 'red', 'violet', 'brown']
        self.assertEquals(decodeMultiplier(colors), (10, 'M'))

    def testDecodeMultiplierWhenMultiplerBandIsGrey(self):
        colors = ['black', 'brown', 'red', 'grey', 'brown']
        self.assertEquals(decodeMultiplier(colors), (100, 'M'))

    def testDecodeMultiplierWhenMultiplerBandIsWhite(self):
        colors = ['black', 'brown', 'red', 'white', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, 'G'))

    def testDecodeMultiplierWhenMultiplerBandIsGold(self):
        colors = ['black', 'brown', 'red', 'gold', 'brown']
        self.assertEquals(decodeMultiplier(colors), (0.1, ''))

    def testDecodeMultiplierWhenMultiplerBandIsSilver(self):
        colors = ['black', 'brown', 'red', 'silver', 'brown']
        self.assertEquals(decodeMultiplier(colors), (.01, ''))
