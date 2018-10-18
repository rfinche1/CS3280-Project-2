import unittest
from resistor import validateColorsList


class TestValidateColorsList(unittest.TestCase):

    def testValidateColorsListWhenColorsListIsNone(self):
        colors = None
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenColorsListIsEmpty(self):
        colors = []
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenColorsListContainsOneColor(self):
        colors = ['black']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenColorsListContainsTwoColors(self):
        colors = ['black', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenColorsListContainsThreeColors(self):
        colors = ['black', 'brown', 'red']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenColorsListContainsSixColors(self):
        colors = ['black', 'brown', 'red', 'blue', 'green', 'white']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testInvalidFirstBandInColorsListWithFourColors(self):
        colors = ['maroon', 'brown', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)
