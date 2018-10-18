import unittest
from resistor import *


class TestDecodeToleranceTests(unittest.TestCase):

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsBrown(self):
        result = decodeTolerance(['black', 'brown', 'red', 'brown'])
        self.assertEquals(result, 1.0)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsRed(self):
        result = decodeTolerance(['black', 'brown', 'red', 'red'])
        self.assertEquals(result, 2.0)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsGreen(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green'])
        self.assertEquals(result, 0.5)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsBlue(self):
        result = decodeTolerance(['black', 'brown', 'red', 'blue'])
        self.assertEquals(result, 0.25)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsViolet(self):
        result = decodeTolerance(['black', 'brown', 'red', 'violet'])
        self.assertEquals(result, 0.1)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsGold(self):
        result = decodeTolerance(['black', 'brown', 'red', 'gold'])
        self.assertEquals(result, 5.0)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsSilver(self):
        result = decodeTolerance(['black', 'brown', 'red', 'silver'])
        self.assertEquals(result, 10.0)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsNone(self):
        result = decodeTolerance(['black', 'brown', 'red', 'none'])
        self.assertEquals(result, 20.0)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsBrown(self):
        result = decodeTolerance(['black', 'brown', 'red', 'black', 'brown'])
        self.assertEquals(result, 1.0)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsRed(self):
        result = decodeTolerance(['black', 'brown', 'red', 'violet', 'red'])
        self.assertEquals(result, 2.0)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsGreen(self):
        result = decodeTolerance(['black', 'brown', 'red', 'blue', 'green'])
        self.assertEquals(result, 0.5)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsBlue(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green', 'blue'])
        self.assertEquals(result, 0.25)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsViolet(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green', 'violet'])
        self.assertEquals(result, 0.1)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsGold(self):
        result = decodeTolerance(['black', 'brown', 'red', 'black', 'gold'])
        self.assertEquals(result, 5.0)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsSilver(self):
        result = decodeTolerance(['black', 'brown', 'red', 'brown', 'silver'])
        self.assertEquals(result, 10.0)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsNone(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green', 'none'])
        self.assertEquals(result, 20.0)
