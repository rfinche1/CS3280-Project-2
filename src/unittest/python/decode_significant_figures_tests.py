import unittest
from resistor import *


class TestDecodeSignificantFiguresTests(unittest.TestCase):

    def testDecodeSigFigWhenFourBandsWithBlackBlack(self):
        colors = ['black', 'black', 'brown', 'red']
        self.assertEquals(0, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackBrown(self):
        colors = ['black', 'brown', 'brown', 'red']
        self.assertEquals(1, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackRed(self):
        colors = ['black', 'red', 'brown', 'red']
        self.assertEquals(2, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackOrange(self):
        colors = ['black', 'orange', 'brown', 'red']
        self.assertEquals(3, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackYellow(self):
        colors = ['black', 'yellow', 'brown', 'red']
        self.assertEquals(4, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackGreen(self):
        colors = ['black', 'green', 'brown', 'red']
        self.assertEquals(5, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackBlue(self):
        colors = ['black', 'blue', 'brown', 'red']
        self.assertEquals(6, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackViolet(self):
        colors = ['black', 'violet', 'brown', 'red']
        self.assertEquals(7, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackGrey(self):
        colors = ['black', 'grey', 'brown', 'red']
        self.assertEquals(8, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlackWhite(self):
        colors = ['black', 'white', 'brown', 'red']
        self.assertEquals(9, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownBlack(self):
        colors = ['brown', 'black', 'brown', 'red']
        self.assertEquals(10, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownBrown(self):
        colors = ['brown', 'brown', 'brown', 'red']
        self.assertEquals(11, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownRed(self):
        colors = ['brown', 'red', 'brown', 'red']
        self.assertEquals(12, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownOrange(self):
        colors = ['brown', 'orange', 'brown', 'red']
        self.assertEquals(13, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownYellow(self):
        colors = ['brown', 'yellow', 'brown', 'red']
        self.assertEquals(14, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownGreen(self):
        colors = ['brown', 'green', 'brown', 'red']
        self.assertEquals(15, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownBlue(self):
        colors = ['brown', 'blue', 'brown', 'red']
        self.assertEquals(16, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownViolet(self):
        colors = ['brown', 'violet', 'brown', 'red']
        self.assertEquals(17, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownGrey(self):
        colors = ['brown', 'grey', 'brown', 'red']
        self.assertEquals(18, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBrownWhite(self):
        colors = ['brown', 'white', 'brown', 'red']
        self.assertEquals(19, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedBlack(self):
        colors = ['red', 'black', 'brown', 'red']
        self.assertEquals(20, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedBrown(self):
        colors = ['red', 'brown', 'brown', 'red']
        self.assertEquals(21, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedRed(self):
        colors = ['red', 'red', 'brown', 'red']
        self.assertEquals(22, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedOrange(self):
        colors = ['red', 'orange', 'brown', 'red']
        self.assertEquals(23, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedYellow(self):
        colors = ['red', 'yellow', 'brown', 'red']
        self.assertEquals(24, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedGreen(self):
        colors = ['red', 'green', 'brown', 'red']
        self.assertEquals(25, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedBlue(self):
        colors = ['red', 'blue', 'brown', 'red']
        self.assertEquals(26, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedViolet(self):
        colors = ['red', 'violet', 'brown', 'red']
        self.assertEquals(27, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedGrey(self):
        colors = ['red', 'grey', 'brown', 'red']
        self.assertEquals(28, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithRedWhite(self):
        colors = ['red', 'white', 'brown', 'red']
        self.assertEquals(29, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeBlack(self):
        colors = ['orange', 'black', 'brown', 'red']
        self.assertEquals(30, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeBrown(self):
        colors = ['orange', 'brown', 'brown', 'red']
        self.assertEquals(31, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeRed(self):
        colors = ['orange', 'red', 'brown', 'red']
        self.assertEquals(32, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeOrange(self):
        colors = ['orange', 'orange', 'brown', 'red']
        self.assertEquals(33, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeYellow(self):
        colors = ['orange', 'yellow', 'brown', 'red']
        self.assertEquals(34, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeGreen(self):
        colors = ['orange', 'green', 'brown', 'red']
        self.assertEquals(35, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeBlue(self):
        colors = ['orange', 'blue', 'brown', 'red']
        self.assertEquals(36, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeViolet(self):
        colors = ['orange', 'violet', 'brown', 'red']
        self.assertEquals(37, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeGrey(self):
        colors = ['orange', 'grey', 'brown', 'red']
        self.assertEquals(38, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithOrangeWhite(self):
        colors = ['orange', 'white', 'brown', 'red']
        self.assertEquals(39, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowBlack(self):
        colors = ['yellow', 'black', 'brown', 'red']
        self.assertEquals(40, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowBrown(self):
        colors = ['yellow', 'brown', 'brown', 'red']
        self.assertEquals(41, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowRed(self):
        colors = ['yellow', 'red', 'brown', 'red']
        self.assertEquals(42, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowOrange(self):
        colors = ['yellow', 'orange', 'brown', 'red']
        self.assertEquals(43, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowYellow(self):
        colors = ['yellow', 'yellow', 'brown', 'red']
        self.assertEquals(44, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowGreen(self):
        colors = ['yellow', 'green', 'brown', 'red']
        self.assertEquals(45, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowBlue(self):
        colors = ['yellow', 'blue', 'brown', 'red']
        self.assertEquals(46, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowViolet(self):
        colors = ['yellow', 'violet', 'brown', 'red']
        self.assertEquals(47, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowGrey(self):
        colors = ['yellow', 'grey', 'brown', 'red']
        self.assertEquals(48, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithYellowWhite(self):
        colors = ['yellow', 'white', 'brown', 'red']
        self.assertEquals(49, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenBlack(self):
        colors = ['green', 'black', 'brown', 'red']
        self.assertEquals(50, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenBrown(self):
        colors = ['green', 'brown', 'brown', 'red']
        self.assertEquals(51, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenRed(self):
        colors = ['green', 'red', 'brown', 'red']
        self.assertEquals(52, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenOrange(self):
        colors = ['green', 'orange', 'brown', 'red']
        self.assertEquals(53, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenYellow(self):
        colors = ['green', 'yellow', 'brown', 'red']
        self.assertEquals(54, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenGreen(self):
        colors = ['green', 'green', 'brown', 'red']
        self.assertEquals(55, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenBlue(self):
        colors = ['green', 'blue', 'brown', 'red']
        self.assertEquals(56, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenViolet(self):
        colors = ['green', 'violet', 'brown', 'red']
        self.assertEquals(57, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenGrey(self):
        colors = ['green', 'grey', 'brown', 'red']
        self.assertEquals(58, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreenWhite(self):
        colors = ['green', 'white', 'brown', 'red']
        self.assertEquals(59, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueBlack(self):
        colors = ['blue', 'black', 'brown', 'red']
        self.assertEquals(60, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueBrown(self):
        colors = ['blue', 'brown', 'brown', 'red']
        self.assertEquals(61, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueRed(self):
        colors = ['blue', 'red', 'brown', 'red']
        self.assertEquals(62, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueOrange(self):
        colors = ['blue', 'orange', 'brown', 'red']
        self.assertEquals(63, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueYellow(self):
        colors = ['blue', 'yellow', 'brown', 'red']
        self.assertEquals(64, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueGreen(self):
        colors = ['blue', 'green', 'brown', 'red']
        self.assertEquals(65, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueBlue(self):
        colors = ['blue', 'blue', 'brown', 'red']
        self.assertEquals(66, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueViolet(self):
        colors = ['blue', 'violet', 'brown', 'red']
        self.assertEquals(67, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueGrey(self):
        colors = ['blue', 'grey', 'brown', 'red']
        self.assertEquals(68, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithBlueWhite(self):
        colors = ['blue', 'white', 'brown', 'red']
        self.assertEquals(69, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletBlack(self):
        colors = ['violet', 'black', 'brown', 'red']
        self.assertEquals(70, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletBrown(self):
        colors = ['violet', 'brown', 'brown', 'red']
        self.assertEquals(71, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletRed(self):
        colors = ['violet', 'red', 'brown', 'red']
        self.assertEquals(72, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletOrange(self):
        colors = ['violet', 'orange', 'brown', 'red']
        self.assertEquals(73, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletYellow(self):
        colors = ['violet', 'yellow', 'brown', 'red']
        self.assertEquals(74, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletGreen(self):
        colors = ['violet', 'green', 'brown', 'red']
        self.assertEquals(75, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletBlue(self):
        colors = ['violet', 'blue', 'brown', 'red']
        self.assertEquals(76, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletViolet(self):
        colors = ['violet', 'violet', 'brown', 'red']
        self.assertEquals(77, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletGrey(self):
        colors = ['violet', 'grey', 'brown', 'red']
        self.assertEquals(78, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithVioletWhite(self):
        colors = ['violet', 'white', 'brown', 'red']
        self.assertEquals(79, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyBlack(self):
        colors = ['grey', 'black', 'brown', 'red']
        self.assertEquals(80, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyBrown(self):
        colors = ['grey', 'brown', 'brown', 'red']
        self.assertEquals(81, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyRed(self):
        colors = ['grey', 'red', 'brown', 'red']
        self.assertEquals(82, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyOrange(self):
        colors = ['grey', 'orange', 'brown', 'red']
        self.assertEquals(83, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyYellow(self):
        colors = ['grey', 'yellow', 'brown', 'red']
        self.assertEquals(84, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyGreen(self):
        colors = ['grey', 'green', 'brown', 'red']
        self.assertEquals(85, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyBlue(self):
        colors = ['grey', 'blue', 'brown', 'red']
        self.assertEquals(86, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyViolet(self):
        colors = ['grey', 'violet', 'brown', 'red']
        self.assertEquals(87, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyGrey(self):
        colors = ['grey', 'grey', 'brown', 'red']
        self.assertEquals(88, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithGreyWhite(self):
        colors = ['grey', 'white', 'brown', 'red']
        self.assertEquals(89, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteBlack(self):
        colors = ['white', 'black', 'brown', 'red']
        self.assertEquals(90, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteBrown(self):
        colors = ['white', 'brown', 'brown', 'red']
        self.assertEquals(91, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteRed(self):
        colors = ['white', 'red', 'brown', 'red']
        self.assertEquals(92, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteOrange(self):
        colors = ['white', 'orange', 'brown', 'red']
        self.assertEquals(93, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteYellow(self):
        colors = ['white', 'yellow', 'brown', 'red']
        self.assertEquals(94, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteGreen(self):
        colors = ['white', 'green', 'brown', 'red']
        self.assertEquals(95, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteBlue(self):
        colors = ['white', 'blue', 'brown', 'red']
        self.assertEquals(96, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteViolet(self):
        colors = ['white', 'violet', 'brown', 'red']
        self.assertEquals(97, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteGrey(self):
        colors = ['white', 'grey', 'brown', 'red']
        self.assertEquals(98, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFourBandsWithWhiteWhite(self):
        colors = ['white', 'white', 'brown', 'red']
        self.assertEquals(99, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackBlack(self):
        colors = ['black', 'black', 'black', 'brown', 'red']
        self.assertEquals(0, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackBrown(self):
        colors = ['black', 'black', 'brown', 'brown', 'red']
        self.assertEquals(1, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackRed(self):
        colors = ['black', 'black', 'red', 'brown', 'red']
        self.assertEquals(2, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackOrange(self):
        colors = ['black', 'black', 'orange', 'brown', 'red']
        self.assertEquals(3, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackYellow(self):
        colors = ['black', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(4, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackGreen(self):
        colors = ['black', 'black', 'green', 'brown', 'red']
        self.assertEquals(5, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackBlue(self):
        colors = ['black', 'black', 'blue', 'brown', 'red']
        self.assertEquals(6, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackViolet(self):
        colors = ['black', 'black', 'violet', 'brown', 'red']
        self.assertEquals(7, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackGrey(self):
        colors = ['black', 'black', 'grey', 'brown', 'red']
        self.assertEquals(8, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlackWhite(self):
        colors = ['black', 'black', 'white', 'brown', 'red']
        self.assertEquals(9, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownBlack(self):
        colors = ['black', 'brown', 'black', 'brown', 'red']
        self.assertEquals(10, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownBrown(self):
        colors = ['black', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(11, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownRed(self):
        colors = ['black', 'brown', 'red', 'brown', 'red']
        self.assertEquals(12, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownOrange(self):
        colors = ['black', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(13, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownYellow(self):
        colors = ['black', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(14, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownGreen(self):
        colors = ['black', 'brown', 'green', 'brown', 'red']
        self.assertEquals(15, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownBlue(self):
        colors = ['black', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(16, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownViolet(self):
        colors = ['black', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(17, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownGrey(self):
        colors = ['black', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(18, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBrownWhite(self):
        colors = ['black', 'brown', 'white', 'brown', 'red']
        self.assertEquals(19, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedBlack(self):
        colors = ['black', 'red', 'black', 'brown', 'red']
        self.assertEquals(20, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedBrown(self):
        colors = ['black', 'red', 'brown', 'brown', 'red']
        self.assertEquals(21, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedRed(self):
        colors = ['black', 'red', 'red', 'brown', 'red']
        self.assertEquals(22, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedOrange(self):
        colors = ['black', 'red', 'orange', 'brown', 'red']
        self.assertEquals(23, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedYellow(self):
        colors = ['black', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(24, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedGreen(self):
        colors = ['black', 'red', 'green', 'brown', 'red']
        self.assertEquals(25, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedBlue(self):
        colors = ['black', 'red', 'blue', 'brown', 'red']
        self.assertEquals(26, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedViolet(self):
        colors = ['black', 'red', 'violet', 'brown', 'red']
        self.assertEquals(27, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedGrey(self):
        colors = ['black', 'red', 'grey', 'brown', 'red']
        self.assertEquals(28, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackRedWhite(self):
        colors = ['black', 'red', 'white', 'brown', 'red']
        self.assertEquals(29, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeBlack(self):
        colors = ['black', 'orange', 'black', 'brown', 'red']
        self.assertEquals(30, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeBrown(self):
        colors = ['black', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(31, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeRed(self):
        colors = ['black', 'orange', 'red', 'brown', 'red']
        self.assertEquals(32, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeOrange(self):
        colors = ['black', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(33, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeYellow(self):
        colors = ['black', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(34, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeGreen(self):
        colors = ['black', 'orange', 'green', 'brown', 'red']
        self.assertEquals(35, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeBlue(self):
        colors = ['black', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(36, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeViolet(self):
        colors = ['black', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(37, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeGrey(self):
        colors = ['black', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(38, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackOrangeWhite(self):
        colors = ['black', 'orange', 'white', 'brown', 'red']
        self.assertEquals(39, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowBlack(self):
        colors = ['black', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(40, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowBrown(self):
        colors = ['black', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(41, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowRed(self):
        colors = ['black', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(42, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowOrange(self):
        colors = ['black', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(43, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowYellow(self):
        colors = ['black', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(44, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowGreen(self):
        colors = ['black', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(45, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowBlue(self):
        colors = ['black', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(46, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowViolet(self):
        colors = ['black', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(47, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowGrey(self):
        colors = ['black', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(48, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackYellowWhite(self):
        colors = ['black', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(49, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenBlack(self):
        colors = ['black', 'green', 'black', 'brown', 'red']
        self.assertEquals(50, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenBrown(self):
        colors = ['black', 'green', 'brown', 'brown', 'red']
        self.assertEquals(51, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenRed(self):
        colors = ['black', 'green', 'red', 'brown', 'red']
        self.assertEquals(52, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenOrange(self):
        colors = ['black', 'green', 'orange', 'brown', 'red']
        self.assertEquals(53, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenYellow(self):
        colors = ['black', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(54, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenGreen(self):
        colors = ['black', 'green', 'green', 'brown', 'red']
        self.assertEquals(55, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenBlue(self):
        colors = ['black', 'green', 'blue', 'brown', 'red']
        self.assertEquals(56, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenViolet(self):
        colors = ['black', 'green', 'violet', 'brown', 'red']
        self.assertEquals(57, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenGrey(self):
        colors = ['black', 'green', 'grey', 'brown', 'red']
        self.assertEquals(58, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreenWhite(self):
        colors = ['black', 'green', 'white', 'brown', 'red']
        self.assertEquals(59, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueBlack(self):
        colors = ['black', 'blue', 'black', 'brown', 'red']
        self.assertEquals(60, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueBrown(self):
        colors = ['black', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(61, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueRed(self):
        colors = ['black', 'blue', 'red', 'brown', 'red']
        self.assertEquals(62, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueOrange(self):
        colors = ['black', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(63, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueYellow(self):
        colors = ['black', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(64, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueGreen(self):
        colors = ['black', 'blue', 'green', 'brown', 'red']
        self.assertEquals(65, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueBlue(self):
        colors = ['black', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(66, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueViolet(self):
        colors = ['black', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(67, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueGrey(self):
        colors = ['black', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(68, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackBlueWhite(self):
        colors = ['black', 'blue', 'white', 'brown', 'red']
        self.assertEquals(69, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletBlack(self):
        colors = ['black', 'violet', 'black', 'brown', 'red']
        self.assertEquals(70, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletBrown(self):
        colors = ['black', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(71, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletRed(self):
        colors = ['black', 'violet', 'red', 'brown', 'red']
        self.assertEquals(72, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletOrange(self):
        colors = ['black', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(73, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletYellow(self):
        colors = ['black', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(74, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletGreen(self):
        colors = ['black', 'violet', 'green', 'brown', 'red']
        self.assertEquals(75, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletBlue(self):
        colors = ['black', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(76, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletViolet(self):
        colors = ['black', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(77, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletGrey(self):
        colors = ['black', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(78, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackVioletWhite(self):
        colors = ['black', 'violet', 'white', 'brown', 'red']
        self.assertEquals(79, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyBlack(self):
        colors = ['black', 'grey', 'black', 'brown', 'red']
        self.assertEquals(80, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyBrown(self):
        colors = ['black', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(81, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyRed(self):
        colors = ['black', 'grey', 'red', 'brown', 'red']
        self.assertEquals(82, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyOrange(self):
        colors = ['black', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(83, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyYellow(self):
        colors = ['black', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(84, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyGreen(self):
        colors = ['black', 'grey', 'green', 'brown', 'red']
        self.assertEquals(85, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyBlue(self):
        colors = ['black', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(86, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyViolet(self):
        colors = ['black', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(87, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyGrey(self):
        colors = ['black', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(88, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackGreyWhite(self):
        colors = ['black', 'grey', 'white', 'brown', 'red']
        self.assertEquals(89, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteBlack(self):
        colors = ['black', 'white', 'black', 'brown', 'red']
        self.assertEquals(90, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteBrown(self):
        colors = ['black', 'white', 'brown', 'brown', 'red']
        self.assertEquals(91, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteRed(self):
        colors = ['black', 'white', 'red', 'brown', 'red']
        self.assertEquals(92, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteOrange(self):
        colors = ['black', 'white', 'orange', 'brown', 'red']
        self.assertEquals(93, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteYellow(self):
        colors = ['black', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(94, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteGreen(self):
        colors = ['black', 'white', 'green', 'brown', 'red']
        self.assertEquals(95, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteBlue(self):
        colors = ['black', 'white', 'blue', 'brown', 'red']
        self.assertEquals(96, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteViolet(self):
        colors = ['black', 'white', 'violet', 'brown', 'red']
        self.assertEquals(97, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteGrey(self):
        colors = ['black', 'white', 'grey', 'brown', 'red']
        self.assertEquals(98, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlackWhiteWhite(self):
        colors = ['black', 'white', 'white', 'brown', 'red']
        self.assertEquals(99, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackBlack(self):
        colors = ['brown', 'black', 'black', 'brown', 'red']
        self.assertEquals(100, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackBrown(self):
        colors = ['brown', 'black', 'brown', 'brown', 'red']
        self.assertEquals(101, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackRed(self):
        colors = ['brown', 'black', 'red', 'brown', 'red']
        self.assertEquals(102, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackOrange(self):
        colors = ['brown', 'black', 'orange', 'brown', 'red']
        self.assertEquals(103, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackYellow(self):
        colors = ['brown', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(104, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackGreen(self):
        colors = ['brown', 'black', 'green', 'brown', 'red']
        self.assertEquals(105, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackBlue(self):
        colors = ['brown', 'black', 'blue', 'brown', 'red']
        self.assertEquals(106, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackViolet(self):
        colors = ['brown', 'black', 'violet', 'brown', 'red']
        self.assertEquals(107, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackGrey(self):
        colors = ['brown', 'black', 'grey', 'brown', 'red']
        self.assertEquals(108, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlackWhite(self):
        colors = ['brown', 'black', 'white', 'brown', 'red']
        self.assertEquals(109, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownBlack(self):
        colors = ['brown', 'brown', 'black', 'brown', 'red']
        self.assertEquals(110, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownBrown(self):
        colors = ['brown', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(111, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownRed(self):
        colors = ['brown', 'brown', 'red', 'brown', 'red']
        self.assertEquals(112, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownOrange(self):
        colors = ['brown', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(113, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownYellow(self):
        colors = ['brown', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(114, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownGreen(self):
        colors = ['brown', 'brown', 'green', 'brown', 'red']
        self.assertEquals(115, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownBlue(self):
        colors = ['brown', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(116, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownViolet(self):
        colors = ['brown', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(117, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownGrey(self):
        colors = ['brown', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(118, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBrownWhite(self):
        colors = ['brown', 'brown', 'white', 'brown', 'red']
        self.assertEquals(119, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedBlack(self):
        colors = ['brown', 'red', 'black', 'brown', 'red']
        self.assertEquals(120, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedBrown(self):
        colors = ['brown', 'red', 'brown', 'brown', 'red']
        self.assertEquals(121, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedRed(self):
        colors = ['brown', 'red', 'red', 'brown', 'red']
        self.assertEquals(122, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedOrange(self):
        colors = ['brown', 'red', 'orange', 'brown', 'red']
        self.assertEquals(123, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedYellow(self):
        colors = ['brown', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(124, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedGreen(self):
        colors = ['brown', 'red', 'green', 'brown', 'red']
        self.assertEquals(125, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedBlue(self):
        colors = ['brown', 'red', 'blue', 'brown', 'red']
        self.assertEquals(126, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedViolet(self):
        colors = ['brown', 'red', 'violet', 'brown', 'red']
        self.assertEquals(127, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedGrey(self):
        colors = ['brown', 'red', 'grey', 'brown', 'red']
        self.assertEquals(128, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownRedWhite(self):
        colors = ['brown', 'red', 'white', 'brown', 'red']
        self.assertEquals(129, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeBlack(self):
        colors = ['brown', 'orange', 'black', 'brown', 'red']
        self.assertEquals(130, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeBrown(self):
        colors = ['brown', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(131, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeRed(self):
        colors = ['brown', 'orange', 'red', 'brown', 'red']
        self.assertEquals(132, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeOrange(self):
        colors = ['brown', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(133, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeYellow(self):
        colors = ['brown', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(134, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeGreen(self):
        colors = ['brown', 'orange', 'green', 'brown', 'red']
        self.assertEquals(135, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeBlue(self):
        colors = ['brown', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(136, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeViolet(self):
        colors = ['brown', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(137, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeGrey(self):
        colors = ['brown', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(138, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownOrangeWhite(self):
        colors = ['brown', 'orange', 'white', 'brown', 'red']
        self.assertEquals(139, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowBlack(self):
        colors = ['brown', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(140, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowBrown(self):
        colors = ['brown', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(141, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowRed(self):
        colors = ['brown', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(142, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowOrange(self):
        colors = ['brown', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(143, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowYellow(self):
        colors = ['brown', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(144, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowGreen(self):
        colors = ['brown', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(145, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowBlue(self):
        colors = ['brown', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(146, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowViolet(self):
        colors = ['brown', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(147, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowGrey(self):
        colors = ['brown', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(148, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownYellowWhite(self):
        colors = ['brown', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(149, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenBlack(self):
        colors = ['brown', 'green', 'black', 'brown', 'red']
        self.assertEquals(150, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenBrown(self):
        colors = ['brown', 'green', 'brown', 'brown', 'red']
        self.assertEquals(151, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenRed(self):
        colors = ['brown', 'green', 'red', 'brown', 'red']
        self.assertEquals(152, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenOrange(self):
        colors = ['brown', 'green', 'orange', 'brown', 'red']
        self.assertEquals(153, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenYellow(self):
        colors = ['brown', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(154, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenGreen(self):
        colors = ['brown', 'green', 'green', 'brown', 'red']
        self.assertEquals(155, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenBlue(self):
        colors = ['brown', 'green', 'blue', 'brown', 'red']
        self.assertEquals(156, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenViolet(self):
        colors = ['brown', 'green', 'violet', 'brown', 'red']
        self.assertEquals(157, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenGrey(self):
        colors = ['brown', 'green', 'grey', 'brown', 'red']
        self.assertEquals(158, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreenWhite(self):
        colors = ['brown', 'green', 'white', 'brown', 'red']
        self.assertEquals(159, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueBlack(self):
        colors = ['brown', 'blue', 'black', 'brown', 'red']
        self.assertEquals(160, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueBrown(self):
        colors = ['brown', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(161, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueRed(self):
        colors = ['brown', 'blue', 'red', 'brown', 'red']
        self.assertEquals(162, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueOrange(self):
        colors = ['brown', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(163, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueYellow(self):
        colors = ['brown', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(164, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueGreen(self):
        colors = ['brown', 'blue', 'green', 'brown', 'red']
        self.assertEquals(165, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueBlue(self):
        colors = ['brown', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(166, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueViolet(self):
        colors = ['brown', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(167, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueGrey(self):
        colors = ['brown', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(168, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownBlueWhite(self):
        colors = ['brown', 'blue', 'white', 'brown', 'red']
        self.assertEquals(169, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletBlack(self):
        colors = ['brown', 'violet', 'black', 'brown', 'red']
        self.assertEquals(170, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletBrown(self):
        colors = ['brown', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(171, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletRed(self):
        colors = ['brown', 'violet', 'red', 'brown', 'red']
        self.assertEquals(172, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletOrange(self):
        colors = ['brown', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(173, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletYellow(self):
        colors = ['brown', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(174, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletGreen(self):
        colors = ['brown', 'violet', 'green', 'brown', 'red']
        self.assertEquals(175, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletBlue(self):
        colors = ['brown', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(176, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletViolet(self):
        colors = ['brown', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(177, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletGrey(self):
        colors = ['brown', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(178, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownVioletWhite(self):
        colors = ['brown', 'violet', 'white', 'brown', 'red']
        self.assertEquals(179, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyBlack(self):
        colors = ['brown', 'grey', 'black', 'brown', 'red']
        self.assertEquals(180, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyBrown(self):
        colors = ['brown', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(181, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyRed(self):
        colors = ['brown', 'grey', 'red', 'brown', 'red']
        self.assertEquals(182, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyOrange(self):
        colors = ['brown', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(183, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyYellow(self):
        colors = ['brown', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(184, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyGreen(self):
        colors = ['brown', 'grey', 'green', 'brown', 'red']
        self.assertEquals(185, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyBlue(self):
        colors = ['brown', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(186, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyViolet(self):
        colors = ['brown', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(187, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyGrey(self):
        colors = ['brown', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(188, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownGreyWhite(self):
        colors = ['brown', 'grey', 'white', 'brown', 'red']
        self.assertEquals(189, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteBlack(self):
        colors = ['brown', 'white', 'black', 'brown', 'red']
        self.assertEquals(190, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteBrown(self):
        colors = ['brown', 'white', 'brown', 'brown', 'red']
        self.assertEquals(191, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteRed(self):
        colors = ['brown', 'white', 'red', 'brown', 'red']
        self.assertEquals(192, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteOrange(self):
        colors = ['brown', 'white', 'orange', 'brown', 'red']
        self.assertEquals(193, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteYellow(self):
        colors = ['brown', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(194, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteGreen(self):
        colors = ['brown', 'white', 'green', 'brown', 'red']
        self.assertEquals(195, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteBlue(self):
        colors = ['brown', 'white', 'blue', 'brown', 'red']
        self.assertEquals(196, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteViolet(self):
        colors = ['brown', 'white', 'violet', 'brown', 'red']
        self.assertEquals(197, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteGrey(self):
        colors = ['brown', 'white', 'grey', 'brown', 'red']
        self.assertEquals(198, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBrownWhiteWhite(self):
        colors = ['brown', 'white', 'white', 'brown', 'red']
        self.assertEquals(199, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackBlack(self):
        colors = ['red', 'black', 'black', 'brown', 'red']
        self.assertEquals(200, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackBrown(self):
        colors = ['red', 'black', 'brown', 'brown', 'red']
        self.assertEquals(201, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackRed(self):
        colors = ['red', 'black', 'red', 'brown', 'red']
        self.assertEquals(202, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackOrange(self):
        colors = ['red', 'black', 'orange', 'brown', 'red']
        self.assertEquals(203, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackYellow(self):
        colors = ['red', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(204, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackGreen(self):
        colors = ['red', 'black', 'green', 'brown', 'red']
        self.assertEquals(205, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackBlue(self):
        colors = ['red', 'black', 'blue', 'brown', 'red']
        self.assertEquals(206, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackViolet(self):
        colors = ['red', 'black', 'violet', 'brown', 'red']
        self.assertEquals(207, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackGrey(self):
        colors = ['red', 'black', 'grey', 'brown', 'red']
        self.assertEquals(208, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlackWhite(self):
        colors = ['red', 'black', 'white', 'brown', 'red']
        self.assertEquals(209, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownBlack(self):
        colors = ['red', 'brown', 'black', 'brown', 'red']
        self.assertEquals(210, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownBrown(self):
        colors = ['red', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(211, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownRed(self):
        colors = ['red', 'brown', 'red', 'brown', 'red']
        self.assertEquals(212, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownOrange(self):
        colors = ['red', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(213, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownYellow(self):
        colors = ['red', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(214, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownGreen(self):
        colors = ['red', 'brown', 'green', 'brown', 'red']
        self.assertEquals(215, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownBlue(self):
        colors = ['red', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(216, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownViolet(self):
        colors = ['red', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(217, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownGrey(self):
        colors = ['red', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(218, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBrownWhite(self):
        colors = ['red', 'brown', 'white', 'brown', 'red']
        self.assertEquals(219, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedBlack(self):
        colors = ['red', 'red', 'black', 'brown', 'red']
        self.assertEquals(220, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedBrown(self):
        colors = ['red', 'red', 'brown', 'brown', 'red']
        self.assertEquals(221, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedRed(self):
        colors = ['red', 'red', 'red', 'brown', 'red']
        self.assertEquals(222, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedOrange(self):
        colors = ['red', 'red', 'orange', 'brown', 'red']
        self.assertEquals(223, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedYellow(self):
        colors = ['red', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(224, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedGreen(self):
        colors = ['red', 'red', 'green', 'brown', 'red']
        self.assertEquals(225, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedBlue(self):
        colors = ['red', 'red', 'blue', 'brown', 'red']
        self.assertEquals(226, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedViolet(self):
        colors = ['red', 'red', 'violet', 'brown', 'red']
        self.assertEquals(227, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedGrey(self):
        colors = ['red', 'red', 'grey', 'brown', 'red']
        self.assertEquals(228, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedRedWhite(self):
        colors = ['red', 'red', 'white', 'brown', 'red']
        self.assertEquals(229, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeBlack(self):
        colors = ['red', 'orange', 'black', 'brown', 'red']
        self.assertEquals(230, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeBrown(self):
        colors = ['red', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(231, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeRed(self):
        colors = ['red', 'orange', 'red', 'brown', 'red']
        self.assertEquals(232, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeOrange(self):
        colors = ['red', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(233, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeYellow(self):
        colors = ['red', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(234, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeGreen(self):
        colors = ['red', 'orange', 'green', 'brown', 'red']
        self.assertEquals(235, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeBlue(self):
        colors = ['red', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(236, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeViolet(self):
        colors = ['red', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(237, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeGrey(self):
        colors = ['red', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(238, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedOrangeWhite(self):
        colors = ['red', 'orange', 'white', 'brown', 'red']
        self.assertEquals(239, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowBlack(self):
        colors = ['red', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(240, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowBrown(self):
        colors = ['red', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(241, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowRed(self):
        colors = ['red', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(242, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowOrange(self):
        colors = ['red', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(243, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowYellow(self):
        colors = ['red', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(244, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowGreen(self):
        colors = ['red', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(245, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowBlue(self):
        colors = ['red', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(246, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowViolet(self):
        colors = ['red', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(247, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowGrey(self):
        colors = ['red', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(248, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedYellowWhite(self):
        colors = ['red', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(249, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenBlack(self):
        colors = ['red', 'green', 'black', 'brown', 'red']
        self.assertEquals(250, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenBrown(self):
        colors = ['red', 'green', 'brown', 'brown', 'red']
        self.assertEquals(251, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenRed(self):
        colors = ['red', 'green', 'red', 'brown', 'red']
        self.assertEquals(252, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenOrange(self):
        colors = ['red', 'green', 'orange', 'brown', 'red']
        self.assertEquals(253, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenYellow(self):
        colors = ['red', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(254, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenGreen(self):
        colors = ['red', 'green', 'green', 'brown', 'red']
        self.assertEquals(255, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenBlue(self):
        colors = ['red', 'green', 'blue', 'brown', 'red']
        self.assertEquals(256, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenViolet(self):
        colors = ['red', 'green', 'violet', 'brown', 'red']
        self.assertEquals(257, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenGrey(self):
        colors = ['red', 'green', 'grey', 'brown', 'red']
        self.assertEquals(258, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreenWhite(self):
        colors = ['red', 'green', 'white', 'brown', 'red']
        self.assertEquals(259, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueBlack(self):
        colors = ['red', 'blue', 'black', 'brown', 'red']
        self.assertEquals(260, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueBrown(self):
        colors = ['red', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(261, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueRed(self):
        colors = ['red', 'blue', 'red', 'brown', 'red']
        self.assertEquals(262, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueOrange(self):
        colors = ['red', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(263, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueYellow(self):
        colors = ['red', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(264, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueGreen(self):
        colors = ['red', 'blue', 'green', 'brown', 'red']
        self.assertEquals(265, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueBlue(self):
        colors = ['red', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(266, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueViolet(self):
        colors = ['red', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(267, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueGrey(self):
        colors = ['red', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(268, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedBlueWhite(self):
        colors = ['red', 'blue', 'white', 'brown', 'red']
        self.assertEquals(269, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletBlack(self):
        colors = ['red', 'violet', 'black', 'brown', 'red']
        self.assertEquals(270, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletBrown(self):
        colors = ['red', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(271, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletRed(self):
        colors = ['red', 'violet', 'red', 'brown', 'red']
        self.assertEquals(272, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletOrange(self):
        colors = ['red', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(273, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletYellow(self):
        colors = ['red', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(274, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletGreen(self):
        colors = ['red', 'violet', 'green', 'brown', 'red']
        self.assertEquals(275, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletBlue(self):
        colors = ['red', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(276, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletViolet(self):
        colors = ['red', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(277, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletGrey(self):
        colors = ['red', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(278, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedVioletWhite(self):
        colors = ['red', 'violet', 'white', 'brown', 'red']
        self.assertEquals(279, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyBlack(self):
        colors = ['red', 'grey', 'black', 'brown', 'red']
        self.assertEquals(280, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyBrown(self):
        colors = ['red', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(281, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyRed(self):
        colors = ['red', 'grey', 'red', 'brown', 'red']
        self.assertEquals(282, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyOrange(self):
        colors = ['red', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(283, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyYellow(self):
        colors = ['red', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(284, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyGreen(self):
        colors = ['red', 'grey', 'green', 'brown', 'red']
        self.assertEquals(285, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyBlue(self):
        colors = ['red', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(286, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyViolet(self):
        colors = ['red', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(287, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyGrey(self):
        colors = ['red', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(288, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedGreyWhite(self):
        colors = ['red', 'grey', 'white', 'brown', 'red']
        self.assertEquals(289, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteBlack(self):
        colors = ['red', 'white', 'black', 'brown', 'red']
        self.assertEquals(290, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteBrown(self):
        colors = ['red', 'white', 'brown', 'brown', 'red']
        self.assertEquals(291, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteRed(self):
        colors = ['red', 'white', 'red', 'brown', 'red']
        self.assertEquals(292, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteOrange(self):
        colors = ['red', 'white', 'orange', 'brown', 'red']
        self.assertEquals(293, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteYellow(self):
        colors = ['red', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(294, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteGreen(self):
        colors = ['red', 'white', 'green', 'brown', 'red']
        self.assertEquals(295, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteBlue(self):
        colors = ['red', 'white', 'blue', 'brown', 'red']
        self.assertEquals(296, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteViolet(self):
        colors = ['red', 'white', 'violet', 'brown', 'red']
        self.assertEquals(297, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteGrey(self):
        colors = ['red', 'white', 'grey', 'brown', 'red']
        self.assertEquals(298, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithRedWhiteWhite(self):
        colors = ['red', 'white', 'white', 'brown', 'red']
        self.assertEquals(299, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackBlack(self):
        colors = ['orange', 'black', 'black', 'brown', 'red']
        self.assertEquals(300, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackBrown(self):
        colors = ['orange', 'black', 'brown', 'brown', 'red']
        self.assertEquals(301, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackRed(self):
        colors = ['orange', 'black', 'red', 'brown', 'red']
        self.assertEquals(302, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackOrange(self):
        colors = ['orange', 'black', 'orange', 'brown', 'red']
        self.assertEquals(303, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackYellow(self):
        colors = ['orange', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(304, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackGreen(self):
        colors = ['orange', 'black', 'green', 'brown', 'red']
        self.assertEquals(305, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackBlue(self):
        colors = ['orange', 'black', 'blue', 'brown', 'red']
        self.assertEquals(306, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackViolet(self):
        colors = ['orange', 'black', 'violet', 'brown', 'red']
        self.assertEquals(307, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackGrey(self):
        colors = ['orange', 'black', 'grey', 'brown', 'red']
        self.assertEquals(308, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlackWhite(self):
        colors = ['orange', 'black', 'white', 'brown', 'red']
        self.assertEquals(309, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownBlack(self):
        colors = ['orange', 'brown', 'black', 'brown', 'red']
        self.assertEquals(310, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownBrown(self):
        colors = ['orange', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(311, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownRed(self):
        colors = ['orange', 'brown', 'red', 'brown', 'red']
        self.assertEquals(312, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownOrange(self):
        colors = ['orange', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(313, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownYellow(self):
        colors = ['orange', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(314, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownGreen(self):
        colors = ['orange', 'brown', 'green', 'brown', 'red']
        self.assertEquals(315, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownBlue(self):
        colors = ['orange', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(316, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownViolet(self):
        colors = ['orange', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(317, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownGrey(self):
        colors = ['orange', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(318, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBrownWhite(self):
        colors = ['orange', 'brown', 'white', 'brown', 'red']
        self.assertEquals(319, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedBlack(self):
        colors = ['orange', 'red', 'black', 'brown', 'red']
        self.assertEquals(320, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedBrown(self):
        colors = ['orange', 'red', 'brown', 'brown', 'red']
        self.assertEquals(321, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedRed(self):
        colors = ['orange', 'red', 'red', 'brown', 'red']
        self.assertEquals(322, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedOrange(self):
        colors = ['orange', 'red', 'orange', 'brown', 'red']
        self.assertEquals(323, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedYellow(self):
        colors = ['orange', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(324, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedGreen(self):
        colors = ['orange', 'red', 'green', 'brown', 'red']
        self.assertEquals(325, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedBlue(self):
        colors = ['orange', 'red', 'blue', 'brown', 'red']
        self.assertEquals(326, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedViolet(self):
        colors = ['orange', 'red', 'violet', 'brown', 'red']
        self.assertEquals(327, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedGrey(self):
        colors = ['orange', 'red', 'grey', 'brown', 'red']
        self.assertEquals(328, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeRedWhite(self):
        colors = ['orange', 'red', 'white', 'brown', 'red']
        self.assertEquals(329, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeBlack(self):
        colors = ['orange', 'orange', 'black', 'brown', 'red']
        self.assertEquals(330, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeBrown(self):
        colors = ['orange', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(331, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeRed(self):
        colors = ['orange', 'orange', 'red', 'brown', 'red']
        self.assertEquals(332, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeOrange(self):
        colors = ['orange', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(333, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeYellow(self):
        colors = ['orange', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(334, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeGreen(self):
        colors = ['orange', 'orange', 'green', 'brown', 'red']
        self.assertEquals(335, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeBlue(self):
        colors = ['orange', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(336, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeViolet(self):
        colors = ['orange', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(337, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeGrey(self):
        colors = ['orange', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(338, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeOrangeWhite(self):
        colors = ['orange', 'orange', 'white', 'brown', 'red']
        self.assertEquals(339, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowBlack(self):
        colors = ['orange', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(340, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowBrown(self):
        colors = ['orange', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(341, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowRed(self):
        colors = ['orange', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(342, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowOrange(self):
        colors = ['orange', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(343, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowYellow(self):
        colors = ['orange', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(344, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowGreen(self):
        colors = ['orange', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(345, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowBlue(self):
        colors = ['orange', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(346, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowViolet(self):
        colors = ['orange', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(347, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowGrey(self):
        colors = ['orange', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(348, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeYellowWhite(self):
        colors = ['orange', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(349, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenBlack(self):
        colors = ['orange', 'green', 'black', 'brown', 'red']
        self.assertEquals(350, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenBrown(self):
        colors = ['orange', 'green', 'brown', 'brown', 'red']
        self.assertEquals(351, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenRed(self):
        colors = ['orange', 'green', 'red', 'brown', 'red']
        self.assertEquals(352, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenOrange(self):
        colors = ['orange', 'green', 'orange', 'brown', 'red']
        self.assertEquals(353, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenYellow(self):
        colors = ['orange', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(354, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenGreen(self):
        colors = ['orange', 'green', 'green', 'brown', 'red']
        self.assertEquals(355, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenBlue(self):
        colors = ['orange', 'green', 'blue', 'brown', 'red']
        self.assertEquals(356, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenViolet(self):
        colors = ['orange', 'green', 'violet', 'brown', 'red']
        self.assertEquals(357, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenGrey(self):
        colors = ['orange', 'green', 'grey', 'brown', 'red']
        self.assertEquals(358, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreenWhite(self):
        colors = ['orange', 'green', 'white', 'brown', 'red']
        self.assertEquals(359, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueBlack(self):
        colors = ['orange', 'blue', 'black', 'brown', 'red']
        self.assertEquals(360, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueBrown(self):
        colors = ['orange', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(361, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueRed(self):
        colors = ['orange', 'blue', 'red', 'brown', 'red']
        self.assertEquals(362, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueOrange(self):
        colors = ['orange', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(363, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueYellow(self):
        colors = ['orange', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(364, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueGreen(self):
        colors = ['orange', 'blue', 'green', 'brown', 'red']
        self.assertEquals(365, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueBlue(self):
        colors = ['orange', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(366, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueViolet(self):
        colors = ['orange', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(367, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueGrey(self):
        colors = ['orange', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(368, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeBlueWhite(self):
        colors = ['orange', 'blue', 'white', 'brown', 'red']
        self.assertEquals(369, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletBlack(self):
        colors = ['orange', 'violet', 'black', 'brown', 'red']
        self.assertEquals(370, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletBrown(self):
        colors = ['orange', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(371, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletRed(self):
        colors = ['orange', 'violet', 'red', 'brown', 'red']
        self.assertEquals(372, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletOrange(self):
        colors = ['orange', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(373, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletYellow(self):
        colors = ['orange', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(374, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletGreen(self):
        colors = ['orange', 'violet', 'green', 'brown', 'red']
        self.assertEquals(375, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletBlue(self):
        colors = ['orange', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(376, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletViolet(self):
        colors = ['orange', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(377, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletGrey(self):
        colors = ['orange', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(378, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeVioletWhite(self):
        colors = ['orange', 'violet', 'white', 'brown', 'red']
        self.assertEquals(379, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyBlack(self):
        colors = ['orange', 'grey', 'black', 'brown', 'red']
        self.assertEquals(380, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyBrown(self):
        colors = ['orange', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(381, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyRed(self):
        colors = ['orange', 'grey', 'red', 'brown', 'red']
        self.assertEquals(382, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyOrange(self):
        colors = ['orange', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(383, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyYellow(self):
        colors = ['orange', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(384, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyGreen(self):
        colors = ['orange', 'grey', 'green', 'brown', 'red']
        self.assertEquals(385, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyBlue(self):
        colors = ['orange', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(386, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyViolet(self):
        colors = ['orange', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(387, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyGrey(self):
        colors = ['orange', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(388, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeGreyWhite(self):
        colors = ['orange', 'grey', 'white', 'brown', 'red']
        self.assertEquals(389, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteBlack(self):
        colors = ['orange', 'white', 'black', 'brown', 'red']
        self.assertEquals(390, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteBrown(self):
        colors = ['orange', 'white', 'brown', 'brown', 'red']
        self.assertEquals(391, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteRed(self):
        colors = ['orange', 'white', 'red', 'brown', 'red']
        self.assertEquals(392, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteOrange(self):
        colors = ['orange', 'white', 'orange', 'brown', 'red']
        self.assertEquals(393, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteYellow(self):
        colors = ['orange', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(394, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteGreen(self):
        colors = ['orange', 'white', 'green', 'brown', 'red']
        self.assertEquals(395, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteBlue(self):
        colors = ['orange', 'white', 'blue', 'brown', 'red']
        self.assertEquals(396, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteViolet(self):
        colors = ['orange', 'white', 'violet', 'brown', 'red']
        self.assertEquals(397, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteGrey(self):
        colors = ['orange', 'white', 'grey', 'brown', 'red']
        self.assertEquals(398, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithOrangeWhiteWhite(self):
        colors = ['orange', 'white', 'white', 'brown', 'red']
        self.assertEquals(399, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackBlack(self):
        colors = ['yellow', 'black', 'black', 'brown', 'red']
        self.assertEquals(400, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackBrown(self):
        colors = ['yellow', 'black', 'brown', 'brown', 'red']
        self.assertEquals(401, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackRed(self):
        colors = ['yellow', 'black', 'red', 'brown', 'red']
        self.assertEquals(402, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackOrange(self):
        colors = ['yellow', 'black', 'orange', 'brown', 'red']
        self.assertEquals(403, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackYellow(self):
        colors = ['yellow', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(404, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackGreen(self):
        colors = ['yellow', 'black', 'green', 'brown', 'red']
        self.assertEquals(405, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackBlue(self):
        colors = ['yellow', 'black', 'blue', 'brown', 'red']
        self.assertEquals(406, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackViolet(self):
        colors = ['yellow', 'black', 'violet', 'brown', 'red']
        self.assertEquals(407, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackGrey(self):
        colors = ['yellow', 'black', 'grey', 'brown', 'red']
        self.assertEquals(408, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlackWhite(self):
        colors = ['yellow', 'black', 'white', 'brown', 'red']
        self.assertEquals(409, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownBlack(self):
        colors = ['yellow', 'brown', 'black', 'brown', 'red']
        self.assertEquals(410, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownBrown(self):
        colors = ['yellow', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(411, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownRed(self):
        colors = ['yellow', 'brown', 'red', 'brown', 'red']
        self.assertEquals(412, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownOrange(self):
        colors = ['yellow', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(413, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownYellow(self):
        colors = ['yellow', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(414, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownGreen(self):
        colors = ['yellow', 'brown', 'green', 'brown', 'red']
        self.assertEquals(415, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownBlue(self):
        colors = ['yellow', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(416, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownViolet(self):
        colors = ['yellow', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(417, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownGrey(self):
        colors = ['yellow', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(418, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBrownWhite(self):
        colors = ['yellow', 'brown', 'white', 'brown', 'red']
        self.assertEquals(419, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedBlack(self):
        colors = ['yellow', 'red', 'black', 'brown', 'red']
        self.assertEquals(420, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedBrown(self):
        colors = ['yellow', 'red', 'brown', 'brown', 'red']
        self.assertEquals(421, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedRed(self):
        colors = ['yellow', 'red', 'red', 'brown', 'red']
        self.assertEquals(422, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedOrange(self):
        colors = ['yellow', 'red', 'orange', 'brown', 'red']
        self.assertEquals(423, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedYellow(self):
        colors = ['yellow', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(424, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedGreen(self):
        colors = ['yellow', 'red', 'green', 'brown', 'red']
        self.assertEquals(425, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedBlue(self):
        colors = ['yellow', 'red', 'blue', 'brown', 'red']
        self.assertEquals(426, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedViolet(self):
        colors = ['yellow', 'red', 'violet', 'brown', 'red']
        self.assertEquals(427, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedGrey(self):
        colors = ['yellow', 'red', 'grey', 'brown', 'red']
        self.assertEquals(428, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowRedWhite(self):
        colors = ['yellow', 'red', 'white', 'brown', 'red']
        self.assertEquals(429, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeBlack(self):
        colors = ['yellow', 'orange', 'black', 'brown', 'red']
        self.assertEquals(430, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeBrown(self):
        colors = ['yellow', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(431, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeRed(self):
        colors = ['yellow', 'orange', 'red', 'brown', 'red']
        self.assertEquals(432, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeOrange(self):
        colors = ['yellow', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(433, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeYellow(self):
        colors = ['yellow', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(434, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeGreen(self):
        colors = ['yellow', 'orange', 'green', 'brown', 'red']
        self.assertEquals(435, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeBlue(self):
        colors = ['yellow', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(436, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeViolet(self):
        colors = ['yellow', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(437, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeGrey(self):
        colors = ['yellow', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(438, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowOrangeWhite(self):
        colors = ['yellow', 'orange', 'white', 'brown', 'red']
        self.assertEquals(439, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowBlack(self):
        colors = ['yellow', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(440, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowBrown(self):
        colors = ['yellow', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(441, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowRed(self):
        colors = ['yellow', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(442, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowOrange(self):
        colors = ['yellow', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(443, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowYellow(self):
        colors = ['yellow', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(444, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowGreen(self):
        colors = ['yellow', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(445, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowBlue(self):
        colors = ['yellow', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(446, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowViolet(self):
        colors = ['yellow', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(447, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowGrey(self):
        colors = ['yellow', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(448, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowYellowWhite(self):
        colors = ['yellow', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(449, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenBlack(self):
        colors = ['yellow', 'green', 'black', 'brown', 'red']
        self.assertEquals(450, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenBrown(self):
        colors = ['yellow', 'green', 'brown', 'brown', 'red']
        self.assertEquals(451, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenRed(self):
        colors = ['yellow', 'green', 'red', 'brown', 'red']
        self.assertEquals(452, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenOrange(self):
        colors = ['yellow', 'green', 'orange', 'brown', 'red']
        self.assertEquals(453, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenYellow(self):
        colors = ['yellow', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(454, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenGreen(self):
        colors = ['yellow', 'green', 'green', 'brown', 'red']
        self.assertEquals(455, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenBlue(self):
        colors = ['yellow', 'green', 'blue', 'brown', 'red']
        self.assertEquals(456, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenViolet(self):
        colors = ['yellow', 'green', 'violet', 'brown', 'red']
        self.assertEquals(457, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenGrey(self):
        colors = ['yellow', 'green', 'grey', 'brown', 'red']
        self.assertEquals(458, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreenWhite(self):
        colors = ['yellow', 'green', 'white', 'brown', 'red']
        self.assertEquals(459, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueBlack(self):
        colors = ['yellow', 'blue', 'black', 'brown', 'red']
        self.assertEquals(460, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueBrown(self):
        colors = ['yellow', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(461, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueRed(self):
        colors = ['yellow', 'blue', 'red', 'brown', 'red']
        self.assertEquals(462, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueOrange(self):
        colors = ['yellow', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(463, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueYellow(self):
        colors = ['yellow', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(464, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueGreen(self):
        colors = ['yellow', 'blue', 'green', 'brown', 'red']
        self.assertEquals(465, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueBlue(self):
        colors = ['yellow', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(466, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueViolet(self):
        colors = ['yellow', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(467, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueGrey(self):
        colors = ['yellow', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(468, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowBlueWhite(self):
        colors = ['yellow', 'blue', 'white', 'brown', 'red']
        self.assertEquals(469, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletBlack(self):
        colors = ['yellow', 'violet', 'black', 'brown', 'red']
        self.assertEquals(470, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletBrown(self):
        colors = ['yellow', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(471, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletRed(self):
        colors = ['yellow', 'violet', 'red', 'brown', 'red']
        self.assertEquals(472, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletOrange(self):
        colors = ['yellow', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(473, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletYellow(self):
        colors = ['yellow', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(474, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletGreen(self):
        colors = ['yellow', 'violet', 'green', 'brown', 'red']
        self.assertEquals(475, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletBlue(self):
        colors = ['yellow', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(476, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletViolet(self):
        colors = ['yellow', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(477, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletGrey(self):
        colors = ['yellow', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(478, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowVioletWhite(self):
        colors = ['yellow', 'violet', 'white', 'brown', 'red']
        self.assertEquals(479, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyBlack(self):
        colors = ['yellow', 'grey', 'black', 'brown', 'red']
        self.assertEquals(480, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyBrown(self):
        colors = ['yellow', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(481, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyRed(self):
        colors = ['yellow', 'grey', 'red', 'brown', 'red']
        self.assertEquals(482, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyOrange(self):
        colors = ['yellow', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(483, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyYellow(self):
        colors = ['yellow', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(484, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyGreen(self):
        colors = ['yellow', 'grey', 'green', 'brown', 'red']
        self.assertEquals(485, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyBlue(self):
        colors = ['yellow', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(486, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyViolet(self):
        colors = ['yellow', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(487, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyGrey(self):
        colors = ['yellow', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(488, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowGreyWhite(self):
        colors = ['yellow', 'grey', 'white', 'brown', 'red']
        self.assertEquals(489, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteBlack(self):
        colors = ['yellow', 'white', 'black', 'brown', 'red']
        self.assertEquals(490, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteBrown(self):
        colors = ['yellow', 'white', 'brown', 'brown', 'red']
        self.assertEquals(491, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteRed(self):
        colors = ['yellow', 'white', 'red', 'brown', 'red']
        self.assertEquals(492, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteOrange(self):
        colors = ['yellow', 'white', 'orange', 'brown', 'red']
        self.assertEquals(493, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteYellow(self):
        colors = ['yellow', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(494, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteGreen(self):
        colors = ['yellow', 'white', 'green', 'brown', 'red']
        self.assertEquals(495, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteBlue(self):
        colors = ['yellow', 'white', 'blue', 'brown', 'red']
        self.assertEquals(496, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteViolet(self):
        colors = ['yellow', 'white', 'violet', 'brown', 'red']
        self.assertEquals(497, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteGrey(self):
        colors = ['yellow', 'white', 'grey', 'brown', 'red']
        self.assertEquals(498, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithYellowWhiteWhite(self):
        colors = ['yellow', 'white', 'white', 'brown', 'red']
        self.assertEquals(499, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackBlack(self):
        colors = ['green', 'black', 'black', 'brown', 'red']
        self.assertEquals(500, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackBrown(self):
        colors = ['green', 'black', 'brown', 'brown', 'red']
        self.assertEquals(501, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackRed(self):
        colors = ['green', 'black', 'red', 'brown', 'red']
        self.assertEquals(502, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackOrange(self):
        colors = ['green', 'black', 'orange', 'brown', 'red']
        self.assertEquals(503, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackYellow(self):
        colors = ['green', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(504, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackGreen(self):
        colors = ['green', 'black', 'green', 'brown', 'red']
        self.assertEquals(505, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackBlue(self):
        colors = ['green', 'black', 'blue', 'brown', 'red']
        self.assertEquals(506, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackViolet(self):
        colors = ['green', 'black', 'violet', 'brown', 'red']
        self.assertEquals(507, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackGrey(self):
        colors = ['green', 'black', 'grey', 'brown', 'red']
        self.assertEquals(508, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlackWhite(self):
        colors = ['green', 'black', 'white', 'brown', 'red']
        self.assertEquals(509, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownBlack(self):
        colors = ['green', 'brown', 'black', 'brown', 'red']
        self.assertEquals(510, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownBrown(self):
        colors = ['green', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(511, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownRed(self):
        colors = ['green', 'brown', 'red', 'brown', 'red']
        self.assertEquals(512, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownOrange(self):
        colors = ['green', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(513, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownYellow(self):
        colors = ['green', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(514, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownGreen(self):
        colors = ['green', 'brown', 'green', 'brown', 'red']
        self.assertEquals(515, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownBlue(self):
        colors = ['green', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(516, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownViolet(self):
        colors = ['green', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(517, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownGrey(self):
        colors = ['green', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(518, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBrownWhite(self):
        colors = ['green', 'brown', 'white', 'brown', 'red']
        self.assertEquals(519, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedBlack(self):
        colors = ['green', 'red', 'black', 'brown', 'red']
        self.assertEquals(520, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedBrown(self):
        colors = ['green', 'red', 'brown', 'brown', 'red']
        self.assertEquals(521, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedRed(self):
        colors = ['green', 'red', 'red', 'brown', 'red']
        self.assertEquals(522, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedOrange(self):
        colors = ['green', 'red', 'orange', 'brown', 'red']
        self.assertEquals(523, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedYellow(self):
        colors = ['green', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(524, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedGreen(self):
        colors = ['green', 'red', 'green', 'brown', 'red']
        self.assertEquals(525, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedBlue(self):
        colors = ['green', 'red', 'blue', 'brown', 'red']
        self.assertEquals(526, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedViolet(self):
        colors = ['green', 'red', 'violet', 'brown', 'red']
        self.assertEquals(527, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedGrey(self):
        colors = ['green', 'red', 'grey', 'brown', 'red']
        self.assertEquals(528, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenRedWhite(self):
        colors = ['green', 'red', 'white', 'brown', 'red']
        self.assertEquals(529, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeBlack(self):
        colors = ['green', 'orange', 'black', 'brown', 'red']
        self.assertEquals(530, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeBrown(self):
        colors = ['green', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(531, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeRed(self):
        colors = ['green', 'orange', 'red', 'brown', 'red']
        self.assertEquals(532, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeOrange(self):
        colors = ['green', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(533, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeYellow(self):
        colors = ['green', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(534, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeGreen(self):
        colors = ['green', 'orange', 'green', 'brown', 'red']
        self.assertEquals(535, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeBlue(self):
        colors = ['green', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(536, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeViolet(self):
        colors = ['green', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(537, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeGrey(self):
        colors = ['green', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(538, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenOrangeWhite(self):
        colors = ['green', 'orange', 'white', 'brown', 'red']
        self.assertEquals(539, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowBlack(self):
        colors = ['green', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(540, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowBrown(self):
        colors = ['green', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(541, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowRed(self):
        colors = ['green', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(542, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowOrange(self):
        colors = ['green', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(543, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowYellow(self):
        colors = ['green', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(544, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowGreen(self):
        colors = ['green', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(545, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowBlue(self):
        colors = ['green', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(546, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowViolet(self):
        colors = ['green', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(547, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowGrey(self):
        colors = ['green', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(548, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenYellowWhite(self):
        colors = ['green', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(549, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenBlack(self):
        colors = ['green', 'green', 'black', 'brown', 'red']
        self.assertEquals(550, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenBrown(self):
        colors = ['green', 'green', 'brown', 'brown', 'red']
        self.assertEquals(551, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenRed(self):
        colors = ['green', 'green', 'red', 'brown', 'red']
        self.assertEquals(552, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenOrange(self):
        colors = ['green', 'green', 'orange', 'brown', 'red']
        self.assertEquals(553, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenYellow(self):
        colors = ['green', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(554, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenGreen(self):
        colors = ['green', 'green', 'green', 'brown', 'red']
        self.assertEquals(555, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenBlue(self):
        colors = ['green', 'green', 'blue', 'brown', 'red']
        self.assertEquals(556, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenViolet(self):
        colors = ['green', 'green', 'violet', 'brown', 'red']
        self.assertEquals(557, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenGrey(self):
        colors = ['green', 'green', 'grey', 'brown', 'red']
        self.assertEquals(558, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreenWhite(self):
        colors = ['green', 'green', 'white', 'brown', 'red']
        self.assertEquals(559, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueBlack(self):
        colors = ['green', 'blue', 'black', 'brown', 'red']
        self.assertEquals(560, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueBrown(self):
        colors = ['green', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(561, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueRed(self):
        colors = ['green', 'blue', 'red', 'brown', 'red']
        self.assertEquals(562, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueOrange(self):
        colors = ['green', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(563, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueYellow(self):
        colors = ['green', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(564, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueGreen(self):
        colors = ['green', 'blue', 'green', 'brown', 'red']
        self.assertEquals(565, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueBlue(self):
        colors = ['green', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(566, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueViolet(self):
        colors = ['green', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(567, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueGrey(self):
        colors = ['green', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(568, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenBlueWhite(self):
        colors = ['green', 'blue', 'white', 'brown', 'red']
        self.assertEquals(569, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletBlack(self):
        colors = ['green', 'violet', 'black', 'brown', 'red']
        self.assertEquals(570, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletBrown(self):
        colors = ['green', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(571, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletRed(self):
        colors = ['green', 'violet', 'red', 'brown', 'red']
        self.assertEquals(572, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletOrange(self):
        colors = ['green', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(573, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletYellow(self):
        colors = ['green', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(574, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletGreen(self):
        colors = ['green', 'violet', 'green', 'brown', 'red']
        self.assertEquals(575, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletBlue(self):
        colors = ['green', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(576, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletViolet(self):
        colors = ['green', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(577, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletGrey(self):
        colors = ['green', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(578, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenVioletWhite(self):
        colors = ['green', 'violet', 'white', 'brown', 'red']
        self.assertEquals(579, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyBlack(self):
        colors = ['green', 'grey', 'black', 'brown', 'red']
        self.assertEquals(580, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyBrown(self):
        colors = ['green', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(581, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyRed(self):
        colors = ['green', 'grey', 'red', 'brown', 'red']
        self.assertEquals(582, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyOrange(self):
        colors = ['green', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(583, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyYellow(self):
        colors = ['green', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(584, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyGreen(self):
        colors = ['green', 'grey', 'green', 'brown', 'red']
        self.assertEquals(585, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyBlue(self):
        colors = ['green', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(586, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyViolet(self):
        colors = ['green', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(587, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyGrey(self):
        colors = ['green', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(588, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenGreyWhite(self):
        colors = ['green', 'grey', 'white', 'brown', 'red']
        self.assertEquals(589, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteBlack(self):
        colors = ['green', 'white', 'black', 'brown', 'red']
        self.assertEquals(590, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteBrown(self):
        colors = ['green', 'white', 'brown', 'brown', 'red']
        self.assertEquals(591, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteRed(self):
        colors = ['green', 'white', 'red', 'brown', 'red']
        self.assertEquals(592, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteOrange(self):
        colors = ['green', 'white', 'orange', 'brown', 'red']
        self.assertEquals(593, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteYellow(self):
        colors = ['green', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(594, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteGreen(self):
        colors = ['green', 'white', 'green', 'brown', 'red']
        self.assertEquals(595, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteBlue(self):
        colors = ['green', 'white', 'blue', 'brown', 'red']
        self.assertEquals(596, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteViolet(self):
        colors = ['green', 'white', 'violet', 'brown', 'red']
        self.assertEquals(597, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteGrey(self):
        colors = ['green', 'white', 'grey', 'brown', 'red']
        self.assertEquals(598, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreenWhiteWhite(self):
        colors = ['green', 'white', 'white', 'brown', 'red']
        self.assertEquals(599, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackBlack(self):
        colors = ['blue', 'black', 'black', 'brown', 'red']
        self.assertEquals(600, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackBrown(self):
        colors = ['blue', 'black', 'brown', 'brown', 'red']
        self.assertEquals(601, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackRed(self):
        colors = ['blue', 'black', 'red', 'brown', 'red']
        self.assertEquals(602, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackOrange(self):
        colors = ['blue', 'black', 'orange', 'brown', 'red']
        self.assertEquals(603, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackYellow(self):
        colors = ['blue', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(604, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackGreen(self):
        colors = ['blue', 'black', 'green', 'brown', 'red']
        self.assertEquals(605, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackBlue(self):
        colors = ['blue', 'black', 'blue', 'brown', 'red']
        self.assertEquals(606, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackViolet(self):
        colors = ['blue', 'black', 'violet', 'brown', 'red']
        self.assertEquals(607, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackGrey(self):
        colors = ['blue', 'black', 'grey', 'brown', 'red']
        self.assertEquals(608, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlackWhite(self):
        colors = ['blue', 'black', 'white', 'brown', 'red']
        self.assertEquals(609, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownBlack(self):
        colors = ['blue', 'brown', 'black', 'brown', 'red']
        self.assertEquals(610, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownBrown(self):
        colors = ['blue', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(611, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownRed(self):
        colors = ['blue', 'brown', 'red', 'brown', 'red']
        self.assertEquals(612, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownOrange(self):
        colors = ['blue', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(613, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownYellow(self):
        colors = ['blue', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(614, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownGreen(self):
        colors = ['blue', 'brown', 'green', 'brown', 'red']
        self.assertEquals(615, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownBlue(self):
        colors = ['blue', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(616, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownViolet(self):
        colors = ['blue', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(617, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownGrey(self):
        colors = ['blue', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(618, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBrownWhite(self):
        colors = ['blue', 'brown', 'white', 'brown', 'red']
        self.assertEquals(619, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedBlack(self):
        colors = ['blue', 'red', 'black', 'brown', 'red']
        self.assertEquals(620, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedBrown(self):
        colors = ['blue', 'red', 'brown', 'brown', 'red']
        self.assertEquals(621, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedRed(self):
        colors = ['blue', 'red', 'red', 'brown', 'red']
        self.assertEquals(622, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedOrange(self):
        colors = ['blue', 'red', 'orange', 'brown', 'red']
        self.assertEquals(623, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedYellow(self):
        colors = ['blue', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(624, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedGreen(self):
        colors = ['blue', 'red', 'green', 'brown', 'red']
        self.assertEquals(625, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedBlue(self):
        colors = ['blue', 'red', 'blue', 'brown', 'red']
        self.assertEquals(626, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedViolet(self):
        colors = ['blue', 'red', 'violet', 'brown', 'red']
        self.assertEquals(627, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedGrey(self):
        colors = ['blue', 'red', 'grey', 'brown', 'red']
        self.assertEquals(628, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueRedWhite(self):
        colors = ['blue', 'red', 'white', 'brown', 'red']
        self.assertEquals(629, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeBlack(self):
        colors = ['blue', 'orange', 'black', 'brown', 'red']
        self.assertEquals(630, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeBrown(self):
        colors = ['blue', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(631, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeRed(self):
        colors = ['blue', 'orange', 'red', 'brown', 'red']
        self.assertEquals(632, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeOrange(self):
        colors = ['blue', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(633, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeYellow(self):
        colors = ['blue', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(634, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeGreen(self):
        colors = ['blue', 'orange', 'green', 'brown', 'red']
        self.assertEquals(635, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeBlue(self):
        colors = ['blue', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(636, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeViolet(self):
        colors = ['blue', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(637, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeGrey(self):
        colors = ['blue', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(638, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueOrangeWhite(self):
        colors = ['blue', 'orange', 'white', 'brown', 'red']
        self.assertEquals(639, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowBlack(self):
        colors = ['blue', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(640, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowBrown(self):
        colors = ['blue', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(641, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowRed(self):
        colors = ['blue', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(642, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowOrange(self):
        colors = ['blue', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(643, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowYellow(self):
        colors = ['blue', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(644, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowGreen(self):
        colors = ['blue', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(645, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowBlue(self):
        colors = ['blue', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(646, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowViolet(self):
        colors = ['blue', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(647, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowGrey(self):
        colors = ['blue', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(648, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueYellowWhite(self):
        colors = ['blue', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(649, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenBlack(self):
        colors = ['blue', 'green', 'black', 'brown', 'red']
        self.assertEquals(650, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenBrown(self):
        colors = ['blue', 'green', 'brown', 'brown', 'red']
        self.assertEquals(651, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenRed(self):
        colors = ['blue', 'green', 'red', 'brown', 'red']
        self.assertEquals(652, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenOrange(self):
        colors = ['blue', 'green', 'orange', 'brown', 'red']
        self.assertEquals(653, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenYellow(self):
        colors = ['blue', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(654, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenGreen(self):
        colors = ['blue', 'green', 'green', 'brown', 'red']
        self.assertEquals(655, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenBlue(self):
        colors = ['blue', 'green', 'blue', 'brown', 'red']
        self.assertEquals(656, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenViolet(self):
        colors = ['blue', 'green', 'violet', 'brown', 'red']
        self.assertEquals(657, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenGrey(self):
        colors = ['blue', 'green', 'grey', 'brown', 'red']
        self.assertEquals(658, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreenWhite(self):
        colors = ['blue', 'green', 'white', 'brown', 'red']
        self.assertEquals(659, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueBlack(self):
        colors = ['blue', 'blue', 'black', 'brown', 'red']
        self.assertEquals(660, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueBrown(self):
        colors = ['blue', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(661, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueRed(self):
        colors = ['blue', 'blue', 'red', 'brown', 'red']
        self.assertEquals(662, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueOrange(self):
        colors = ['blue', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(663, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueYellow(self):
        colors = ['blue', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(664, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueGreen(self):
        colors = ['blue', 'blue', 'green', 'brown', 'red']
        self.assertEquals(665, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueBlue(self):
        colors = ['blue', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(666, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueViolet(self):
        colors = ['blue', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(667, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueGrey(self):
        colors = ['blue', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(668, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueBlueWhite(self):
        colors = ['blue', 'blue', 'white', 'brown', 'red']
        self.assertEquals(669, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletBlack(self):
        colors = ['blue', 'violet', 'black', 'brown', 'red']
        self.assertEquals(670, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletBrown(self):
        colors = ['blue', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(671, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletRed(self):
        colors = ['blue', 'violet', 'red', 'brown', 'red']
        self.assertEquals(672, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletOrange(self):
        colors = ['blue', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(673, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletYellow(self):
        colors = ['blue', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(674, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletGreen(self):
        colors = ['blue', 'violet', 'green', 'brown', 'red']
        self.assertEquals(675, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletBlue(self):
        colors = ['blue', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(676, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletViolet(self):
        colors = ['blue', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(677, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletGrey(self):
        colors = ['blue', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(678, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueVioletWhite(self):
        colors = ['blue', 'violet', 'white', 'brown', 'red']
        self.assertEquals(679, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyBlack(self):
        colors = ['blue', 'grey', 'black', 'brown', 'red']
        self.assertEquals(680, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyBrown(self):
        colors = ['blue', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(681, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyRed(self):
        colors = ['blue', 'grey', 'red', 'brown', 'red']
        self.assertEquals(682, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyOrange(self):
        colors = ['blue', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(683, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyYellow(self):
        colors = ['blue', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(684, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyGreen(self):
        colors = ['blue', 'grey', 'green', 'brown', 'red']
        self.assertEquals(685, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyBlue(self):
        colors = ['blue', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(686, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyViolet(self):
        colors = ['blue', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(687, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyGrey(self):
        colors = ['blue', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(688, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueGreyWhite(self):
        colors = ['blue', 'grey', 'white', 'brown', 'red']
        self.assertEquals(689, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteBlack(self):
        colors = ['blue', 'white', 'black', 'brown', 'red']
        self.assertEquals(690, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteBrown(self):
        colors = ['blue', 'white', 'brown', 'brown', 'red']
        self.assertEquals(691, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteRed(self):
        colors = ['blue', 'white', 'red', 'brown', 'red']
        self.assertEquals(692, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteOrange(self):
        colors = ['blue', 'white', 'orange', 'brown', 'red']
        self.assertEquals(693, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteYellow(self):
        colors = ['blue', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(694, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteGreen(self):
        colors = ['blue', 'white', 'green', 'brown', 'red']
        self.assertEquals(695, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteBlue(self):
        colors = ['blue', 'white', 'blue', 'brown', 'red']
        self.assertEquals(696, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteViolet(self):
        colors = ['blue', 'white', 'violet', 'brown', 'red']
        self.assertEquals(697, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteGrey(self):
        colors = ['blue', 'white', 'grey', 'brown', 'red']
        self.assertEquals(698, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithBlueWhiteWhite(self):
        colors = ['blue', 'white', 'white', 'brown', 'red']
        self.assertEquals(699, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackBlack(self):
        colors = ['violet', 'black', 'black', 'brown', 'red']
        self.assertEquals(700, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackBrown(self):
        colors = ['violet', 'black', 'brown', 'brown', 'red']
        self.assertEquals(701, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackRed(self):
        colors = ['violet', 'black', 'red', 'brown', 'red']
        self.assertEquals(702, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackOrange(self):
        colors = ['violet', 'black', 'orange', 'brown', 'red']
        self.assertEquals(703, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackYellow(self):
        colors = ['violet', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(704, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackGreen(self):
        colors = ['violet', 'black', 'green', 'brown', 'red']
        self.assertEquals(705, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackBlue(self):
        colors = ['violet', 'black', 'blue', 'brown', 'red']
        self.assertEquals(706, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackViolet(self):
        colors = ['violet', 'black', 'violet', 'brown', 'red']
        self.assertEquals(707, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackGrey(self):
        colors = ['violet', 'black', 'grey', 'brown', 'red']
        self.assertEquals(708, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlackWhite(self):
        colors = ['violet', 'black', 'white', 'brown', 'red']
        self.assertEquals(709, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownBlack(self):
        colors = ['violet', 'brown', 'black', 'brown', 'red']
        self.assertEquals(710, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownBrown(self):
        colors = ['violet', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(711, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownRed(self):
        colors = ['violet', 'brown', 'red', 'brown', 'red']
        self.assertEquals(712, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownOrange(self):
        colors = ['violet', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(713, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownYellow(self):
        colors = ['violet', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(714, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownGreen(self):
        colors = ['violet', 'brown', 'green', 'brown', 'red']
        self.assertEquals(715, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownBlue(self):
        colors = ['violet', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(716, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownViolet(self):
        colors = ['violet', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(717, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownGrey(self):
        colors = ['violet', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(718, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBrownWhite(self):
        colors = ['violet', 'brown', 'white', 'brown', 'red']
        self.assertEquals(719, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedBlack(self):
        colors = ['violet', 'red', 'black', 'brown', 'red']
        self.assertEquals(720, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedBrown(self):
        colors = ['violet', 'red', 'brown', 'brown', 'red']
        self.assertEquals(721, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedRed(self):
        colors = ['violet', 'red', 'red', 'brown', 'red']
        self.assertEquals(722, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedOrange(self):
        colors = ['violet', 'red', 'orange', 'brown', 'red']
        self.assertEquals(723, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedYellow(self):
        colors = ['violet', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(724, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedGreen(self):
        colors = ['violet', 'red', 'green', 'brown', 'red']
        self.assertEquals(725, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedBlue(self):
        colors = ['violet', 'red', 'blue', 'brown', 'red']
        self.assertEquals(726, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedViolet(self):
        colors = ['violet', 'red', 'violet', 'brown', 'red']
        self.assertEquals(727, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedGrey(self):
        colors = ['violet', 'red', 'grey', 'brown', 'red']
        self.assertEquals(728, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletRedWhite(self):
        colors = ['violet', 'red', 'white', 'brown', 'red']
        self.assertEquals(729, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeBlack(self):
        colors = ['violet', 'orange', 'black', 'brown', 'red']
        self.assertEquals(730, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeBrown(self):
        colors = ['violet', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(731, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeRed(self):
        colors = ['violet', 'orange', 'red', 'brown', 'red']
        self.assertEquals(732, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeOrange(self):
        colors = ['violet', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(733, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeYellow(self):
        colors = ['violet', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(734, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeGreen(self):
        colors = ['violet', 'orange', 'green', 'brown', 'red']
        self.assertEquals(735, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeBlue(self):
        colors = ['violet', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(736, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeViolet(self):
        colors = ['violet', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(737, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeGrey(self):
        colors = ['violet', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(738, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletOrangeWhite(self):
        colors = ['violet', 'orange', 'white', 'brown', 'red']
        self.assertEquals(739, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowBlack(self):
        colors = ['violet', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(740, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowBrown(self):
        colors = ['violet', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(741, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowRed(self):
        colors = ['violet', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(742, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowOrange(self):
        colors = ['violet', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(743, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowYellow(self):
        colors = ['violet', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(744, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowGreen(self):
        colors = ['violet', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(745, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowBlue(self):
        colors = ['violet', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(746, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowViolet(self):
        colors = ['violet', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(747, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowGrey(self):
        colors = ['violet', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(748, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletYellowWhite(self):
        colors = ['violet', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(749, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenBlack(self):
        colors = ['violet', 'green', 'black', 'brown', 'red']
        self.assertEquals(750, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenBrown(self):
        colors = ['violet', 'green', 'brown', 'brown', 'red']
        self.assertEquals(751, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenRed(self):
        colors = ['violet', 'green', 'red', 'brown', 'red']
        self.assertEquals(752, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenOrange(self):
        colors = ['violet', 'green', 'orange', 'brown', 'red']
        self.assertEquals(753, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenYellow(self):
        colors = ['violet', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(754, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenGreen(self):
        colors = ['violet', 'green', 'green', 'brown', 'red']
        self.assertEquals(755, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenBlue(self):
        colors = ['violet', 'green', 'blue', 'brown', 'red']
        self.assertEquals(756, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenViolet(self):
        colors = ['violet', 'green', 'violet', 'brown', 'red']
        self.assertEquals(757, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenGrey(self):
        colors = ['violet', 'green', 'grey', 'brown', 'red']
        self.assertEquals(758, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreenWhite(self):
        colors = ['violet', 'green', 'white', 'brown', 'red']
        self.assertEquals(759, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueBlack(self):
        colors = ['violet', 'blue', 'black', 'brown', 'red']
        self.assertEquals(760, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueBrown(self):
        colors = ['violet', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(761, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueRed(self):
        colors = ['violet', 'blue', 'red', 'brown', 'red']
        self.assertEquals(762, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueOrange(self):
        colors = ['violet', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(763, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueYellow(self):
        colors = ['violet', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(764, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueGreen(self):
        colors = ['violet', 'blue', 'green', 'brown', 'red']
        self.assertEquals(765, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueBlue(self):
        colors = ['violet', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(766, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueViolet(self):
        colors = ['violet', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(767, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueGrey(self):
        colors = ['violet', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(768, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletBlueWhite(self):
        colors = ['violet', 'blue', 'white', 'brown', 'red']
        self.assertEquals(769, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletBlack(self):
        colors = ['violet', 'violet', 'black', 'brown', 'red']
        self.assertEquals(770, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletBrown(self):
        colors = ['violet', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(771, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletRed(self):
        colors = ['violet', 'violet', 'red', 'brown', 'red']
        self.assertEquals(772, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletOrange(self):
        colors = ['violet', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(773, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletYellow(self):
        colors = ['violet', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(774, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletGreen(self):
        colors = ['violet', 'violet', 'green', 'brown', 'red']
        self.assertEquals(775, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletBlue(self):
        colors = ['violet', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(776, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletViolet(self):
        colors = ['violet', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(777, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletGrey(self):
        colors = ['violet', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(778, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletVioletWhite(self):
        colors = ['violet', 'violet', 'white', 'brown', 'red']
        self.assertEquals(779, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyBlack(self):
        colors = ['violet', 'grey', 'black', 'brown', 'red']
        self.assertEquals(780, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyBrown(self):
        colors = ['violet', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(781, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyRed(self):
        colors = ['violet', 'grey', 'red', 'brown', 'red']
        self.assertEquals(782, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyOrange(self):
        colors = ['violet', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(783, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyYellow(self):
        colors = ['violet', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(784, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyGreen(self):
        colors = ['violet', 'grey', 'green', 'brown', 'red']
        self.assertEquals(785, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyBlue(self):
        colors = ['violet', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(786, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyViolet(self):
        colors = ['violet', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(787, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyGrey(self):
        colors = ['violet', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(788, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletGreyWhite(self):
        colors = ['violet', 'grey', 'white', 'brown', 'red']
        self.assertEquals(789, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteBlack(self):
        colors = ['violet', 'white', 'black', 'brown', 'red']
        self.assertEquals(790, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteBrown(self):
        colors = ['violet', 'white', 'brown', 'brown', 'red']
        self.assertEquals(791, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteRed(self):
        colors = ['violet', 'white', 'red', 'brown', 'red']
        self.assertEquals(792, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteOrange(self):
        colors = ['violet', 'white', 'orange', 'brown', 'red']
        self.assertEquals(793, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteYellow(self):
        colors = ['violet', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(794, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteGreen(self):
        colors = ['violet', 'white', 'green', 'brown', 'red']
        self.assertEquals(795, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteBlue(self):
        colors = ['violet', 'white', 'blue', 'brown', 'red']
        self.assertEquals(796, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteViolet(self):
        colors = ['violet', 'white', 'violet', 'brown', 'red']
        self.assertEquals(797, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteGrey(self):
        colors = ['violet', 'white', 'grey', 'brown', 'red']
        self.assertEquals(798, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithVioletWhiteWhite(self):
        colors = ['violet', 'white', 'white', 'brown', 'red']
        self.assertEquals(799, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackBlack(self):
        colors = ['grey', 'black', 'black', 'brown', 'red']
        self.assertEquals(800, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackBrown(self):
        colors = ['grey', 'black', 'brown', 'brown', 'red']
        self.assertEquals(801, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackRed(self):
        colors = ['grey', 'black', 'red', 'brown', 'red']
        self.assertEquals(802, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackOrange(self):
        colors = ['grey', 'black', 'orange', 'brown', 'red']
        self.assertEquals(803, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackYellow(self):
        colors = ['grey', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(804, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackGreen(self):
        colors = ['grey', 'black', 'green', 'brown', 'red']
        self.assertEquals(805, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackBlue(self):
        colors = ['grey', 'black', 'blue', 'brown', 'red']
        self.assertEquals(806, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackViolet(self):
        colors = ['grey', 'black', 'violet', 'brown', 'red']
        self.assertEquals(807, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackGrey(self):
        colors = ['grey', 'black', 'grey', 'brown', 'red']
        self.assertEquals(808, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlackWhite(self):
        colors = ['grey', 'black', 'white', 'brown', 'red']
        self.assertEquals(809, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownBlack(self):
        colors = ['grey', 'brown', 'black', 'brown', 'red']
        self.assertEquals(810, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownBrown(self):
        colors = ['grey', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(811, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownRed(self):
        colors = ['grey', 'brown', 'red', 'brown', 'red']
        self.assertEquals(812, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownOrange(self):
        colors = ['grey', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(813, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownYellow(self):
        colors = ['grey', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(814, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownGreen(self):
        colors = ['grey', 'brown', 'green', 'brown', 'red']
        self.assertEquals(815, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownBlue(self):
        colors = ['grey', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(816, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownViolet(self):
        colors = ['grey', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(817, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownGrey(self):
        colors = ['grey', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(818, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBrownWhite(self):
        colors = ['grey', 'brown', 'white', 'brown', 'red']
        self.assertEquals(819, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedBlack(self):
        colors = ['grey', 'red', 'black', 'brown', 'red']
        self.assertEquals(820, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedBrown(self):
        colors = ['grey', 'red', 'brown', 'brown', 'red']
        self.assertEquals(821, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedRed(self):
        colors = ['grey', 'red', 'red', 'brown', 'red']
        self.assertEquals(822, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedOrange(self):
        colors = ['grey', 'red', 'orange', 'brown', 'red']
        self.assertEquals(823, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedYellow(self):
        colors = ['grey', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(824, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedGreen(self):
        colors = ['grey', 'red', 'green', 'brown', 'red']
        self.assertEquals(825, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedBlue(self):
        colors = ['grey', 'red', 'blue', 'brown', 'red']
        self.assertEquals(826, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedViolet(self):
        colors = ['grey', 'red', 'violet', 'brown', 'red']
        self.assertEquals(827, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedGrey(self):
        colors = ['grey', 'red', 'grey', 'brown', 'red']
        self.assertEquals(828, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyRedWhite(self):
        colors = ['grey', 'red', 'white', 'brown', 'red']
        self.assertEquals(829, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeBlack(self):
        colors = ['grey', 'orange', 'black', 'brown', 'red']
        self.assertEquals(830, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeBrown(self):
        colors = ['grey', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(831, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeRed(self):
        colors = ['grey', 'orange', 'red', 'brown', 'red']
        self.assertEquals(832, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeOrange(self):
        colors = ['grey', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(833, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeYellow(self):
        colors = ['grey', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(834, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeGreen(self):
        colors = ['grey', 'orange', 'green', 'brown', 'red']
        self.assertEquals(835, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeBlue(self):
        colors = ['grey', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(836, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeViolet(self):
        colors = ['grey', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(837, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeGrey(self):
        colors = ['grey', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(838, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyOrangeWhite(self):
        colors = ['grey', 'orange', 'white', 'brown', 'red']
        self.assertEquals(839, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowBlack(self):
        colors = ['grey', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(840, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowBrown(self):
        colors = ['grey', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(841, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowRed(self):
        colors = ['grey', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(842, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowOrange(self):
        colors = ['grey', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(843, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowYellow(self):
        colors = ['grey', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(844, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowGreen(self):
        colors = ['grey', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(845, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowBlue(self):
        colors = ['grey', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(846, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowViolet(self):
        colors = ['grey', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(847, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowGrey(self):
        colors = ['grey', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(848, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyYellowWhite(self):
        colors = ['grey', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(849, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenBlack(self):
        colors = ['grey', 'green', 'black', 'brown', 'red']
        self.assertEquals(850, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenBrown(self):
        colors = ['grey', 'green', 'brown', 'brown', 'red']
        self.assertEquals(851, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenRed(self):
        colors = ['grey', 'green', 'red', 'brown', 'red']
        self.assertEquals(852, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenOrange(self):
        colors = ['grey', 'green', 'orange', 'brown', 'red']
        self.assertEquals(853, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenYellow(self):
        colors = ['grey', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(854, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenGreen(self):
        colors = ['grey', 'green', 'green', 'brown', 'red']
        self.assertEquals(855, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenBlue(self):
        colors = ['grey', 'green', 'blue', 'brown', 'red']
        self.assertEquals(856, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenViolet(self):
        colors = ['grey', 'green', 'violet', 'brown', 'red']
        self.assertEquals(857, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenGrey(self):
        colors = ['grey', 'green', 'grey', 'brown', 'red']
        self.assertEquals(858, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreenWhite(self):
        colors = ['grey', 'green', 'white', 'brown', 'red']
        self.assertEquals(859, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueBlack(self):
        colors = ['grey', 'blue', 'black', 'brown', 'red']
        self.assertEquals(860, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueBrown(self):
        colors = ['grey', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(861, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueRed(self):
        colors = ['grey', 'blue', 'red', 'brown', 'red']
        self.assertEquals(862, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueOrange(self):
        colors = ['grey', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(863, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueYellow(self):
        colors = ['grey', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(864, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueGreen(self):
        colors = ['grey', 'blue', 'green', 'brown', 'red']
        self.assertEquals(865, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueBlue(self):
        colors = ['grey', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(866, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueViolet(self):
        colors = ['grey', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(867, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueGrey(self):
        colors = ['grey', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(868, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyBlueWhite(self):
        colors = ['grey', 'blue', 'white', 'brown', 'red']
        self.assertEquals(869, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletBlack(self):
        colors = ['grey', 'violet', 'black', 'brown', 'red']
        self.assertEquals(870, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletBrown(self):
        colors = ['grey', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(871, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletRed(self):
        colors = ['grey', 'violet', 'red', 'brown', 'red']
        self.assertEquals(872, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletOrange(self):
        colors = ['grey', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(873, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletYellow(self):
        colors = ['grey', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(874, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletGreen(self):
        colors = ['grey', 'violet', 'green', 'brown', 'red']
        self.assertEquals(875, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletBlue(self):
        colors = ['grey', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(876, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletViolet(self):
        colors = ['grey', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(877, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletGrey(self):
        colors = ['grey', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(878, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyVioletWhite(self):
        colors = ['grey', 'violet', 'white', 'brown', 'red']
        self.assertEquals(879, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyBlack(self):
        colors = ['grey', 'grey', 'black', 'brown', 'red']
        self.assertEquals(880, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyBrown(self):
        colors = ['grey', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(881, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyRed(self):
        colors = ['grey', 'grey', 'red', 'brown', 'red']
        self.assertEquals(882, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyOrange(self):
        colors = ['grey', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(883, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyYellow(self):
        colors = ['grey', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(884, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyGreen(self):
        colors = ['grey', 'grey', 'green', 'brown', 'red']
        self.assertEquals(885, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyBlue(self):
        colors = ['grey', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(886, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyViolet(self):
        colors = ['grey', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(887, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyGrey(self):
        colors = ['grey', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(888, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyGreyWhite(self):
        colors = ['grey', 'grey', 'white', 'brown', 'red']
        self.assertEquals(889, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteBlack(self):
        colors = ['grey', 'white', 'black', 'brown', 'red']
        self.assertEquals(890, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteBrown(self):
        colors = ['grey', 'white', 'brown', 'brown', 'red']
        self.assertEquals(891, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteRed(self):
        colors = ['grey', 'white', 'red', 'brown', 'red']
        self.assertEquals(892, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteOrange(self):
        colors = ['grey', 'white', 'orange', 'brown', 'red']
        self.assertEquals(893, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteYellow(self):
        colors = ['grey', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(894, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteGreen(self):
        colors = ['grey', 'white', 'green', 'brown', 'red']
        self.assertEquals(895, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteBlue(self):
        colors = ['grey', 'white', 'blue', 'brown', 'red']
        self.assertEquals(896, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteViolet(self):
        colors = ['grey', 'white', 'violet', 'brown', 'red']
        self.assertEquals(897, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteGrey(self):
        colors = ['grey', 'white', 'grey', 'brown', 'red']
        self.assertEquals(898, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithGreyWhiteWhite(self):
        colors = ['grey', 'white', 'white', 'brown', 'red']
        self.assertEquals(899, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackBlack(self):
        colors = ['white', 'black', 'black', 'brown', 'red']
        self.assertEquals(900, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackBrown(self):
        colors = ['white', 'black', 'brown', 'brown', 'red']
        self.assertEquals(901, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackRed(self):
        colors = ['white', 'black', 'red', 'brown', 'red']
        self.assertEquals(902, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackOrange(self):
        colors = ['white', 'black', 'orange', 'brown', 'red']
        self.assertEquals(903, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackYellow(self):
        colors = ['white', 'black', 'yellow', 'brown', 'red']
        self.assertEquals(904, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackGreen(self):
        colors = ['white', 'black', 'green', 'brown', 'red']
        self.assertEquals(905, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackBlue(self):
        colors = ['white', 'black', 'blue', 'brown', 'red']
        self.assertEquals(906, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackViolet(self):
        colors = ['white', 'black', 'violet', 'brown', 'red']
        self.assertEquals(907, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackGrey(self):
        colors = ['white', 'black', 'grey', 'brown', 'red']
        self.assertEquals(908, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlackWhite(self):
        colors = ['white', 'black', 'white', 'brown', 'red']
        self.assertEquals(909, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownBlack(self):
        colors = ['white', 'brown', 'black', 'brown', 'red']
        self.assertEquals(910, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownBrown(self):
        colors = ['white', 'brown', 'brown', 'brown', 'red']
        self.assertEquals(911, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownRed(self):
        colors = ['white', 'brown', 'red', 'brown', 'red']
        self.assertEquals(912, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownOrange(self):
        colors = ['white', 'brown', 'orange', 'brown', 'red']
        self.assertEquals(913, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownYellow(self):
        colors = ['white', 'brown', 'yellow', 'brown', 'red']
        self.assertEquals(914, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownGreen(self):
        colors = ['white', 'brown', 'green', 'brown', 'red']
        self.assertEquals(915, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownBlue(self):
        colors = ['white', 'brown', 'blue', 'brown', 'red']
        self.assertEquals(916, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownViolet(self):
        colors = ['white', 'brown', 'violet', 'brown', 'red']
        self.assertEquals(917, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownGrey(self):
        colors = ['white', 'brown', 'grey', 'brown', 'red']
        self.assertEquals(918, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBrownWhite(self):
        colors = ['white', 'brown', 'white', 'brown', 'red']
        self.assertEquals(919, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedBlack(self):
        colors = ['white', 'red', 'black', 'brown', 'red']
        self.assertEquals(920, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedBrown(self):
        colors = ['white', 'red', 'brown', 'brown', 'red']
        self.assertEquals(921, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedRed(self):
        colors = ['white', 'red', 'red', 'brown', 'red']
        self.assertEquals(922, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedOrange(self):
        colors = ['white', 'red', 'orange', 'brown', 'red']
        self.assertEquals(923, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedYellow(self):
        colors = ['white', 'red', 'yellow', 'brown', 'red']
        self.assertEquals(924, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedGreen(self):
        colors = ['white', 'red', 'green', 'brown', 'red']
        self.assertEquals(925, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedBlue(self):
        colors = ['white', 'red', 'blue', 'brown', 'red']
        self.assertEquals(926, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedViolet(self):
        colors = ['white', 'red', 'violet', 'brown', 'red']
        self.assertEquals(927, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedGrey(self):
        colors = ['white', 'red', 'grey', 'brown', 'red']
        self.assertEquals(928, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteRedWhite(self):
        colors = ['white', 'red', 'white', 'brown', 'red']
        self.assertEquals(929, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeBlack(self):
        colors = ['white', 'orange', 'black', 'brown', 'red']
        self.assertEquals(930, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeBrown(self):
        colors = ['white', 'orange', 'brown', 'brown', 'red']
        self.assertEquals(931, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeRed(self):
        colors = ['white', 'orange', 'red', 'brown', 'red']
        self.assertEquals(932, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeOrange(self):
        colors = ['white', 'orange', 'orange', 'brown', 'red']
        self.assertEquals(933, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeYellow(self):
        colors = ['white', 'orange', 'yellow', 'brown', 'red']
        self.assertEquals(934, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeGreen(self):
        colors = ['white', 'orange', 'green', 'brown', 'red']
        self.assertEquals(935, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeBlue(self):
        colors = ['white', 'orange', 'blue', 'brown', 'red']
        self.assertEquals(936, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeViolet(self):
        colors = ['white', 'orange', 'violet', 'brown', 'red']
        self.assertEquals(937, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeGrey(self):
        colors = ['white', 'orange', 'grey', 'brown', 'red']
        self.assertEquals(938, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteOrangeWhite(self):
        colors = ['white', 'orange', 'white', 'brown', 'red']
        self.assertEquals(939, decodeSignificantFigures(colors))
    
    def testDecodeSigFigWhenFiveBandsWithWhiteYellowBlack(self):
        colors = ['white', 'yellow', 'black', 'brown', 'red']
        self.assertEquals(940, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowBrown(self):
        colors = ['white', 'yellow', 'brown', 'brown', 'red']
        self.assertEquals(941, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowRed(self):
        colors = ['white', 'yellow', 'red', 'brown', 'red']
        self.assertEquals(942, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowOrange(self):
        colors = ['white', 'yellow', 'orange', 'brown', 'red']
        self.assertEquals(943, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowYellow(self):
        colors = ['white', 'yellow', 'yellow', 'brown', 'red']
        self.assertEquals(944, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowGreen(self):
        colors = ['white', 'yellow', 'green', 'brown', 'red']
        self.assertEquals(945, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowBlue(self):
        colors = ['white', 'yellow', 'blue', 'brown', 'red']
        self.assertEquals(946, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowViolet(self):
        colors = ['white', 'yellow', 'violet', 'brown', 'red']
        self.assertEquals(947, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowGrey(self):
        colors = ['white', 'yellow', 'grey', 'brown', 'red']
        self.assertEquals(948, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteYellowWhite(self):
        colors = ['white', 'yellow', 'white', 'brown', 'red']
        self.assertEquals(949, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenBlack(self):
        colors = ['white', 'green', 'black', 'brown', 'red']
        self.assertEquals(950, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenBrown(self):
        colors = ['white', 'green', 'brown', 'brown', 'red']
        self.assertEquals(951, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenRed(self):
        colors = ['white', 'green', 'red', 'brown', 'red']
        self.assertEquals(952, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenOrange(self):
        colors = ['white', 'green', 'orange', 'brown', 'red']
        self.assertEquals(953, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenYellow(self):
        colors = ['white', 'green', 'yellow', 'brown', 'red']
        self.assertEquals(954, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenGreen(self):
        colors = ['white', 'green', 'green', 'brown', 'red']
        self.assertEquals(955, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenBlue(self):
        colors = ['white', 'green', 'blue', 'brown', 'red']
        self.assertEquals(956, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenViolet(self):
        colors = ['white', 'green', 'violet', 'brown', 'red']
        self.assertEquals(957, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenGrey(self):
        colors = ['white', 'green', 'grey', 'brown', 'red']
        self.assertEquals(958, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreenWhite(self):
        colors = ['white', 'green', 'white', 'brown', 'red']
        self.assertEquals(959, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueBlack(self):
        colors = ['white', 'blue', 'black', 'brown', 'red']
        self.assertEquals(960, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueBrown(self):
        colors = ['white', 'blue', 'brown', 'brown', 'red']
        self.assertEquals(961, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueRed(self):
        colors = ['white', 'blue', 'red', 'brown', 'red']
        self.assertEquals(962, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueOrange(self):
        colors = ['white', 'blue', 'orange', 'brown', 'red']
        self.assertEquals(963, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueYellow(self):
        colors = ['white', 'blue', 'yellow', 'brown', 'red']
        self.assertEquals(964, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueGreen(self):
        colors = ['white', 'blue', 'green', 'brown', 'red']
        self.assertEquals(965, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueBlue(self):
        colors = ['white', 'blue', 'blue', 'brown', 'red']
        self.assertEquals(966, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueViolet(self):
        colors = ['white', 'blue', 'violet', 'brown', 'red']
        self.assertEquals(967, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueGrey(self):
        colors = ['white', 'blue', 'grey', 'brown', 'red']
        self.assertEquals(968, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteBlueWhite(self):
        colors = ['white', 'blue', 'white', 'brown', 'red']
        self.assertEquals(969, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletBlack(self):
        colors = ['white', 'violet', 'black', 'brown', 'red']
        self.assertEquals(970, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletBrown(self):
        colors = ['white', 'violet', 'brown', 'brown', 'red']
        self.assertEquals(971, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletRed(self):
        colors = ['white', 'violet', 'red', 'brown', 'red']
        self.assertEquals(972, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletOrange(self):
        colors = ['white', 'violet', 'orange', 'brown', 'red']
        self.assertEquals(973, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletYellow(self):
        colors = ['white', 'violet', 'yellow', 'brown', 'red']
        self.assertEquals(974, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletGreen(self):
        colors = ['white', 'violet', 'green', 'brown', 'red']
        self.assertEquals(975, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletBlue(self):
        colors = ['white', 'violet', 'blue', 'brown', 'red']
        self.assertEquals(976, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletViolet(self):
        colors = ['white', 'violet', 'violet', 'brown', 'red']
        self.assertEquals(977, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletGrey(self):
        colors = ['white', 'violet', 'grey', 'brown', 'red']
        self.assertEquals(978, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteVioletWhite(self):
        colors = ['white', 'violet', 'white', 'brown', 'red']
        self.assertEquals(979, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyBlack(self):
        colors = ['white', 'grey', 'black', 'brown', 'red']
        self.assertEquals(980, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyBrown(self):
        colors = ['white', 'grey', 'brown', 'brown', 'red']
        self.assertEquals(981, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyRed(self):
        colors = ['white', 'grey', 'red', 'brown', 'red']
        self.assertEquals(982, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyOrange(self):
        colors = ['white', 'grey', 'orange', 'brown', 'red']
        self.assertEquals(983, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyYellow(self):
        colors = ['white', 'grey', 'yellow', 'brown', 'red']
        self.assertEquals(984, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyGreen(self):
        colors = ['white', 'grey', 'green', 'brown', 'red']
        self.assertEquals(985, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyBlue(self):
        colors = ['white', 'grey', 'blue', 'brown', 'red']
        self.assertEquals(986, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyViolet(self):
        colors = ['white', 'grey', 'violet', 'brown', 'red']
        self.assertEquals(987, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyGrey(self):
        colors = ['white', 'grey', 'grey', 'brown', 'red']
        self.assertEquals(988, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteGreyWhite(self):
        colors = ['white', 'grey', 'white', 'brown', 'red']
        self.assertEquals(989, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteBlack(self):
        colors = ['white', 'white', 'black', 'brown', 'red']
        self.assertEquals(990, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteBrown(self):
        colors = ['white', 'white', 'brown', 'brown', 'red']
        self.assertEquals(991, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteRed(self):
        colors = ['white', 'white', 'red', 'brown', 'red']
        self.assertEquals(992, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteOrange(self):
        colors = ['white', 'white', 'orange', 'brown', 'red']
        self.assertEquals(993, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteYellow(self):
        colors = ['white', 'white', 'yellow', 'brown', 'red']
        self.assertEquals(994, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteGreen(self):
        colors = ['white', 'white', 'green', 'brown', 'red']
        self.assertEquals(995, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteBlue(self):
        colors = ['white', 'white', 'blue', 'brown', 'red']
        self.assertEquals(996, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteViolet(self):
        colors = ['white', 'white', 'violet', 'brown', 'red']
        self.assertEquals(997, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteGrey(self):
        colors = ['white', 'white', 'grey', 'brown', 'red']
        self.assertEquals(998, decodeSignificantFigures(colors))

    def testDecodeSigFigWhenFiveBandsWithWhiteWhiteWhite(self):
        colors = ['white', 'white', 'white', 'brown', 'red']
        self.assertEquals(999, decodeSignificantFigures(colors))
