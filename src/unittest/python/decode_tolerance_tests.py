import unittest
from resistor import *


class TestDecodeToleranceTests(unittest.TestCase):

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsBrown(self):
        result = decodeTolerance(['black', 'brown', 'red', 'brown'])
        self.assertEquals(1.0, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsRed(self):
        result = decodeTolerance(['black', 'brown', 'red', 'red'])
        self.assertEquals(2.0, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsGreen(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green'])
        self.assertEquals(0.5, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsBlue(self):
        result = decodeTolerance(['black', 'brown', 'red', 'blue'])
        self.assertEquals(0.25, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsViolet(self):
        result = decodeTolerance(['black', 'brown', 'red', 'violet'])
        self.assertEquals(0.1, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsGold(self):
        result = decodeTolerance(['black', 'brown', 'red', 'gold'])
        self.assertEquals(5.0, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsSilver(self):
        result = decodeTolerance(['black', 'brown', 'red', 'silver'])
        self.assertEquals(10.0, result)

    def testDecodeToleranceWhenFourBandResistorAndFourthBandIsNone(self):
        result = decodeTolerance(['black', 'brown', 'red', 'none'])
        self.assertEquals(20.0, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsBrown(self):
        result = decodeTolerance(['black', 'brown', 'red', 'black', 'brown'])
        self.assertEquals(1.0, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsRed(self):
        result = decodeTolerance(['black', 'brown', 'red', 'violet', 'red'])
        self.assertEquals(2.0, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsGreen(self):
        result = decodeTolerance(['black', 'brown', 'red', 'blue', 'green'])
        self.assertEquals(0.5, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsBlue(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green', 'blue'])
        self.assertEquals(0.25, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsViolet(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green', 'violet'])
        self.assertEquals(0.1, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsGold(self):
        result = decodeTolerance(['black', 'brown', 'red', 'black', 'gold'])
        self.assertEquals(5.0, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsSilver(self):
        result = decodeTolerance(['black', 'brown', 'red', 'brown', 'silver'])
        self.assertEquals(10.0, result)

    def testDecodeToleranceWhenFiveBandResistorAndFifthBandIsNone(self):
        result = decodeTolerance(['black', 'brown', 'red', 'green', 'none'])
        self.assertEquals(20.0, result)
