import unittest
from resistor import *


class CreateFormattedResistanceStringTests(unittest.TestCase):

    def testCreateFormattedResistanceStringFourBandBlackBlackBlackBrown(self):
        colors = ['black', 'black', 'black', 'brown']
        result = createFormattedResistanceString(colors)
        self.assertEquals(result, "0 ohms +/- 1.0%")
