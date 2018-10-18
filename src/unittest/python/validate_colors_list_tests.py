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

    def testValidateColorsWithFourColorsWhenFirstIsNoneType(self):
        colors = [None, 'brown', 'red', 'yellow']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsWithFourColorsWhenSecondIsNoneType(self):
        colors = ['black', None, 'red', 'yellow']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsWithFourColorsWhenThirdIsNoneType(self):
        colors = ['black', 'brown', None, 'yellow']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsWithFourColorsWhenFourthIsNoneType(self):
        colors = ['black', 'brown', 'red', None]
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsWithFourColorsWhenAllAreNoneType(self):
        colors = [None, None, None, None]
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFourColorsWhenFirstColorIsNone(self):
        colors = ['none', 'brown', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFourColorsWhenSecondColorIsNone(self):
        colors = ['black', 'none', 'red', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFourColorsWhenThirdColorIsNone(self):
        colors = ['black', 'brown', 'none', 'blue']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFourColorsWhenAllAreNone(self):
        colors = ['none', 'none', 'none', 'none']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFourColorsWhenFourthColorIsNone(self):
        colors = ['black', 'brown', 'red', 'none']
        self.assertTrue(validateColorsList(colors))

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

    def testValidateColorsListWhenBlackInFourthBandOfFourBandColorList(self):
        colors = ['black', 'brown', 'red', 'black']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenOrangeInFourthBandOfFourBandColorList(self):
        colors = ['black', 'brown', 'red', 'orange']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenYellowInFourthBandOfFourBandColorList(self):
        colors = ['black', 'brown', 'red', 'yellow']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenWhiteInFourthBandOfFourBandColorList(self):
        colors = ['black', 'brown', 'red', 'white']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWhenSilverInThirdBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'silver', 'red']))

    def testValidateColorsListWhenGoldInThirdBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'gold', 'red']))

    def testValidateColorsListWhenSilverInFourthBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'silver']))

    def testValidateColorsListWhenGoldInFourthBandInColorsList(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'gold']))

    def testValidateColorsListWhenValidFourBandResistor(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'blue']))

    def testValidateColorsListWhenValidFiveBandResistor(self):
        self.assertTrue(validateColorsList(
            ['black', 'brown', 'red', 'blue', 'brown']))

    def testSilverInFirstBandInColorsListOfFiveColors(self):
        colors = ['silver', 'brown', 'red', 'orange', 'green']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testSilverInSecondBandInColorsListOfFiveColors(self):
        colors = ['black', 'silver', 'red', 'orange', 'green']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testGoldInFirstBandInColorsListOfFiveColors(self):
        colors = ['gold', 'brown', 'red', 'orange', 'green']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testGoldInSecondBandInColorsListOfFiveColors(self):
        colors = ['black', 'gold', 'red', 'orange', 'green']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testBlackInFifthBandInColorsListOfFiveColors(self):
        colors = ['black', 'brown', 'red', 'orange', 'black']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testOrangeInFifthBandInColorsListOfFiveColors(self):
        colors = ['black', 'brown', 'red', 'orange', 'orange']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testYellowInFifthBandInColorsListOfFiveColors(self):
        colors = ['black', 'brown', 'red', 'orange', 'yellow']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testWhiteInFifthBandInColorsListOfFiveColors(self):
        colors = ['black', 'brown', 'red', 'orange', 'white']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsAndFirstIsNone(self):
        colors = ['none', 'brown', 'red', 'orange', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsAndSecondIsNone(self):
        colors = ['black', 'none', 'red', 'orange', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsAndThirdIsNone(self):
        colors = ['black', 'brown', 'none', 'orange', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsAndFourthIsNone(self):
        colors = ['black', 'brown', 'red', 'none', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsAndFifthIsNone(self):
        colors = ['black', 'brown', 'red', 'orange', 'none']
        self.assertTrue(validateColorsList(colors))

    def testValidateColorsListWithFiveColorsWhenFirstIsNoneType(self):
        colors = [None, 'brown', 'red', 'orange', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsWhenSecondIsNoneType(self):
        colors = ['black', None, 'red', 'orange', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsWhenThirdIsNoneType(self):
        colors = ['black', 'brown', None, 'orange', 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsWhenFourthIsNoneType(self):
        colors = ['black', 'brown', 'red', None, 'brown']
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsWhenFifthIsNoneType(self):
        colors = ['black', 'brown', 'red', 'orange', None]
        self.assertRaises(ValueError, validateColorsList, colors)

    def testValidateColorsListWithFiveColorsWhenAllNoneType(self):
        colors = [None, None, None, None, None]
        self.assertRaises(ValueError, validateColorsList, colors)
