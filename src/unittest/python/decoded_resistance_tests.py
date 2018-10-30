import unittest
from resistor import *


class DecodeResistanceTests(unittest.TestCase):

    def testDecodeResistanceOnValidFourBandResistorOhms(self):
        colors = ['red', 'brown', 'black', 'brown']
        result = decodeResistance(colors)
        expected = {'value': 21,
                    'units': 'ohms',
                    'tolerance': 1.0,
                    'formatted': '21 ohms +/- 1.0%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFourBandResistorKohms(self):
        colors = ['violet', 'grey', 'red', 'green']
        result = decodeResistance(colors)
        expected = {'value': 7.8,
                    'units': 'Kohms',
                    'tolerance': 0.5,
                    'formatted': '7.8 Kohms +/- 0.5%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFourBandResistorMohms(self):
        colors = ['blue', 'orange', 'green', 'grey']
        result = decodeResistance(colors)
        expected = {'value': 6.3,
                    'units': 'Mohms',
                    'tolerance': 0.05,
                    'formatted': '6.3 Mohms +/- 0.05%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFourBandResistorGohms(self):
        colors = ['grey', 'black', 'grey', 'brown']
        result = decodeResistance(colors)
        expected = {'value': 8.0,
                    'units': 'Gohms',
                    'tolerance': 1.0,
                    'formatted': '8.0 Gohms +/- 1.0%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFiveBandResistorOhms(self):
        colors = ['red', 'orange', 'black', 'black', 'brown']
        result = decodeResistance(colors)
        expected = {'value': 230,
                    'units': 'ohms',
                    'tolerance': 1.0,
                    'formatted': '230 ohms +/- 1.0%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFiveBandResistorKohms(self):
        colors = ['green', 'yellow', 'red', 'brown', 'red']
        result = decodeResistance(colors)
        expected = {'value': 5.42,
                    'units': 'Kohms',
                    'tolerance': 2.0,
                    'formatted': '5.42 Kohms +/- 2.0%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFiveBandResistorMohms(self):
        colors = ['blue', 'red', 'green', 'green', 'grey']
        result = decodeResistance(colors)
        expected = {'value': 62.5,
                    'units': 'Mohms',
                    'tolerance': 0.05,
                    'formatted': '62.5 Mohms +/- 0.05%'
                    }
        self.assertEquals(expected, result)

    def testDecodeResistanceOnValidFiveBandResistorGohms(self):
        colors = ['brown', 'red', 'violet', 'white', 'brown']
        result = decodeResistance(colors)
        expected = {'value': 127,
                    'units': 'Gohms',
                    'tolerance': 1.0,
                    'formatted': '127 Gohms +/- 1.0%'
                    }
        self.assertEquals(expected, result)
