import unittest
from resistor import *


class TestDecodeToleranceTests(unittest.TestCase):

    def testDecodeMultiplierFiveBandWhenMultiplierBandIsBlack(self):
        colors = ['black', 'brown', 'red', 'black', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, ''))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsBrown(self):
        colors = ['black', 'brown', 'red', 'brown', 'brown']
        self.assertEquals(decodeMultiplier(colors), (10, ''))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsRed(self):
        colors = ['black', 'brown', 'red', 'red', 'brown']
        self.assertEquals(decodeMultiplier(colors), (100, ''))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsOrange(self):
        colors = ['black', 'brown', 'red', 'orange', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, 'K'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsYellow(self):
        colors = ['black', 'brown', 'red', 'yellow', 'brown']
        self.assertEquals(decodeMultiplier(colors), (10, 'K'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsGreen(self):
        colors = ['black', 'brown', 'red', 'green', 'brown']
        self.assertEquals(decodeMultiplier(colors), (100, 'K'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsBlue(self):
        colors = ['black', 'brown', 'red', 'blue', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, 'M'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsViolet(self):
        colors = ['black', 'brown', 'red', 'violet', 'brown']
        self.assertEquals(decodeMultiplier(colors), (10, 'M'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsGrey(self):
        colors = ['black', 'brown', 'red', 'grey', 'brown']
        self.assertEquals(decodeMultiplier(colors), (100, 'M'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsWhite(self):
        colors = ['black', 'brown', 'red', 'white', 'brown']
        self.assertEquals(decodeMultiplier(colors), (1, 'G'))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsGold(self):
        colors = ['black', 'brown', 'red', 'gold', 'brown']
        self.assertEquals(decodeMultiplier(colors), (0.1, ''))

    def testDecodeMultiplierFiveBandWhenMultiplerBandIsSilver(self):
        colors = ['black', 'brown', 'red', 'silver', 'brown']
        self.assertEquals(decodeMultiplier(colors), (.01, ''))
