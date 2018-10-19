import unittest
from resistor import *

class TestDecodeSignificantFiguresTests(unittest.TestCase):

    def testDecodeSigFigWhenFourBandsWithBlackBlack(self):
        colors = ['black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 0)

    def testDecodeSigFigWhenFourBandsWithBlackBrown(self):
        colors = ['black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 1)

    def testDecodeSigFigWhenFourBandsWithBlackRed(self):
        colors = ['black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 2)

    def testDecodeSigFigWhenFourBandsWithBlackOrange(self):
        colors = ['black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 3)

    def testDecodeSigFigWhenFourBandsWithBlackYellow(self):
        colors = ['black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 4)

    def testDecodeSigFigWhenFourBandsWithBlackGreen(self):
        colors = ['black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 5)

    def testDecodeSigFigWhenFourBandsWithBlackBlue(self):
        colors = ['black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 6)

    def testDecodeSigFigWhenFourBandsWithBlackViolet(self):
        colors = ['black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 7)

    def testDecodeSigFigWhenFourBandsWithBlackGrey(self):
        colors = ['black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 8)

    def testDecodeSigFigWhenFourBandsWithBlackWhite(self):
        colors = ['black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 9)

    def testDecodeSigFigWhenFourBandsWithBrownBlack(self):
        colors = ['brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 10)

    def testDecodeSigFigWhenFourBandsWithBrownBrown(self):
        colors = ['brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 11)

    def testDecodeSigFigWhenFourBandsWithBrownRed(self):
        colors = ['brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 12)

    def testDecodeSigFigWhenFourBandsWithBrownOrange(self):
        colors = ['brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 13)

    def testDecodeSigFigWhenFourBandsWithBrownYellow(self):
        colors = ['brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 14)

    def testDecodeSigFigWhenFourBandsWithBrownGreen(self):
        colors = ['brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 15)

    def testDecodeSigFigWhenFourBandsWithBrownBlue(self):
        colors = ['brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 16)

    def testDecodeSigFigWhenFourBandsWithBrownViolet(self):
        colors = ['brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 17)

    def testDecodeSigFigWhenFourBandsWithBrownGrey(self):
        colors = ['brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 18)

    def testDecodeSigFigWhenFourBandsWithBrownWhite(self):
        colors = ['brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 19)

    def testDecodeSigFigWhenFourBandsWithRedBlack(self):
        colors = ['red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 20)

    def testDecodeSigFigWhenFourBandsWithRedBrown(self):
        colors = ['red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 21)

    def testDecodeSigFigWhenFourBandsWithRedRed(self):
        colors = ['red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 22)

    def testDecodeSigFigWhenFourBandsWithRedOrange(self):
        colors = ['red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 23)

    def testDecodeSigFigWhenFourBandsWithRedYellow(self):
        colors = ['red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 24)

    def testDecodeSigFigWhenFourBandsWithRedGreen(self):
        colors = ['red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 25)

    def testDecodeSigFigWhenFourBandsWithRedBlue(self):
        colors = ['red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 26)

    def testDecodeSigFigWhenFourBandsWithRedViolet(self):
        colors = ['red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 27)

    def testDecodeSigFigWhenFourBandsWithRedGrey(self):
        colors = ['red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 28)

    def testDecodeSigFigWhenFourBandsWithRedWhite(self):
        colors = ['red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 29)

    def testDecodeSigFigWhenFourBandsWithOrangeBlack(self):
        colors = ['orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 30)

    def testDecodeSigFigWhenFourBandsWithOrangeBrown(self):
        colors = ['orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 31)

    def testDecodeSigFigWhenFourBandsWithOrangeRed(self):
        colors = ['orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 32)

    def testDecodeSigFigWhenFourBandsWithOrangeOrange(self):
        colors = ['orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 33)

    def testDecodeSigFigWhenFourBandsWithOrangeYellow(self):
        colors = ['orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 34)

    def testDecodeSigFigWhenFourBandsWithOrangeGreen(self):
        colors = ['orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 35)

    def testDecodeSigFigWhenFourBandsWithOrangeBlue(self):
        colors = ['orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 36)

    def testDecodeSigFigWhenFourBandsWithOrangeViolet(self):
        colors = ['orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 37)

    def testDecodeSigFigWhenFourBandsWithOrangeGrey(self):
        colors = ['orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 38)

    def testDecodeSigFigWhenFourBandsWithOrangeWhite(self):
        colors = ['orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 39)

    def testDecodeSigFigWhenFourBandsWithYellowBlack(self):
        colors = ['yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 40)

    def testDecodeSigFigWhenFourBandsWithYellowBrown(self):
        colors = ['yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 41)

    def testDecodeSigFigWhenFourBandsWithYellowRed(self):
        colors = ['yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 42)

    def testDecodeSigFigWhenFourBandsWithYellowOrange(self):
        colors = ['yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 43)

    def testDecodeSigFigWhenFourBandsWithYellowYellow(self):
        colors = ['yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 44)

    def testDecodeSigFigWhenFourBandsWithYellowGreen(self):
        colors = ['yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 45)

    def testDecodeSigFigWhenFourBandsWithYellowBlue(self):
        colors = ['yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 46)

    def testDecodeSigFigWhenFourBandsWithYellowViolet(self):
        colors = ['yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 47)

    def testDecodeSigFigWhenFourBandsWithYellowGrey(self):
        colors = ['yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 48)

    def testDecodeSigFigWhenFourBandsWithYellowWhite(self):
        colors = ['yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 49)

    def testDecodeSigFigWhenFourBandsWithGreenBlack(self):
        colors = ['green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 50)

    def testDecodeSigFigWhenFourBandsWithGreenBrown(self):
        colors = ['green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 51)

    def testDecodeSigFigWhenFourBandsWithGreenRed(self):
        colors = ['green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 52)

    def testDecodeSigFigWhenFourBandsWithGreenOrange(self):
        colors = ['green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 53)

    def testDecodeSigFigWhenFourBandsWithGreenYellow(self):
        colors = ['green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 54)

    def testDecodeSigFigWhenFourBandsWithGreenGreen(self):
        colors = ['green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 55)

    def testDecodeSigFigWhenFourBandsWithGreenBlue(self):
        colors = ['green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 56)

    def testDecodeSigFigWhenFourBandsWithGreenViolet(self):
        colors = ['green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 57)

    def testDecodeSigFigWhenFourBandsWithGreenGrey(self):
        colors = ['green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 58)

    def testDecodeSigFigWhenFourBandsWithGreenWhite(self):
        colors = ['green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 59)

    def testDecodeSigFigWhenFourBandsWithBlueBlack(self):
        colors = ['blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 60)

    def testDecodeSigFigWhenFourBandsWithBlueBrown(self):
        colors = ['blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 61)

    def testDecodeSigFigWhenFourBandsWithBlueRed(self):
        colors = ['blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 62)

    def testDecodeSigFigWhenFourBandsWithBlueOrange(self):
        colors = ['blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 63)

    def testDecodeSigFigWhenFourBandsWithBlueYellow(self):
        colors = ['blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 64)

    def testDecodeSigFigWhenFourBandsWithBlueGreen(self):
        colors = ['blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 65)

    def testDecodeSigFigWhenFourBandsWithBlueBlue(self):
        colors = ['blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 66)

    def testDecodeSigFigWhenFourBandsWithBlueViolet(self):
        colors = ['blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 67)

    def testDecodeSigFigWhenFourBandsWithBlueGrey(self):
        colors = ['blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 68)

    def testDecodeSigFigWhenFourBandsWithBlueWhite(self):
        colors = ['blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 69)

    def testDecodeSigFigWhenFourBandsWithVioletBlack(self):
        colors = ['violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 70)

    def testDecodeSigFigWhenFourBandsWithVioletBrown(self):
        colors = ['violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 71)

    def testDecodeSigFigWhenFourBandsWithVioletRed(self):
        colors = ['violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 72)

    def testDecodeSigFigWhenFourBandsWithVioletOrange(self):
        colors = ['violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 73)

    def testDecodeSigFigWhenFourBandsWithVioletYellow(self):
        colors = ['violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 74)

    def testDecodeSigFigWhenFourBandsWithVioletGreen(self):
        colors = ['violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 75)

    def testDecodeSigFigWhenFourBandsWithVioletBlue(self):
        colors = ['violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 76)

    def testDecodeSigFigWhenFourBandsWithVioletViolet(self):
        colors = ['violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 77)

    def testDecodeSigFigWhenFourBandsWithVioletGrey(self):
        colors = ['violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 78)

    def testDecodeSigFigWhenFourBandsWithVioletWhite(self):
        colors = ['violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 79)

    def testDecodeSigFigWhenFourBandsWithGreyBlack(self):
        colors = ['grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 80)

    def testDecodeSigFigWhenFourBandsWithGreyBrown(self):
        colors = ['grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 81)

    def testDecodeSigFigWhenFourBandsWithGreyRed(self):
        colors = ['grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 82)

    def testDecodeSigFigWhenFourBandsWithGreyOrange(self):
        colors = ['grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 83)

    def testDecodeSigFigWhenFourBandsWithGreyYellow(self):
        colors = ['grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 84)

    def testDecodeSigFigWhenFourBandsWithGreyGreen(self):
        colors = ['grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 85)

    def testDecodeSigFigWhenFourBandsWithGreyBlue(self):
        colors = ['grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 86)

    def testDecodeSigFigWhenFourBandsWithGreyViolet(self):
        colors = ['grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 87)

    def testDecodeSigFigWhenFourBandsWithGreyGrey(self):
        colors = ['grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 88)

    def testDecodeSigFigWhenFourBandsWithGreyWhite(self):
        colors = ['grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 89)

    def testDecodeSigFigWhenFourBandsWithWhiteBlack(self):
        colors = ['white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 90)

    def testDecodeSigFigWhenFourBandsWithWhiteBrown(self):
        colors = ['white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 91)

    def testDecodeSigFigWhenFourBandsWithWhiteRed(self):
        colors = ['white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 92)

    def testDecodeSigFigWhenFourBandsWithWhiteOrange(self):
        colors = ['white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 93)

    def testDecodeSigFigWhenFourBandsWithWhiteYellow(self):
        colors = ['white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 94)

    def testDecodeSigFigWhenFourBandsWithWhiteGreen(self):
        colors = ['white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 95)

    def testDecodeSigFigWhenFourBandsWithWhiteBlue(self):
        colors = ['white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 96)

    def testDecodeSigFigWhenFourBandsWithWhiteViolet(self):
        colors = ['white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 97)

    def testDecodeSigFigWhenFourBandsWithWhiteGrey(self):
        colors = ['white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 98)

    def testDecodeSigFigWhenFourBandsWithWhiteWhite(self):
        colors = ['white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 99)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackBlack(self):
        colors = ['black', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 0)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackBrown(self):
        colors = ['black', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 1)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackRed(self):
        colors = ['black', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 2)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackOrange(self):
        colors = ['black', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 3)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackYellow(self):
        colors = ['black', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 4)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackGreen(self):
        colors = ['black', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 5)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackBlue(self):
        colors = ['black', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 6)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackViolet(self):
        colors = ['black', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 7)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackGrey(self):
        colors = ['black', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 8)

    def testDecodeSigFigWhenFiveBandsWithBlackBlackWhite(self):
        colors = ['black', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 9)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownBlack(self):
        colors = ['black', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 10)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownBrown(self):
        colors = ['black', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 11)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownRed(self):
        colors = ['black', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 12)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownOrange(self):
        colors = ['black', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 13)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownYellow(self):
        colors = ['black', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 14)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownGreen(self):
        colors = ['black', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 15)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownBlue(self):
        colors = ['black', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 16)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownViolet(self):
        colors = ['black', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 17)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownGrey(self):
        colors = ['black', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 18)

    def testDecodeSigFigWhenFiveBandsWithBlackBrownWhite(self):
        colors = ['black', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 19)

    def testDecodeSigFigWhenFiveBandsWithBlackRedBlack(self):
        colors = ['black', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 20)

    def testDecodeSigFigWhenFiveBandsWithBlackRedBrown(self):
        colors = ['black', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 21)

    def testDecodeSigFigWhenFiveBandsWithBlackRedRed(self):
        colors = ['black', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 22)

    def testDecodeSigFigWhenFiveBandsWithBlackRedOrange(self):
        colors = ['black', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 23)

    def testDecodeSigFigWhenFiveBandsWithBlackRedYellow(self):
        colors = ['black', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 24)

    def testDecodeSigFigWhenFiveBandsWithBlackRedGreen(self):
        colors = ['black', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 25)

    def testDecodeSigFigWhenFiveBandsWithBlackRedBlue(self):
        colors = ['black', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 26)

    def testDecodeSigFigWhenFiveBandsWithBlackRedViolet(self):
        colors = ['black', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 27)

    def testDecodeSigFigWhenFiveBandsWithBlackRedGrey(self):
        colors = ['black', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 28)

    def testDecodeSigFigWhenFiveBandsWithBlackRedWhite(self):
        colors = ['black', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 29)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeBlack(self):
        colors = ['black', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 30)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeBrown(self):
        colors = ['black', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 31)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeRed(self):
        colors = ['black', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 32)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeOrange(self):
        colors = ['black', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 33)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeYellow(self):
        colors = ['black', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 34)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeGreen(self):
        colors = ['black', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 35)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeBlue(self):
        colors = ['black', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 36)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeViolet(self):
        colors = ['black', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 37)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeGrey(self):
        colors = ['black', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 38)

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeWhite(self):
        colors = ['black', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 39)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowBlack(self):
        colors = ['black', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 40)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowBrown(self):
        colors = ['black', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 41)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowRed(self):
        colors = ['black', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 42)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowOrange(self):
        colors = ['black', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 43)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowYellow(self):
        colors = ['black', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 44)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowGreen(self):
        colors = ['black', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 45)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowBlue(self):
        colors = ['black', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 46)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowViolet(self):
        colors = ['black', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 47)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowGrey(self):
        colors = ['black', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 48)

    def testDecodeSigFigWhenFiveBandsWithBlackYellowWhite(self):
        colors = ['black', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 49)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenBlack(self):
        colors = ['black', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 50)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenBrown(self):
        colors = ['black', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 51)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenRed(self):
        colors = ['black', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 52)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenOrange(self):
        colors = ['black', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 53)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenYellow(self):
        colors = ['black', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 54)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenGreen(self):
        colors = ['black', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 55)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenBlue(self):
        colors = ['black', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 56)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenViolet(self):
        colors = ['black', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 57)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenGrey(self):
        colors = ['black', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 58)

    def testDecodeSigFigWhenFiveBandsWithBlackGreenWhite(self):
        colors = ['black', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 59)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueBlack(self):
        colors = ['black', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 60)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueBrown(self):
        colors = ['black', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 61)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueRed(self):
        colors = ['black', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 62)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueOrange(self):
        colors = ['black', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 63)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueYellow(self):
        colors = ['black', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 64)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueGreen(self):
        colors = ['black', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 65)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueBlue(self):
        colors = ['black', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 66)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueViolet(self):
        colors = ['black', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 67)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueGrey(self):
        colors = ['black', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 68)

    def testDecodeSigFigWhenFiveBandsWithBlackBlueWhite(self):
        colors = ['black', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 69)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletBlack(self):
        colors = ['black', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 70)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletBrown(self):
        colors = ['black', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 71)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletRed(self):
        colors = ['black', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 72)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletOrange(self):
        colors = ['black', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 73)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletYellow(self):
        colors = ['black', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 74)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletGreen(self):
        colors = ['black', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 75)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletBlue(self):
        colors = ['black', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 76)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletViolet(self):
        colors = ['black', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 77)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletGrey(self):
        colors = ['black', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 78)

    def testDecodeSigFigWhenFiveBandsWithBlackVioletWhite(self):
        colors = ['black', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 79)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyBlack(self):
        colors = ['black', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 80)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyBrown(self):
        colors = ['black', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 81)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyRed(self):
        colors = ['black', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 82)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyOrange(self):
        colors = ['black', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 83)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyYellow(self):
        colors = ['black', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 84)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyGreen(self):
        colors = ['black', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 85)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyBlue(self):
        colors = ['black', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 86)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyViolet(self):
        colors = ['black', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 87)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyGrey(self):
        colors = ['black', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 88)

    def testDecodeSigFigWhenFiveBandsWithBlackGreyWhite(self):
        colors = ['black', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 89)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteBlack(self):
        colors = ['black', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 90)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteBrown(self):
        colors = ['black', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 91)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteRed(self):
        colors = ['black', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 92)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteOrange(self):
        colors = ['black', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 93)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteYellow(self):
        colors = ['black', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 94)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteGreen(self):
        colors = ['black', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 95)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteBlue(self):
        colors = ['black', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 96)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteViolet(self):
        colors = ['black', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 97)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteGrey(self):
        colors = ['black', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 98)

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteWhite(self):
        colors = ['black', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 99)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackBlack(self):
        colors = ['brown', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 100)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackBrown(self):
        colors = ['brown', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 101)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackRed(self):
        colors = ['brown', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 102)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackOrange(self):
        colors = ['brown', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 103)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackYellow(self):
        colors = ['brown', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 104)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackGreen(self):
        colors = ['brown', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 105)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackBlue(self):
        colors = ['brown', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 106)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackViolet(self):
        colors = ['brown', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 107)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackGrey(self):
        colors = ['brown', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 108)

    def testDecodeSigFigWhenFiveBandsWithBrownBlackWhite(self):
        colors = ['brown', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 109)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownBlack(self):
        colors = ['brown', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 110)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownBrown(self):
        colors = ['brown', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 111)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownRed(self):
        colors = ['brown', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 112)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownOrange(self):
        colors = ['brown', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 113)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownYellow(self):
        colors = ['brown', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 114)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownGreen(self):
        colors = ['brown', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 115)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownBlue(self):
        colors = ['brown', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 116)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownViolet(self):
        colors = ['brown', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 117)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownGrey(self):
        colors = ['brown', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 118)

    def testDecodeSigFigWhenFiveBandsWithBrownBrownWhite(self):
        colors = ['brown', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 119)

    def testDecodeSigFigWhenFiveBandsWithBrownRedBlack(self):
        colors = ['brown', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 120)

    def testDecodeSigFigWhenFiveBandsWithBrownRedBrown(self):
        colors = ['brown', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 121)

    def testDecodeSigFigWhenFiveBandsWithBrownRedRed(self):
        colors = ['brown', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 122)

    def testDecodeSigFigWhenFiveBandsWithBrownRedOrange(self):
        colors = ['brown', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 123)

    def testDecodeSigFigWhenFiveBandsWithBrownRedYellow(self):
        colors = ['brown', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 124)

    def testDecodeSigFigWhenFiveBandsWithBrownRedGreen(self):
        colors = ['brown', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 125)

    def testDecodeSigFigWhenFiveBandsWithBrownRedBlue(self):
        colors = ['brown', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 126)

    def testDecodeSigFigWhenFiveBandsWithBrownRedViolet(self):
        colors = ['brown', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 127)

    def testDecodeSigFigWhenFiveBandsWithBrownRedGrey(self):
        colors = ['brown', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 128)

    def testDecodeSigFigWhenFiveBandsWithBrownRedWhite(self):
        colors = ['brown', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 129)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeBlack(self):
        colors = ['brown', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 130)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeBrown(self):
        colors = ['brown', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 131)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeRed(self):
        colors = ['brown', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 132)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeOrange(self):
        colors = ['brown', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 133)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeYellow(self):
        colors = ['brown', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 134)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeGreen(self):
        colors = ['brown', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 135)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeBlue(self):
        colors = ['brown', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 136)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeViolet(self):
        colors = ['brown', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 137)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeGrey(self):
        colors = ['brown', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 138)

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeWhite(self):
        colors = ['brown', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 139)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowBlack(self):
        colors = ['brown', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 140)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowBrown(self):
        colors = ['brown', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 141)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowRed(self):
        colors = ['brown', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 142)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowOrange(self):
        colors = ['brown', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 143)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowYellow(self):
        colors = ['brown', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 144)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowGreen(self):
        colors = ['brown', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 145)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowBlue(self):
        colors = ['brown', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 146)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowViolet(self):
        colors = ['brown', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 147)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowGrey(self):
        colors = ['brown', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 148)

    def testDecodeSigFigWhenFiveBandsWithBrownYellowWhite(self):
        colors = ['brown', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 149)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenBlack(self):
        colors = ['brown', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 150)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenBrown(self):
        colors = ['brown', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 151)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenRed(self):
        colors = ['brown', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 152)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenOrange(self):
        colors = ['brown', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 153)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenYellow(self):
        colors = ['brown', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 154)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenGreen(self):
        colors = ['brown', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 155)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenBlue(self):
        colors = ['brown', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 156)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenViolet(self):
        colors = ['brown', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 157)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenGrey(self):
        colors = ['brown', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 158)

    def testDecodeSigFigWhenFiveBandsWithBrownGreenWhite(self):
        colors = ['brown', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 159)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueBlack(self):
        colors = ['brown', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 160)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueBrown(self):
        colors = ['brown', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 161)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueRed(self):
        colors = ['brown', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 162)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueOrange(self):
        colors = ['brown', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 163)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueYellow(self):
        colors = ['brown', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 164)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueGreen(self):
        colors = ['brown', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 165)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueBlue(self):
        colors = ['brown', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 166)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueViolet(self):
        colors = ['brown', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 167)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueGrey(self):
        colors = ['brown', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 168)

    def testDecodeSigFigWhenFiveBandsWithBrownBlueWhite(self):
        colors = ['brown', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 169)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletBlack(self):
        colors = ['brown', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 170)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletBrown(self):
        colors = ['brown', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 171)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletRed(self):
        colors = ['brown', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 172)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletOrange(self):
        colors = ['brown', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 173)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletYellow(self):
        colors = ['brown', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 174)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletGreen(self):
        colors = ['brown', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 175)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletBlue(self):
        colors = ['brown', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 176)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletViolet(self):
        colors = ['brown', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 177)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletGrey(self):
        colors = ['brown', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 178)

    def testDecodeSigFigWhenFiveBandsWithBrownVioletWhite(self):
        colors = ['brown', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 179)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyBlack(self):
        colors = ['brown', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 180)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyBrown(self):
        colors = ['brown', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 181)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyRed(self):
        colors = ['brown', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 182)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyOrange(self):
        colors = ['brown', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 183)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyYellow(self):
        colors = ['brown', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 184)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyGreen(self):
        colors = ['brown', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 185)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyBlue(self):
        colors = ['brown', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 186)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyViolet(self):
        colors = ['brown', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 187)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyGrey(self):
        colors = ['brown', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 188)

    def testDecodeSigFigWhenFiveBandsWithBrownGreyWhite(self):
        colors = ['brown', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 189)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteBlack(self):
        colors = ['brown', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 190)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteBrown(self):
        colors = ['brown', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 191)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteRed(self):
        colors = ['brown', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 192)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteOrange(self):
        colors = ['brown', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 193)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteYellow(self):
        colors = ['brown', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 194)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteGreen(self):
        colors = ['brown', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 195)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteBlue(self):
        colors = ['brown', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 196)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteViolet(self):
        colors = ['brown', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 197)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteGrey(self):
        colors = ['brown', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 198)

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteWhite(self):
        colors = ['brown', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 199)

    def testDecodeSigFigWhenFiveBandsWithRedBlackBlack(self):
        colors = ['red', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 200)

    def testDecodeSigFigWhenFiveBandsWithRedBlackBrown(self):
        colors = ['red', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 201)

    def testDecodeSigFigWhenFiveBandsWithRedBlackRed(self):
        colors = ['red', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 202)

    def testDecodeSigFigWhenFiveBandsWithRedBlackOrange(self):
        colors = ['red', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 203)

    def testDecodeSigFigWhenFiveBandsWithRedBlackYellow(self):
        colors = ['red', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 204)

    def testDecodeSigFigWhenFiveBandsWithRedBlackGreen(self):
        colors = ['red', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 205)

    def testDecodeSigFigWhenFiveBandsWithRedBlackBlue(self):
        colors = ['red', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 206)

    def testDecodeSigFigWhenFiveBandsWithRedBlackViolet(self):
        colors = ['red', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 207)

    def testDecodeSigFigWhenFiveBandsWithRedBlackGrey(self):
        colors = ['red', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 208)

    def testDecodeSigFigWhenFiveBandsWithRedBlackWhite(self):
        colors = ['red', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 209)

    def testDecodeSigFigWhenFiveBandsWithRedBrownBlack(self):
        colors = ['red', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 210)

    def testDecodeSigFigWhenFiveBandsWithRedBrownBrown(self):
        colors = ['red', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 211)

    def testDecodeSigFigWhenFiveBandsWithRedBrownRed(self):
        colors = ['red', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 212)

    def testDecodeSigFigWhenFiveBandsWithRedBrownOrange(self):
        colors = ['red', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 213)

    def testDecodeSigFigWhenFiveBandsWithRedBrownYellow(self):
        colors = ['red', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 214)

    def testDecodeSigFigWhenFiveBandsWithRedBrownGreen(self):
        colors = ['red', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 215)

    def testDecodeSigFigWhenFiveBandsWithRedBrownBlue(self):
        colors = ['red', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 216)

    def testDecodeSigFigWhenFiveBandsWithRedBrownViolet(self):
        colors = ['red', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 217)

    def testDecodeSigFigWhenFiveBandsWithRedBrownGrey(self):
        colors = ['red', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 218)

    def testDecodeSigFigWhenFiveBandsWithRedBrownWhite(self):
        colors = ['red', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 219)

    def testDecodeSigFigWhenFiveBandsWithRedRedBlack(self):
        colors = ['red', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 220)

    def testDecodeSigFigWhenFiveBandsWithRedRedBrown(self):
        colors = ['red', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 221)

    def testDecodeSigFigWhenFiveBandsWithRedRedRed(self):
        colors = ['red', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 222)

    def testDecodeSigFigWhenFiveBandsWithRedRedOrange(self):
        colors = ['red', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 223)

    def testDecodeSigFigWhenFiveBandsWithRedRedYellow(self):
        colors = ['red', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 224)

    def testDecodeSigFigWhenFiveBandsWithRedRedGreen(self):
        colors = ['red', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 225)

    def testDecodeSigFigWhenFiveBandsWithRedRedBlue(self):
        colors = ['red', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 226)

    def testDecodeSigFigWhenFiveBandsWithRedRedViolet(self):
        colors = ['red', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 227)

    def testDecodeSigFigWhenFiveBandsWithRedRedGrey(self):
        colors = ['red', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 228)

    def testDecodeSigFigWhenFiveBandsWithRedRedWhite(self):
        colors = ['red', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 229)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeBlack(self):
        colors = ['red', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 230)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeBrown(self):
        colors = ['red', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 231)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeRed(self):
        colors = ['red', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 232)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeOrange(self):
        colors = ['red', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 233)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeYellow(self):
        colors = ['red', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 234)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeGreen(self):
        colors = ['red', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 235)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeBlue(self):
        colors = ['red', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 236)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeViolet(self):
        colors = ['red', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 237)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeGrey(self):
        colors = ['red', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 238)

    def testDecodeSigFigWhenFiveBandsWithRedOrangeWhite(self):
        colors = ['red', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 239)

    def testDecodeSigFigWhenFiveBandsWithRedYellowBlack(self):
        colors = ['red', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 240)

    def testDecodeSigFigWhenFiveBandsWithRedYellowBrown(self):
        colors = ['red', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 241)

    def testDecodeSigFigWhenFiveBandsWithRedYellowRed(self):
        colors = ['red', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 242)

    def testDecodeSigFigWhenFiveBandsWithRedYellowOrange(self):
        colors = ['red', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 243)

    def testDecodeSigFigWhenFiveBandsWithRedYellowYellow(self):
        colors = ['red', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 244)

    def testDecodeSigFigWhenFiveBandsWithRedYellowGreen(self):
        colors = ['red', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 245)

    def testDecodeSigFigWhenFiveBandsWithRedYellowBlue(self):
        colors = ['red', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 246)

    def testDecodeSigFigWhenFiveBandsWithRedYellowViolet(self):
        colors = ['red', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 247)

    def testDecodeSigFigWhenFiveBandsWithRedYellowGrey(self):
        colors = ['red', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 248)

    def testDecodeSigFigWhenFiveBandsWithRedYellowWhite(self):
        colors = ['red', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 249)

    def testDecodeSigFigWhenFiveBandsWithRedGreenBlack(self):
        colors = ['red', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 250)

    def testDecodeSigFigWhenFiveBandsWithRedGreenBrown(self):
        colors = ['red', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 251)

    def testDecodeSigFigWhenFiveBandsWithRedGreenRed(self):
        colors = ['red', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 252)

    def testDecodeSigFigWhenFiveBandsWithRedGreenOrange(self):
        colors = ['red', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 253)

    def testDecodeSigFigWhenFiveBandsWithRedGreenYellow(self):
        colors = ['red', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 254)

    def testDecodeSigFigWhenFiveBandsWithRedGreenGreen(self):
        colors = ['red', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 255)

    def testDecodeSigFigWhenFiveBandsWithRedGreenBlue(self):
        colors = ['red', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 256)

    def testDecodeSigFigWhenFiveBandsWithRedGreenViolet(self):
        colors = ['red', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 257)

    def testDecodeSigFigWhenFiveBandsWithRedGreenGrey(self):
        colors = ['red', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 258)

    def testDecodeSigFigWhenFiveBandsWithRedGreenWhite(self):
        colors = ['red', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 259)

    def testDecodeSigFigWhenFiveBandsWithRedBlueBlack(self):
        colors = ['red', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 260)

    def testDecodeSigFigWhenFiveBandsWithRedBlueBrown(self):
        colors = ['red', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 261)

    def testDecodeSigFigWhenFiveBandsWithRedBlueRed(self):
        colors = ['red', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 262)

    def testDecodeSigFigWhenFiveBandsWithRedBlueOrange(self):
        colors = ['red', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 263)

    def testDecodeSigFigWhenFiveBandsWithRedBlueYellow(self):
        colors = ['red', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 264)

    def testDecodeSigFigWhenFiveBandsWithRedBlueGreen(self):
        colors = ['red', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 265)

    def testDecodeSigFigWhenFiveBandsWithRedBlueBlue(self):
        colors = ['red', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 266)

    def testDecodeSigFigWhenFiveBandsWithRedBlueViolet(self):
        colors = ['red', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 267)

    def testDecodeSigFigWhenFiveBandsWithRedBlueGrey(self):
        colors = ['red', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 268)

    def testDecodeSigFigWhenFiveBandsWithRedBlueWhite(self):
        colors = ['red', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 269)

    def testDecodeSigFigWhenFiveBandsWithRedVioletBlack(self):
        colors = ['red', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 270)

    def testDecodeSigFigWhenFiveBandsWithRedVioletBrown(self):
        colors = ['red', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 271)

    def testDecodeSigFigWhenFiveBandsWithRedVioletRed(self):
        colors = ['red', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 272)

    def testDecodeSigFigWhenFiveBandsWithRedVioletOrange(self):
        colors = ['red', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 273)

    def testDecodeSigFigWhenFiveBandsWithRedVioletYellow(self):
        colors = ['red', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 274)

    def testDecodeSigFigWhenFiveBandsWithRedVioletGreen(self):
        colors = ['red', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 275)

    def testDecodeSigFigWhenFiveBandsWithRedVioletBlue(self):
        colors = ['red', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 276)

    def testDecodeSigFigWhenFiveBandsWithRedVioletViolet(self):
        colors = ['red', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 277)

    def testDecodeSigFigWhenFiveBandsWithRedVioletGrey(self):
        colors = ['red', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 278)

    def testDecodeSigFigWhenFiveBandsWithRedVioletWhite(self):
        colors = ['red', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 279)

    def testDecodeSigFigWhenFiveBandsWithRedGreyBlack(self):
        colors = ['red', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 280)

    def testDecodeSigFigWhenFiveBandsWithRedGreyBrown(self):
        colors = ['red', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 281)

    def testDecodeSigFigWhenFiveBandsWithRedGreyRed(self):
        colors = ['red', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 282)

    def testDecodeSigFigWhenFiveBandsWithRedGreyOrange(self):
        colors = ['red', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 283)

    def testDecodeSigFigWhenFiveBandsWithRedGreyYellow(self):
        colors = ['red', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 284)

    def testDecodeSigFigWhenFiveBandsWithRedGreyGreen(self):
        colors = ['red', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 285)

    def testDecodeSigFigWhenFiveBandsWithRedGreyBlue(self):
        colors = ['red', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 286)

    def testDecodeSigFigWhenFiveBandsWithRedGreyViolet(self):
        colors = ['red', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 287)

    def testDecodeSigFigWhenFiveBandsWithRedGreyGrey(self):
        colors = ['red', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 288)

    def testDecodeSigFigWhenFiveBandsWithRedGreyWhite(self):
        colors = ['red', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 289)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteBlack(self):
        colors = ['red', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 290)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteBrown(self):
        colors = ['red', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 291)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteRed(self):
        colors = ['red', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 292)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteOrange(self):
        colors = ['red', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 293)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteYellow(self):
        colors = ['red', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 294)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteGreen(self):
        colors = ['red', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 295)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteBlue(self):
        colors = ['red', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 296)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteViolet(self):
        colors = ['red', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 297)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteGrey(self):
        colors = ['red', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 298)

    def testDecodeSigFigWhenFiveBandsWithRedWhiteWhite(self):
        colors = ['red', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 299)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackBlack(self):
        colors = ['orange', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 300)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackBrown(self):
        colors = ['orange', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 301)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackRed(self):
        colors = ['orange', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 302)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackOrange(self):
        colors = ['orange', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 303)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackYellow(self):
        colors = ['orange', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 304)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackGreen(self):
        colors = ['orange', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 305)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackBlue(self):
        colors = ['orange', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 306)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackViolet(self):
        colors = ['orange', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 307)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackGrey(self):
        colors = ['orange', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 308)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackWhite(self):
        colors = ['orange', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 309)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownBlack(self):
        colors = ['orange', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 310)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownBrown(self):
        colors = ['orange', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 311)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownRed(self):
        colors = ['orange', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 312)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownOrange(self):
        colors = ['orange', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 313)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownYellow(self):
        colors = ['orange', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 314)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownGreen(self):
        colors = ['orange', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 315)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownBlue(self):
        colors = ['orange', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 316)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownViolet(self):
        colors = ['orange', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 317)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownGrey(self):
        colors = ['orange', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 318)

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownWhite(self):
        colors = ['orange', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 319)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedBlack(self):
        colors = ['orange', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 320)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedBrown(self):
        colors = ['orange', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 321)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedRed(self):
        colors = ['orange', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 322)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedOrange(self):
        colors = ['orange', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 323)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedYellow(self):
        colors = ['orange', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 324)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedGreen(self):
        colors = ['orange', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 325)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedBlue(self):
        colors = ['orange', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 326)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedViolet(self):
        colors = ['orange', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 327)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedGrey(self):
        colors = ['orange', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 328)

    def testDecodeSigFigWhenFiveBandsWithOrangeRedWhite(self):
        colors = ['orange', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 329)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeBlack(self):
        colors = ['orange', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 330)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeBrown(self):
        colors = ['orange', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 331)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeRed(self):
        colors = ['orange', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 332)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeOrange(self):
        colors = ['orange', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 333)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeYellow(self):
        colors = ['orange', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 334)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeGreen(self):
        colors = ['orange', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 335)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeBlue(self):
        colors = ['orange', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 336)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeViolet(self):
        colors = ['orange', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 337)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeGrey(self):
        colors = ['orange', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 338)

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeWhite(self):
        colors = ['orange', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 339)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowBlack(self):
        colors = ['orange', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 340)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowBrown(self):
        colors = ['orange', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 341)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowRed(self):
        colors = ['orange', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 342)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowOrange(self):
        colors = ['orange', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 343)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowYellow(self):
        colors = ['orange', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 344)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowGreen(self):
        colors = ['orange', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 345)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowBlue(self):
        colors = ['orange', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 346)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowViolet(self):
        colors = ['orange', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 347)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowGrey(self):
        colors = ['orange', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 348)

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowWhite(self):
        colors = ['orange', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 349)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenBlack(self):
        colors = ['orange', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 350)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenBrown(self):
        colors = ['orange', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 351)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenRed(self):
        colors = ['orange', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 352)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenOrange(self):
        colors = ['orange', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 353)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenYellow(self):
        colors = ['orange', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 354)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenGreen(self):
        colors = ['orange', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 355)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenBlue(self):
        colors = ['orange', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 356)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenViolet(self):
        colors = ['orange', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 357)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenGrey(self):
        colors = ['orange', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 358)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenWhite(self):
        colors = ['orange', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 359)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueBlack(self):
        colors = ['orange', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 360)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueBrown(self):
        colors = ['orange', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 361)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueRed(self):
        colors = ['orange', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 362)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueOrange(self):
        colors = ['orange', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 363)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueYellow(self):
        colors = ['orange', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 364)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueGreen(self):
        colors = ['orange', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 365)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueBlue(self):
        colors = ['orange', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 366)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueViolet(self):
        colors = ['orange', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 367)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueGrey(self):
        colors = ['orange', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 368)

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueWhite(self):
        colors = ['orange', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 369)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletBlack(self):
        colors = ['orange', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 370)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletBrown(self):
        colors = ['orange', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 371)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletRed(self):
        colors = ['orange', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 372)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletOrange(self):
        colors = ['orange', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 373)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletYellow(self):
        colors = ['orange', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 374)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletGreen(self):
        colors = ['orange', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 375)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletBlue(self):
        colors = ['orange', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 376)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletViolet(self):
        colors = ['orange', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 377)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletGrey(self):
        colors = ['orange', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 378)

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletWhite(self):
        colors = ['orange', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 379)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyBlack(self):
        colors = ['orange', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 380)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyBrown(self):
        colors = ['orange', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 381)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyRed(self):
        colors = ['orange', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 382)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyOrange(self):
        colors = ['orange', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 383)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyYellow(self):
        colors = ['orange', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 384)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyGreen(self):
        colors = ['orange', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 385)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyBlue(self):
        colors = ['orange', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 386)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyViolet(self):
        colors = ['orange', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 387)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyGrey(self):
        colors = ['orange', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 388)

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyWhite(self):
        colors = ['orange', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 389)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteBlack(self):
        colors = ['orange', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 390)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteBrown(self):
        colors = ['orange', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 391)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteRed(self):
        colors = ['orange', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 392)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteOrange(self):
        colors = ['orange', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 393)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteYellow(self):
        colors = ['orange', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 394)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteGreen(self):
        colors = ['orange', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 395)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteBlue(self):
        colors = ['orange', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 396)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteViolet(self):
        colors = ['orange', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 397)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteGrey(self):
        colors = ['orange', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 398)

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteWhite(self):
        colors = ['orange', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 399)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackBlack(self):
        colors = ['yellow', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 400)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackBrown(self):
        colors = ['yellow', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 401)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackRed(self):
        colors = ['yellow', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 402)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackOrange(self):
        colors = ['yellow', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 403)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackYellow(self):
        colors = ['yellow', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 404)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackGreen(self):
        colors = ['yellow', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 405)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackBlue(self):
        colors = ['yellow', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 406)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackViolet(self):
        colors = ['yellow', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 407)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackGrey(self):
        colors = ['yellow', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 408)

    def testDecodeSigFigWhenFiveBandsWithYellowBlackWhite(self):
        colors = ['yellow', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 409)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownBlack(self):
        colors = ['yellow', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 410)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownBrown(self):
        colors = ['yellow', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 411)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownRed(self):
        colors = ['yellow', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 412)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownOrange(self):
        colors = ['yellow', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 413)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownYellow(self):
        colors = ['yellow', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 414)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownGreen(self):
        colors = ['yellow', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 415)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownBlue(self):
        colors = ['yellow', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 416)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownViolet(self):
        colors = ['yellow', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 417)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownGrey(self):
        colors = ['yellow', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 418)

    def testDecodeSigFigWhenFiveBandsWithYellowBrownWhite(self):
        colors = ['yellow', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 419)

    def testDecodeSigFigWhenFiveBandsWithYellowRedBlack(self):
        colors = ['yellow', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 420)

    def testDecodeSigFigWhenFiveBandsWithYellowRedBrown(self):
        colors = ['yellow', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 421)

    def testDecodeSigFigWhenFiveBandsWithYellowRedRed(self):
        colors = ['yellow', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 422)

    def testDecodeSigFigWhenFiveBandsWithYellowRedOrange(self):
        colors = ['yellow', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 423)

    def testDecodeSigFigWhenFiveBandsWithYellowRedYellow(self):
        colors = ['yellow', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 424)

    def testDecodeSigFigWhenFiveBandsWithYellowRedGreen(self):
        colors = ['yellow', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 425)

    def testDecodeSigFigWhenFiveBandsWithYellowRedBlue(self):
        colors = ['yellow', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 426)

    def testDecodeSigFigWhenFiveBandsWithYellowRedViolet(self):
        colors = ['yellow', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 427)

    def testDecodeSigFigWhenFiveBandsWithYellowRedGrey(self):
        colors = ['yellow', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 428)

    def testDecodeSigFigWhenFiveBandsWithYellowRedWhite(self):
        colors = ['yellow', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 429)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeBlack(self):
        colors = ['yellow', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 430)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeBrown(self):
        colors = ['yellow', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 431)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeRed(self):
        colors = ['yellow', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 432)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeOrange(self):
        colors = ['yellow', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 433)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeYellow(self):
        colors = ['yellow', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 434)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeGreen(self):
        colors = ['yellow', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 435)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeBlue(self):
        colors = ['yellow', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 436)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeViolet(self):
        colors = ['yellow', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 437)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeGrey(self):
        colors = ['yellow', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 438)

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeWhite(self):
        colors = ['yellow', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 439)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowBlack(self):
        colors = ['yellow', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 440)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowBrown(self):
        colors = ['yellow', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 441)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowRed(self):
        colors = ['yellow', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 442)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowOrange(self):
        colors = ['yellow', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 443)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowYellow(self):
        colors = ['yellow', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 444)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowGreen(self):
        colors = ['yellow', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 445)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowBlue(self):
        colors = ['yellow', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 446)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowViolet(self):
        colors = ['yellow', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 447)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowGrey(self):
        colors = ['yellow', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 448)

    def testDecodeSigFigWhenFiveBandsWithYellowYellowWhite(self):
        colors = ['yellow', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 449)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenBlack(self):
        colors = ['yellow', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 450)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenBrown(self):
        colors = ['yellow', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 451)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenRed(self):
        colors = ['yellow', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 452)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenOrange(self):
        colors = ['yellow', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 453)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenYellow(self):
        colors = ['yellow', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 454)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenGreen(self):
        colors = ['yellow', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 455)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenBlue(self):
        colors = ['yellow', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 456)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenViolet(self):
        colors = ['yellow', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 457)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenGrey(self):
        colors = ['yellow', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 458)

    def testDecodeSigFigWhenFiveBandsWithYellowGreenWhite(self):
        colors = ['yellow', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 459)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueBlack(self):
        colors = ['yellow', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 460)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueBrown(self):
        colors = ['yellow', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 461)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueRed(self):
        colors = ['yellow', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 462)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueOrange(self):
        colors = ['yellow', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 463)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueYellow(self):
        colors = ['yellow', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 464)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueGreen(self):
        colors = ['yellow', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 465)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueBlue(self):
        colors = ['yellow', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 466)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueViolet(self):
        colors = ['yellow', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 467)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueGrey(self):
        colors = ['yellow', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 468)

    def testDecodeSigFigWhenFiveBandsWithYellowBlueWhite(self):
        colors = ['yellow', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 469)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletBlack(self):
        colors = ['yellow', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 470)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletBrown(self):
        colors = ['yellow', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 471)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletRed(self):
        colors = ['yellow', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 472)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletOrange(self):
        colors = ['yellow', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 473)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletYellow(self):
        colors = ['yellow', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 474)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletGreen(self):
        colors = ['yellow', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 475)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletBlue(self):
        colors = ['yellow', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 476)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletViolet(self):
        colors = ['yellow', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 477)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletGrey(self):
        colors = ['yellow', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 478)

    def testDecodeSigFigWhenFiveBandsWithYellowVioletWhite(self):
        colors = ['yellow', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 479)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyBlack(self):
        colors = ['yellow', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 480)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyBrown(self):
        colors = ['yellow', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 481)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyRed(self):
        colors = ['yellow', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 482)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyOrange(self):
        colors = ['yellow', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 483)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyYellow(self):
        colors = ['yellow', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 484)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyGreen(self):
        colors = ['yellow', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 485)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyBlue(self):
        colors = ['yellow', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 486)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyViolet(self):
        colors = ['yellow', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 487)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyGrey(self):
        colors = ['yellow', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 488)

    def testDecodeSigFigWhenFiveBandsWithYellowGreyWhite(self):
        colors = ['yellow', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 489)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteBlack(self):
        colors = ['yellow', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 490)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteBrown(self):
        colors = ['yellow', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 491)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteRed(self):
        colors = ['yellow', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 492)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteOrange(self):
        colors = ['yellow', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 493)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteYellow(self):
        colors = ['yellow', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 494)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteGreen(self):
        colors = ['yellow', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 495)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteBlue(self):
        colors = ['yellow', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 496)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteViolet(self):
        colors = ['yellow', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 497)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteGrey(self):
        colors = ['yellow', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 498)

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteWhite(self):
        colors = ['yellow', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 499)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackBlack(self):
        colors = ['green', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 500)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackBrown(self):
        colors = ['green', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 501)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackRed(self):
        colors = ['green', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 502)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackOrange(self):
        colors = ['green', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 503)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackYellow(self):
        colors = ['green', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 504)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackGreen(self):
        colors = ['green', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 505)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackBlue(self):
        colors = ['green', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 506)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackViolet(self):
        colors = ['green', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 507)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackGrey(self):
        colors = ['green', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 508)

    def testDecodeSigFigWhenFiveBandsWithGreenBlackWhite(self):
        colors = ['green', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 509)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownBlack(self):
        colors = ['green', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 510)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownBrown(self):
        colors = ['green', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 511)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownRed(self):
        colors = ['green', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 512)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownOrange(self):
        colors = ['green', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 513)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownYellow(self):
        colors = ['green', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 514)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownGreen(self):
        colors = ['green', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 515)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownBlue(self):
        colors = ['green', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 516)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownViolet(self):
        colors = ['green', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 517)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownGrey(self):
        colors = ['green', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 518)

    def testDecodeSigFigWhenFiveBandsWithGreenBrownWhite(self):
        colors = ['green', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 519)

    def testDecodeSigFigWhenFiveBandsWithGreenRedBlack(self):
        colors = ['green', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 520)

    def testDecodeSigFigWhenFiveBandsWithGreenRedBrown(self):
        colors = ['green', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 521)

    def testDecodeSigFigWhenFiveBandsWithGreenRedRed(self):
        colors = ['green', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 522)

    def testDecodeSigFigWhenFiveBandsWithGreenRedOrange(self):
        colors = ['green', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 523)

    def testDecodeSigFigWhenFiveBandsWithGreenRedYellow(self):
        colors = ['green', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 524)

    def testDecodeSigFigWhenFiveBandsWithGreenRedGreen(self):
        colors = ['green', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 525)

    def testDecodeSigFigWhenFiveBandsWithGreenRedBlue(self):
        colors = ['green', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 526)

    def testDecodeSigFigWhenFiveBandsWithGreenRedViolet(self):
        colors = ['green', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 527)

    def testDecodeSigFigWhenFiveBandsWithGreenRedGrey(self):
        colors = ['green', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 528)

    def testDecodeSigFigWhenFiveBandsWithGreenRedWhite(self):
        colors = ['green', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 529)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeBlack(self):
        colors = ['green', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 530)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeBrown(self):
        colors = ['green', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 531)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeRed(self):
        colors = ['green', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 532)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeOrange(self):
        colors = ['green', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 533)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeYellow(self):
        colors = ['green', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 534)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeGreen(self):
        colors = ['green', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 535)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeBlue(self):
        colors = ['green', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 536)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeViolet(self):
        colors = ['green', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 537)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeGrey(self):
        colors = ['green', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 538)

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeWhite(self):
        colors = ['green', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 539)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowBlack(self):
        colors = ['green', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 540)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowBrown(self):
        colors = ['green', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 541)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowRed(self):
        colors = ['green', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 542)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowOrange(self):
        colors = ['green', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 543)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowYellow(self):
        colors = ['green', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 544)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowGreen(self):
        colors = ['green', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 545)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowBlue(self):
        colors = ['green', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 546)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowViolet(self):
        colors = ['green', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 547)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowGrey(self):
        colors = ['green', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 548)

    def testDecodeSigFigWhenFiveBandsWithGreenYellowWhite(self):
        colors = ['green', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 549)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenBlack(self):
        colors = ['green', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 550)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenBrown(self):
        colors = ['green', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 551)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenRed(self):
        colors = ['green', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 552)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenOrange(self):
        colors = ['green', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 553)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenYellow(self):
        colors = ['green', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 554)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenGreen(self):
        colors = ['green', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 555)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenBlue(self):
        colors = ['green', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 556)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenViolet(self):
        colors = ['green', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 557)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenGrey(self):
        colors = ['green', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 558)

    def testDecodeSigFigWhenFiveBandsWithGreenGreenWhite(self):
        colors = ['green', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 559)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueBlack(self):
        colors = ['green', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 560)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueBrown(self):
        colors = ['green', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 561)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueRed(self):
        colors = ['green', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 562)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueOrange(self):
        colors = ['green', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 563)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueYellow(self):
        colors = ['green', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 564)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueGreen(self):
        colors = ['green', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 565)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueBlue(self):
        colors = ['green', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 566)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueViolet(self):
        colors = ['green', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 567)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueGrey(self):
        colors = ['green', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 568)

    def testDecodeSigFigWhenFiveBandsWithGreenBlueWhite(self):
        colors = ['green', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 569)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletBlack(self):
        colors = ['green', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 570)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletBrown(self):
        colors = ['green', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 571)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletRed(self):
        colors = ['green', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 572)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletOrange(self):
        colors = ['green', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 573)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletYellow(self):
        colors = ['green', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 574)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletGreen(self):
        colors = ['green', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 575)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletBlue(self):
        colors = ['green', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 576)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletViolet(self):
        colors = ['green', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 577)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletGrey(self):
        colors = ['green', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 578)

    def testDecodeSigFigWhenFiveBandsWithGreenVioletWhite(self):
        colors = ['green', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 579)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyBlack(self):
        colors = ['green', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 580)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyBrown(self):
        colors = ['green', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 581)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyRed(self):
        colors = ['green', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 582)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyOrange(self):
        colors = ['green', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 583)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyYellow(self):
        colors = ['green', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 584)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyGreen(self):
        colors = ['green', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 585)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyBlue(self):
        colors = ['green', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 586)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyViolet(self):
        colors = ['green', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 587)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyGrey(self):
        colors = ['green', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 588)

    def testDecodeSigFigWhenFiveBandsWithGreenGreyWhite(self):
        colors = ['green', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 589)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteBlack(self):
        colors = ['green', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 590)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteBrown(self):
        colors = ['green', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 591)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteRed(self):
        colors = ['green', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 592)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteOrange(self):
        colors = ['green', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 593)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteYellow(self):
        colors = ['green', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 594)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteGreen(self):
        colors = ['green', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 595)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteBlue(self):
        colors = ['green', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 596)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteViolet(self):
        colors = ['green', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 597)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteGrey(self):
        colors = ['green', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 598)

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteWhite(self):
        colors = ['green', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 599)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackBlack(self):
        colors = ['blue', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 600)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackBrown(self):
        colors = ['blue', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 601)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackRed(self):
        colors = ['blue', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 602)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackOrange(self):
        colors = ['blue', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 603)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackYellow(self):
        colors = ['blue', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 604)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackGreen(self):
        colors = ['blue', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 605)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackBlue(self):
        colors = ['blue', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 606)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackViolet(self):
        colors = ['blue', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 607)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackGrey(self):
        colors = ['blue', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 608)

    def testDecodeSigFigWhenFiveBandsWithBlueBlackWhite(self):
        colors = ['blue', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 609)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownBlack(self):
        colors = ['blue', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 610)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownBrown(self):
        colors = ['blue', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 611)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownRed(self):
        colors = ['blue', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 612)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownOrange(self):
        colors = ['blue', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 613)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownYellow(self):
        colors = ['blue', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 614)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownGreen(self):
        colors = ['blue', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 615)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownBlue(self):
        colors = ['blue', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 616)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownViolet(self):
        colors = ['blue', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 617)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownGrey(self):
        colors = ['blue', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 618)

    def testDecodeSigFigWhenFiveBandsWithBlueBrownWhite(self):
        colors = ['blue', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 619)

    def testDecodeSigFigWhenFiveBandsWithBlueRedBlack(self):
        colors = ['blue', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 620)

    def testDecodeSigFigWhenFiveBandsWithBlueRedBrown(self):
        colors = ['blue', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 621)

    def testDecodeSigFigWhenFiveBandsWithBlueRedRed(self):
        colors = ['blue', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 622)

    def testDecodeSigFigWhenFiveBandsWithBlueRedOrange(self):
        colors = ['blue', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 623)

    def testDecodeSigFigWhenFiveBandsWithBlueRedYellow(self):
        colors = ['blue', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 624)

    def testDecodeSigFigWhenFiveBandsWithBlueRedGreen(self):
        colors = ['blue', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 625)

    def testDecodeSigFigWhenFiveBandsWithBlueRedBlue(self):
        colors = ['blue', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 626)

    def testDecodeSigFigWhenFiveBandsWithBlueRedViolet(self):
        colors = ['blue', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 627)

    def testDecodeSigFigWhenFiveBandsWithBlueRedGrey(self):
        colors = ['blue', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 628)

    def testDecodeSigFigWhenFiveBandsWithBlueRedWhite(self):
        colors = ['blue', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 629)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeBlack(self):
        colors = ['blue', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 630)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeBrown(self):
        colors = ['blue', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 631)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeRed(self):
        colors = ['blue', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 632)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeOrange(self):
        colors = ['blue', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 633)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeYellow(self):
        colors = ['blue', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 634)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeGreen(self):
        colors = ['blue', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 635)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeBlue(self):
        colors = ['blue', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 636)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeViolet(self):
        colors = ['blue', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 637)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeGrey(self):
        colors = ['blue', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 638)

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeWhite(self):
        colors = ['blue', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 639)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowBlack(self):
        colors = ['blue', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 640)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowBrown(self):
        colors = ['blue', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 641)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowRed(self):
        colors = ['blue', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 642)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowOrange(self):
        colors = ['blue', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 643)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowYellow(self):
        colors = ['blue', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 644)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowGreen(self):
        colors = ['blue', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 645)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowBlue(self):
        colors = ['blue', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 646)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowViolet(self):
        colors = ['blue', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 647)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowGrey(self):
        colors = ['blue', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 648)

    def testDecodeSigFigWhenFiveBandsWithBlueYellowWhite(self):
        colors = ['blue', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 649)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenBlack(self):
        colors = ['blue', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 650)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenBrown(self):
        colors = ['blue', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 651)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenRed(self):
        colors = ['blue', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 652)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenOrange(self):
        colors = ['blue', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 653)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenYellow(self):
        colors = ['blue', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 654)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenGreen(self):
        colors = ['blue', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 655)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenBlue(self):
        colors = ['blue', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 656)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenViolet(self):
        colors = ['blue', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 657)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenGrey(self):
        colors = ['blue', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 658)

    def testDecodeSigFigWhenFiveBandsWithBlueGreenWhite(self):
        colors = ['blue', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 659)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueBlack(self):
        colors = ['blue', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 660)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueBrown(self):
        colors = ['blue', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 661)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueRed(self):
        colors = ['blue', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 662)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueOrange(self):
        colors = ['blue', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 663)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueYellow(self):
        colors = ['blue', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 664)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueGreen(self):
        colors = ['blue', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 665)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueBlue(self):
        colors = ['blue', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 666)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueViolet(self):
        colors = ['blue', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 667)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueGrey(self):
        colors = ['blue', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 668)

    def testDecodeSigFigWhenFiveBandsWithBlueBlueWhite(self):
        colors = ['blue', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 669)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletBlack(self):
        colors = ['blue', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 670)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletBrown(self):
        colors = ['blue', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 671)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletRed(self):
        colors = ['blue', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 672)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletOrange(self):
        colors = ['blue', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 673)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletYellow(self):
        colors = ['blue', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 674)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletGreen(self):
        colors = ['blue', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 675)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletBlue(self):
        colors = ['blue', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 676)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletViolet(self):
        colors = ['blue', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 677)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletGrey(self):
        colors = ['blue', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 678)

    def testDecodeSigFigWhenFiveBandsWithBlueVioletWhite(self):
        colors = ['blue', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 679)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyBlack(self):
        colors = ['blue', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 680)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyBrown(self):
        colors = ['blue', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 681)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyRed(self):
        colors = ['blue', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 682)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyOrange(self):
        colors = ['blue', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 683)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyYellow(self):
        colors = ['blue', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 684)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyGreen(self):
        colors = ['blue', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 685)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyBlue(self):
        colors = ['blue', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 686)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyViolet(self):
        colors = ['blue', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 687)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyGrey(self):
        colors = ['blue', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 688)

    def testDecodeSigFigWhenFiveBandsWithBlueGreyWhite(self):
        colors = ['blue', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 689)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteBlack(self):
        colors = ['blue', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 690)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteBrown(self):
        colors = ['blue', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 691)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteRed(self):
        colors = ['blue', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 692)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteOrange(self):
        colors = ['blue', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 693)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteYellow(self):
        colors = ['blue', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 694)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteGreen(self):
        colors = ['blue', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 695)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteBlue(self):
        colors = ['blue', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 696)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteViolet(self):
        colors = ['blue', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 697)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteGrey(self):
        colors = ['blue', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 698)

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteWhite(self):
        colors = ['blue', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 699)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackBlack(self):
        colors = ['violet', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 700)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackBrown(self):
        colors = ['violet', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 701)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackRed(self):
        colors = ['violet', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 702)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackOrange(self):
        colors = ['violet', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 703)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackYellow(self):
        colors = ['violet', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 704)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackGreen(self):
        colors = ['violet', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 705)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackBlue(self):
        colors = ['violet', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 706)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackViolet(self):
        colors = ['violet', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 707)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackGrey(self):
        colors = ['violet', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 708)

    def testDecodeSigFigWhenFiveBandsWithVioletBlackWhite(self):
        colors = ['violet', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 709)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownBlack(self):
        colors = ['violet', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 710)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownBrown(self):
        colors = ['violet', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 711)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownRed(self):
        colors = ['violet', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 712)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownOrange(self):
        colors = ['violet', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 713)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownYellow(self):
        colors = ['violet', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 714)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownGreen(self):
        colors = ['violet', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 715)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownBlue(self):
        colors = ['violet', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 716)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownViolet(self):
        colors = ['violet', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 717)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownGrey(self):
        colors = ['violet', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 718)

    def testDecodeSigFigWhenFiveBandsWithVioletBrownWhite(self):
        colors = ['violet', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 719)

    def testDecodeSigFigWhenFiveBandsWithVioletRedBlack(self):
        colors = ['violet', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 720)

    def testDecodeSigFigWhenFiveBandsWithVioletRedBrown(self):
        colors = ['violet', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 721)

    def testDecodeSigFigWhenFiveBandsWithVioletRedRed(self):
        colors = ['violet', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 722)

    def testDecodeSigFigWhenFiveBandsWithVioletRedOrange(self):
        colors = ['violet', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 723)

    def testDecodeSigFigWhenFiveBandsWithVioletRedYellow(self):
        colors = ['violet', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 724)

    def testDecodeSigFigWhenFiveBandsWithVioletRedGreen(self):
        colors = ['violet', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 725)

    def testDecodeSigFigWhenFiveBandsWithVioletRedBlue(self):
        colors = ['violet', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 726)

    def testDecodeSigFigWhenFiveBandsWithVioletRedViolet(self):
        colors = ['violet', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 727)

    def testDecodeSigFigWhenFiveBandsWithVioletRedGrey(self):
        colors = ['violet', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 728)

    def testDecodeSigFigWhenFiveBandsWithVioletRedWhite(self):
        colors = ['violet', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 729)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeBlack(self):
        colors = ['violet', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 730)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeBrown(self):
        colors = ['violet', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 731)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeRed(self):
        colors = ['violet', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 732)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeOrange(self):
        colors = ['violet', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 733)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeYellow(self):
        colors = ['violet', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 734)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeGreen(self):
        colors = ['violet', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 735)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeBlue(self):
        colors = ['violet', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 736)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeViolet(self):
        colors = ['violet', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 737)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeGrey(self):
        colors = ['violet', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 738)

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeWhite(self):
        colors = ['violet', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 739)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowBlack(self):
        colors = ['violet', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 740)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowBrown(self):
        colors = ['violet', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 741)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowRed(self):
        colors = ['violet', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 742)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowOrange(self):
        colors = ['violet', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 743)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowYellow(self):
        colors = ['violet', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 744)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowGreen(self):
        colors = ['violet', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 745)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowBlue(self):
        colors = ['violet', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 746)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowViolet(self):
        colors = ['violet', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 747)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowGrey(self):
        colors = ['violet', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 748)

    def testDecodeSigFigWhenFiveBandsWithVioletYellowWhite(self):
        colors = ['violet', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 749)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenBlack(self):
        colors = ['violet', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 750)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenBrown(self):
        colors = ['violet', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 751)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenRed(self):
        colors = ['violet', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 752)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenOrange(self):
        colors = ['violet', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 753)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenYellow(self):
        colors = ['violet', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 754)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenGreen(self):
        colors = ['violet', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 755)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenBlue(self):
        colors = ['violet', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 756)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenViolet(self):
        colors = ['violet', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 757)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenGrey(self):
        colors = ['violet', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 758)

    def testDecodeSigFigWhenFiveBandsWithVioletGreenWhite(self):
        colors = ['violet', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 759)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueBlack(self):
        colors = ['violet', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 760)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueBrown(self):
        colors = ['violet', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 761)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueRed(self):
        colors = ['violet', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 762)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueOrange(self):
        colors = ['violet', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 763)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueYellow(self):
        colors = ['violet', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 764)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueGreen(self):
        colors = ['violet', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 765)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueBlue(self):
        colors = ['violet', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 766)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueViolet(self):
        colors = ['violet', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 767)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueGrey(self):
        colors = ['violet', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 768)

    def testDecodeSigFigWhenFiveBandsWithVioletBlueWhite(self):
        colors = ['violet', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 769)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletBlack(self):
        colors = ['violet', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 770)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletBrown(self):
        colors = ['violet', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 771)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletRed(self):
        colors = ['violet', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 772)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletOrange(self):
        colors = ['violet', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 773)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletYellow(self):
        colors = ['violet', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 774)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletGreen(self):
        colors = ['violet', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 775)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletBlue(self):
        colors = ['violet', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 776)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletViolet(self):
        colors = ['violet', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 777)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletGrey(self):
        colors = ['violet', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 778)

    def testDecodeSigFigWhenFiveBandsWithVioletVioletWhite(self):
        colors = ['violet', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 779)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyBlack(self):
        colors = ['violet', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 780)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyBrown(self):
        colors = ['violet', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 781)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyRed(self):
        colors = ['violet', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 782)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyOrange(self):
        colors = ['violet', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 783)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyYellow(self):
        colors = ['violet', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 784)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyGreen(self):
        colors = ['violet', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 785)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyBlue(self):
        colors = ['violet', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 786)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyViolet(self):
        colors = ['violet', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 787)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyGrey(self):
        colors = ['violet', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 788)

    def testDecodeSigFigWhenFiveBandsWithVioletGreyWhite(self):
        colors = ['violet', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 789)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteBlack(self):
        colors = ['violet', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 790)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteBrown(self):
        colors = ['violet', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 791)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteRed(self):
        colors = ['violet', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 792)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteOrange(self):
        colors = ['violet', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 793)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteYellow(self):
        colors = ['violet', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 794)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteGreen(self):
        colors = ['violet', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 795)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteBlue(self):
        colors = ['violet', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 796)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteViolet(self):
        colors = ['violet', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 797)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteGrey(self):
        colors = ['violet', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 798)

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteWhite(self):
        colors = ['violet', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 799)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackBlack(self):
        colors = ['grey', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 800)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackBrown(self):
        colors = ['grey', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 801)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackRed(self):
        colors = ['grey', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 802)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackOrange(self):
        colors = ['grey', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 803)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackYellow(self):
        colors = ['grey', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 804)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackGreen(self):
        colors = ['grey', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 805)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackBlue(self):
        colors = ['grey', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 806)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackViolet(self):
        colors = ['grey', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 807)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackGrey(self):
        colors = ['grey', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 808)

    def testDecodeSigFigWhenFiveBandsWithGreyBlackWhite(self):
        colors = ['grey', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 809)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownBlack(self):
        colors = ['grey', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 810)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownBrown(self):
        colors = ['grey', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 811)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownRed(self):
        colors = ['grey', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 812)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownOrange(self):
        colors = ['grey', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 813)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownYellow(self):
        colors = ['grey', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 814)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownGreen(self):
        colors = ['grey', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 815)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownBlue(self):
        colors = ['grey', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 816)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownViolet(self):
        colors = ['grey', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 817)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownGrey(self):
        colors = ['grey', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 818)

    def testDecodeSigFigWhenFiveBandsWithGreyBrownWhite(self):
        colors = ['grey', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 819)

    def testDecodeSigFigWhenFiveBandsWithGreyRedBlack(self):
        colors = ['grey', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 820)

    def testDecodeSigFigWhenFiveBandsWithGreyRedBrown(self):
        colors = ['grey', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 821)

    def testDecodeSigFigWhenFiveBandsWithGreyRedRed(self):
        colors = ['grey', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 822)

    def testDecodeSigFigWhenFiveBandsWithGreyRedOrange(self):
        colors = ['grey', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 823)

    def testDecodeSigFigWhenFiveBandsWithGreyRedYellow(self):
        colors = ['grey', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 824)

    def testDecodeSigFigWhenFiveBandsWithGreyRedGreen(self):
        colors = ['grey', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 825)

    def testDecodeSigFigWhenFiveBandsWithGreyRedBlue(self):
        colors = ['grey', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 826)

    def testDecodeSigFigWhenFiveBandsWithGreyRedViolet(self):
        colors = ['grey', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 827)

    def testDecodeSigFigWhenFiveBandsWithGreyRedGrey(self):
        colors = ['grey', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 828)

    def testDecodeSigFigWhenFiveBandsWithGreyRedWhite(self):
        colors = ['grey', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 829)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeBlack(self):
        colors = ['grey', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 830)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeBrown(self):
        colors = ['grey', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 831)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeRed(self):
        colors = ['grey', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 832)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeOrange(self):
        colors = ['grey', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 833)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeYellow(self):
        colors = ['grey', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 834)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeGreen(self):
        colors = ['grey', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 835)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeBlue(self):
        colors = ['grey', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 836)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeViolet(self):
        colors = ['grey', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 837)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeGrey(self):
        colors = ['grey', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 838)

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeWhite(self):
        colors = ['grey', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 839)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowBlack(self):
        colors = ['grey', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 840)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowBrown(self):
        colors = ['grey', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 841)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowRed(self):
        colors = ['grey', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 842)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowOrange(self):
        colors = ['grey', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 843)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowYellow(self):
        colors = ['grey', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 844)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowGreen(self):
        colors = ['grey', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 845)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowBlue(self):
        colors = ['grey', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 846)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowViolet(self):
        colors = ['grey', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 847)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowGrey(self):
        colors = ['grey', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 848)

    def testDecodeSigFigWhenFiveBandsWithGreyYellowWhite(self):
        colors = ['grey', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 849)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenBlack(self):
        colors = ['grey', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 850)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenBrown(self):
        colors = ['grey', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 851)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenRed(self):
        colors = ['grey', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 852)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenOrange(self):
        colors = ['grey', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 853)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenYellow(self):
        colors = ['grey', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 854)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenGreen(self):
        colors = ['grey', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 855)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenBlue(self):
        colors = ['grey', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 856)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenViolet(self):
        colors = ['grey', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 857)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenGrey(self):
        colors = ['grey', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 858)

    def testDecodeSigFigWhenFiveBandsWithGreyGreenWhite(self):
        colors = ['grey', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 859)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueBlack(self):
        colors = ['grey', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 860)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueBrown(self):
        colors = ['grey', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 861)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueRed(self):
        colors = ['grey', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 862)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueOrange(self):
        colors = ['grey', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 863)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueYellow(self):
        colors = ['grey', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 864)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueGreen(self):
        colors = ['grey', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 865)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueBlue(self):
        colors = ['grey', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 866)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueViolet(self):
        colors = ['grey', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 867)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueGrey(self):
        colors = ['grey', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 868)

    def testDecodeSigFigWhenFiveBandsWithGreyBlueWhite(self):
        colors = ['grey', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 869)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletBlack(self):
        colors = ['grey', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 870)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletBrown(self):
        colors = ['grey', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 871)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletRed(self):
        colors = ['grey', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 872)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletOrange(self):
        colors = ['grey', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 873)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletYellow(self):
        colors = ['grey', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 874)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletGreen(self):
        colors = ['grey', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 875)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletBlue(self):
        colors = ['grey', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 876)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletViolet(self):
        colors = ['grey', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 877)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletGrey(self):
        colors = ['grey', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 878)

    def testDecodeSigFigWhenFiveBandsWithGreyVioletWhite(self):
        colors = ['grey', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 879)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyBlack(self):
        colors = ['grey', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 880)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyBrown(self):
        colors = ['grey', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 881)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyRed(self):
        colors = ['grey', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 882)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyOrange(self):
        colors = ['grey', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 883)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyYellow(self):
        colors = ['grey', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 884)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyGreen(self):
        colors = ['grey', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 885)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyBlue(self):
        colors = ['grey', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 886)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyViolet(self):
        colors = ['grey', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 887)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyGrey(self):
        colors = ['grey', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 888)

    def testDecodeSigFigWhenFiveBandsWithGreyGreyWhite(self):
        colors = ['grey', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 889)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteBlack(self):
        colors = ['grey', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 890)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteBrown(self):
        colors = ['grey', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 891)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteRed(self):
        colors = ['grey', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 892)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteOrange(self):
        colors = ['grey', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 893)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteYellow(self):
        colors = ['grey', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 894)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteGreen(self):
        colors = ['grey', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 895)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteBlue(self):
        colors = ['grey', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 896)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteViolet(self):
        colors = ['grey', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 897)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteGrey(self):
        colors = ['grey', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 898)

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteWhite(self):
        colors = ['grey', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 899)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackBlack(self):
        colors = ['white', 'black', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 900)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackBrown(self):
        colors = ['white', 'black', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 901)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackRed(self):
        colors = ['white', 'black', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 902)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackOrange(self):
        colors = ['white', 'black', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 903)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackYellow(self):
        colors = ['white', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 904)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackGreen(self):
        colors = ['white', 'black', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 905)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackBlue(self):
        colors = ['white', 'black', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 906)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackViolet(self):
        colors = ['white', 'black', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 907)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackGrey(self):
        colors = ['white', 'black', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 908)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackWhite(self):
        colors = ['white', 'black', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 909)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownBlack(self):
        colors = ['white', 'brown', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 910)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownBrown(self):
        colors = ['white', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 911)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownRed(self):
        colors = ['white', 'brown', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 912)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownOrange(self):
        colors = ['white', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 913)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownYellow(self):
        colors = ['white', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 914)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownGreen(self):
        colors = ['white', 'brown', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 915)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownBlue(self):
        colors = ['white', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 916)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownViolet(self):
        colors = ['white', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 917)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownGrey(self):
        colors = ['white', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 918)

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownWhite(self):
        colors = ['white', 'brown', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 919)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedBlack(self):
        colors = ['white', 'red', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 920)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedBrown(self):
        colors = ['white', 'red', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 921)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedRed(self):
        colors = ['white', 'red', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 922)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedOrange(self):
        colors = ['white', 'red', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 923)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedYellow(self):
        colors = ['white', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 924)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedGreen(self):
        colors = ['white', 'red', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 925)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedBlue(self):
        colors = ['white', 'red', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 926)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedViolet(self):
        colors = ['white', 'red', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 927)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedGrey(self):
        colors = ['white', 'red', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 928)

    def testDecodeSigFigWhenFiveBandsWithWhiteRedWhite(self):
        colors = ['white', 'red', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 929)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeBlack(self):
        colors = ['white', 'orange', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 930)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeBrown(self):
        colors = ['white', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 931)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeRed(self):
        colors = ['white', 'orange', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 932)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeOrange(self):
        colors = ['white', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 933)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeYellow(self):
        colors = ['white', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 934)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeGreen(self):
        colors = ['white', 'orange', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 935)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeBlue(self):
        colors = ['white', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 936)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeViolet(self):
        colors = ['white', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 937)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeGrey(self):
        colors = ['white', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 938)

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeWhite(self):
        colors = ['white', 'orange', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 939)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowBlack(self):
        colors = ['white', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 940)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowBrown(self):
        colors = ['white', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 941)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowRed(self):
        colors = ['white', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 942)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowOrange(self):
        colors = ['white', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 943)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowYellow(self):
        colors = ['white', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 944)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowGreen(self):
        colors = ['white', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 945)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowBlue(self):
        colors = ['white', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 946)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowViolet(self):
        colors = ['white', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 947)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowGrey(self):
        colors = ['white', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 948)

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowWhite(self):
        colors = ['white', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 949)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenBlack(self):
        colors = ['white', 'green', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 950)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenBrown(self):
        colors = ['white', 'green', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 951)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenRed(self):
        colors = ['white', 'green', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 952)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenOrange(self):
        colors = ['white', 'green', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 953)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenYellow(self):
        colors = ['white', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 954)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenGreen(self):
        colors = ['white', 'green', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 955)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenBlue(self):
        colors = ['white', 'green', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 956)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenViolet(self):
        colors = ['white', 'green', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 957)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenGrey(self):
        colors = ['white', 'green', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 958)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenWhite(self):
        colors = ['white', 'green', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 959)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueBlack(self):
        colors = ['white', 'blue', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 960)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueBrown(self):
        colors = ['white', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 961)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueRed(self):
        colors = ['white', 'blue', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 962)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueOrange(self):
        colors = ['white', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 963)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueYellow(self):
        colors = ['white', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 964)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueGreen(self):
        colors = ['white', 'blue', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 965)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueBlue(self):
        colors = ['white', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 966)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueViolet(self):
        colors = ['white', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 967)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueGrey(self):
        colors = ['white', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 968)

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueWhite(self):
        colors = ['white', 'blue', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 969)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletBlack(self):
        colors = ['white', 'violet', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 970)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletBrown(self):
        colors = ['white', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 971)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletRed(self):
        colors = ['white', 'violet', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 972)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletOrange(self):
        colors = ['white', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 973)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletYellow(self):
        colors = ['white', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 974)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletGreen(self):
        colors = ['white', 'violet', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 975)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletBlue(self):
        colors = ['white', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 976)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletViolet(self):
        colors = ['white', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 977)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletGrey(self):
        colors = ['white', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 978)

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletWhite(self):
        colors = ['white', 'violet', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 979)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyBlack(self):
        colors = ['white', 'grey', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 980)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyBrown(self):
        colors = ['white', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 981)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyRed(self):
        colors = ['white', 'grey', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 982)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyOrange(self):
        colors = ['white', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 983)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyYellow(self):
        colors = ['white', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 984)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyGreen(self):
        colors = ['white', 'grey', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 985)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyBlue(self):
        colors = ['white', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 986)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyViolet(self):
        colors = ['white', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 987)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyGrey(self):
        colors = ['white', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 988)

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyWhite(self):
        colors = ['white', 'grey', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 989)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteBlack(self):
        colors = ['white', 'white', 'black', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 990)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteBrown(self):
        colors = ['white', 'white', 'brown', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 991)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteRed(self):
        colors = ['white', 'white', 'red', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 992)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteOrange(self):
        colors = ['white', 'white', 'orange', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 993)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteYellow(self):
        colors = ['white', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 994)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteGreen(self):
        colors = ['white', 'white', 'green', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 995)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteBlue(self):
        colors = ['white', 'white', 'blue', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 996)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteViolet(self):
        colors = ['white', 'white', 'violet', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 997)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteGrey(self):
        colors = ['white', 'white', 'grey', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 998)

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteWhite(self):
        colors = ['white', 'white', 'white', 'brown', 'red']
        self.assertEquals(decodeSignificantFigures(colors), 999)
