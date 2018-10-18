import unittest
from resistor import *


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

    def testValidateColorsListWithFourColorsWhenFirstColorIsNone(self):
        colors = [None, 'brown', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testInvalidFirstBandInColorsListWithFourColors(self):
        colors = ['maroon', 'brown', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testInvalidSecondBandInColorsListWithFourColors(self):
        colors = ['black', 'aqua', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testInvalidThirdBandInColorsListWithFourColors(self):
        colors = ['black', 'brown', 'taupe', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testInvalidFourthColorInColorsListWithFourColors(self):
        colors = ['black', 'brown', 'red', 'mauve']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testAllFourColorsInvalidInColorsListWithFourColors(self):
        colors = ['maroon', 'aqua', 'taupe', 'mauve']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testGoldInFirstBandInColorsListWithFourColors(self):
        colors = ['gold', 'brown', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testSilverInFirstBandInColorsListWithFourColors(self):
        colors = ['silver', 'brown', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testGoldInSecondBandInColorsListWithFourColors(self):
        colors = ['black', 'gold', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testSilverInSecondBandInColorsListWithOthersValide(self):
        colors = ['black', 'silver', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testGoldInFirstBandSilverInSecondAndLastTwoValidColors(self):
        colors = ['gold', 'silver', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testSilverInFirstBandGoldInSecondAndLastTwoValidColors(self):
        colors = ['silver', 'gold', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testSilverInThirdBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'silver', 'red']))

    def testGoldInThirdBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'gold', 'red']))

    def testSilverInFourthBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'silver']))

    def testGoldInFourthBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'gold']))

    def testValidFourBandResistor(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'blue']))

    def testValidFiveBandResistor(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'blue', 'brown']))
