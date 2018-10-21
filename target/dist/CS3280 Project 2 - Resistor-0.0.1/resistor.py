valid_colors = ['black', 'brown', 'red', 'orange',
                'yellow', 'green', 'blue', 'violet',
                'grey', 'white', 'gold', 'silver', 'none']

tolerances = {
    'brown': 1.0,
    'red': 2.0,
    'green': 0.5,
    'blue': 0.25,
    'violet': 0.1,
    'grey': 0.05,
    'gold': 5.0,
    'silver': 10.0,
    'none': 20.0
}

multipliers = {
    'black': (1, ''),
    'brown': (10, ''),
    'red': (100, ''),
    'orange': (1, 'K'),
    'yellow': (10, 'K'),
    'green': (100, 'K'),
    'blue': (1, 'M'),
    'violet': (10, 'M'),
    'grey': (100, 'M'),
    'white': (1, 'G'),
    'gold': (0.1, ''),
    'silver': (0.01, '')
}

significantFigures = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}


def validateColorsList(colors):
    '''
    Returns true if a valid list of colors is passed,
    false otherwise

    @param colors   the list of colors

    @return true if colors is a valid list of colors,
    false otherwise
    '''
    if colors is None:
        raise ValueError('Colors list cannot be None.')

    if colors == []:
        raise ValueError('The colors list cannot be empty.')

    if len(colors) < 4:
        raise ValueError('The colors list must contain at least four colors.')

    if len(colors) > 5:
        raise ValueError('The colors list must contain at least four colors.')

    _colorsContainsOnlyValidColors(colors)

    if len(colors) == 4:
        _validateFourBandResistorColorsList(colors)

    if len(colors) == 5:
        _validateFiveBandResistorColorsList(colors)

    return True


def _isValidColor(color):
    '''
    Returns true if the color is a valid color,
    false otherwise

    @param color    the color being tested

    @return true if the color is valid,
    false otherwise
    '''
    return color in valid_colors


def _isFirstBandColorAllowed(color):
    '''
    Returns true if the color of the first band is
    a valid color for that band, and false otherwise.

    @param color    the color of the band

    @preconditions color != 'gold' or color != 'silver'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['gold', 'silver', 'none']
    return color not in invalidBandColors


def _isSecondBandColorAllowed(color):
    '''
    Returns true if the color of the second band is
    a valid color for that band, and false otherwise

    @param color    the color of the band

    @preconditions color != 'gold' or color != 'silver'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['gold', 'silver', 'none']
    return color not in invalidBandColors


def _isThirdBandColorAllowed(color):
    '''
    Returns true if the color of the third band is
    a valid color for that band, and false otherwise

    @param color    the color of the band

    @preconditions color != 'none'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['none']
    return color not in invalidBandColors


def _isFourthBandColorAllowed(color):
    '''
    Returns true if the color of the fourth band is
    a valid color for that band, and false otherwise

    @param color    the color of the band

    @preconditions color != 'black' and color != 'orange'
                    and color != 'yellow' and color != 'white'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['black', 'orange', 'yellow', 'white']
    return color not in invalidBandColors


def _isFourthBandColorAllowedOfFiveBandResistor(color):
    '''
    Returns true if the color of the fourth band is
    a valid color for that band, and false otherwise

    @param color    the color of the band

    @preconditions color != 'none'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['none']
    return color not in invalidBandColors


def _isFifthBandColorAllowedOfFiveBandResistor(color):
    '''
    Returns true if the color of the fifth band is
    a valid color for that band, and false otherwise

    @param color    the color of the band

    @preconditions color != 'black' and color != 'orange'
                    and color != 'yellow' and color != 'white'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['black', 'orange', 'yellow', 'white']
    return color not in invalidBandColors


def _validateFourBandResistorColorsList(colors):
    '''
    Raises a ValueError if the first or second band contains a
    disallowed color. Returns true if all bands are allowed colors

    @param colors   the list of resistor colors

    @return True if a ValueError is not raised
    '''
    (band1, band2, band3, band4) = colors

    if not _isFirstBandColorAllowed(band1):
        raise ValueError(band1 + ' is not allowed in the first band.')

    if not _isSecondBandColorAllowed(band2):
        raise ValueError(band2 + ' is not allowed in the second band.')

    if not _isThirdBandColorAllowed(band3):
        raise ValueError(band3 + ' is not allowed in the third band.')

    if not _isFourthBandColorAllowed(band4):
        raise ValueError(band4 + ' is not allowed in the fourth band.')

    return True


def _validateFiveBandResistorColorsList(colors):
    '''
    Raises a ValueError if the first, second, or fifth band contains a
    disallowed color. Returns true if all bands are allowed colors

    @param colors   the list of resistor colors

    @return True if a ValueError is not raised
    '''
    (band1, band2, band3, band4, band5) = colors

    if not _isFirstBandColorAllowed(band1):
        raise ValueError(band1 + ' is not allowed in the first band.')

    if not _isSecondBandColorAllowed(band2):
        raise ValueError(band2 + ' is not allowed in the second band.')

    if not _isThirdBandColorAllowed(band3):
        raise ValueError(band3 + ' is not allowed in the third band.')

    if not _isFourthBandColorAllowedOfFiveBandResistor(band4):
        raise ValueError(band4 + ' is not allowed in the fourth band.')

    if not _isFifthBandColorAllowedOfFiveBandResistor(band5):
        raise ValueError(band5 + ' is not allowed in the fifth band.')

    return True


def _colorsContainsOnlyValidColors(colors):
    '''
    Raises a ValueError if any of the colors in the passed list
    are not in the list valid_colors

    @param colors   the list of colors being checked
    '''
    for band in colors:
        if not _isValidColor(band):
            raise ValueError(str(band) + ' is not a valid color.')


def decodeTolerance(colors):
    '''
    Returns the tolerance as a floating-point number.
    In the case of a four band resistor, the tolerance will
    be the fourth color. In the case of a five band resistor,
    the tolerance will be the fifth color.

    @param colors   the list of colors

    @return a floating-point number representing the tolerance.
    '''
    validateColorsList(colors)
    if len(colors) == 4:
        return _decodeToleranceOfFourBandResistor(colors)

    if len(colors) == 5:
        return _decodeToleranceOfFiveBandResistor(colors)


def _decodeToleranceOfFourBandResistor(colors):
    '''
    TODO: Spec
    '''
    (_, _, _, toleranceBand) = colors

    return tolerances.get(toleranceBand)


def _decodeToleranceOfFiveBandResistor(colors):
    '''
    TODO: Spec
    '''
    (_, _, _, _, toleranceBand) = colors

    return tolerances.get(toleranceBand)


def decodeMultiplier(colors):
    '''
    Returns a tuple whose first element is the numeric multiplier
    and the second element is the prefix

    @param colors   the list of colors

    @return a tuple whose first element is the numeric multiplier
    and the second element is the prefix
    '''
    validateColorsList(colors)

    if len(colors) == 4:
        (_, _, multiplierBand, _) = colors
        return multipliers.get(multiplierBand)

    if len(colors) == 5:
        (_, _, _, multiplierBand, _) = colors
        return multipliers.get(multiplierBand)


def decodeSignificantFigures(colors):
    '''Returns an integer representing the numeric portion of the
    resistance.

    @param colors   the list of colors

    @return an integer representing the numeric portion of the
    resistance.
    '''
    validateColorsList(colors)

    if len(colors) == 4:
        (sigFigBand1, sigFigBand2, _, _) = colors
        sigFig1 = str(significantFigures.get(sigFigBand1))
        sigFig2 = str(significantFigures.get(sigFigBand2))

        return int(sigFig1 + sigFig2)

    if len(colors) == 5:
        (sigFigBand1, sigFigBand2, sigFigBand3, _, _) = colors
        sigFig1 = str(significantFigures.get(sigFigBand1))
        sigFig2 = str(significantFigures.get(sigFigBand2))
        sigFig3 = str(significantFigures.get(sigFigBand3))

        return int(sigFig1 + sigFig2 + sigFig3)


def createFormattedResistanceString(colors):
    '''
    Creates a string with a full description of the resistor.

    @param colors   the list of colors

    @return a string with a full description of the resistor.
    '''
    validateColorsList(colors)

    significantFigures = decodeSignificantFigures(colors)
    multiplierNumber, multiplierUnit = decodeMultiplier(colors)
    multipliedSignificantFigures = round(
        significantFigures * multiplierNumber, 2)

    multipliedSignificantFigures, multiplierUnit = _correctResistanceUnits(
        multipliedSignificantFigures, multiplierUnit)

    tolerance = decodeTolerance(colors)

    return "{} {}ohms +/- {}%".format(
        multipliedSignificantFigures,
        multiplierUnit,
        tolerance)


def _correctResistanceUnits(multipliedSignificantFigures, multiplierUnit):
    '''
    Corrects resistance in cases where multiplier causes number to roll
    over to next unit. E.g. if result is 1000 Ohms it will correct it to
    1 Kohms.

    @param multipliedSignificantFigures    the result of multiplying the
    significant figures by the multiplier

    @param multiplierUnit   the unit E.g. K, M, or G

    @return a tuple containing the corrected multiplied number and unit
    '''
    if multipliedSignificantFigures < 1000:
        return (multipliedSignificantFigures, multiplierUnit)

    else:
        units = {
            '': 'K',
            'K': 'M',
            'M': 'G'
        }
        multipliedSignificantFigures = multipliedSignificantFigures / 1000
        return (multipliedSignificantFigures, units[multiplierUnit])


def decodeResistance(colors):
    '''
    Returns a dictionary representing a resistor.

    @params colors  the colors list

    @return a dictionary representing a resistor.
    '''
    validateColorsList(colors)
    result = {}
    multiplierNumber, multiplierUnit = decodeMultiplier(colors)

    result['value'] = decodeSignificantFigures(colors) * multiplierNumber
    result['units'] = str(multiplierUnit) + 'ohms'
    result['tolerance'] = decodeTolerance(colors)
    result['formatted'] = createFormattedResistanceString(colors)

    return 

def generateTest():
    valid_four_band_colors = {
        'band1': ['black', 'brown', 'red', 'orange',
                'yellow', 'green', 'blue', 'violet',
                'grey', 'white'],
        'band2': ['black', 'brown', 'red', 'orange',
                'yellow', 'green', 'blue', 'violet',
                'grey', 'white'],
        'band3': ['black', 'brown', 'red', 'orange',
                'yellow', 'green', 'blue', 'violet',
                'grey', 'white', 'gold', 'silver'],
        'band4': ['brown', 'red', 'green', 'blue', 'violet',
                'grey', 'gold', 'silver', 'none']
    }


    filename = 'test.py'
    f = open(filename, 'w')

    f.write('import unittest\n')
    f.write('from resistor import *\n')
    f.write('\n')
    f.write('class CreateFormattedResistanceStringTests(unittest.TestCase):\n\n')

    list1 = valid_four_band_colors.get('band1')
    list2 = valid_four_band_colors.get('band2')
    list3 = valid_four_band_colors.get('band3')
    list4 = valid_four_band_colors.get('band4')
    #count = 0
    for i in list4:
        for j in list3:
            for k in list2:
                for l in list1:
                    colors = [l, k, j, i]
                    f.write(f"    def testCreateFormattedResistanceStringFourBand{l.capitalize()}{k.capitalize()}{j.capitalize()}{i.capitalize()}(self):\n")
                    f.write(f"        colors = ['{l}', '{k}', '{j}', '{i}']\n")
                    f.write(f"        result = createFormattedResistanceString(colors)\n")
                    f.write(f"        self.assertEquals(\"{createFormattedResistanceString(colors)}\", result)\n\n")
                    #print(f"{l} {k} {j} {i} " + createFormattedResistanceString([l, k, j, i]))
                    #count += 1

    list1 = valid_four_band_colors.get('band1')
    list2 = valid_four_band_colors.get('band2')
    list3 = valid_four_band_colors.get('band2')
    list4 = valid_four_band_colors.get('band3')
    list5 = valid_four_band_colors.get('band4')
    #count = 0
    for h in list5:
        for i in list4:
            for j in list3:
                for k in list2:
                    for l in list1:
                        colors = [l, k, j, i, h]
                        f.write(f"    def testCreateFormattedResistanceStringFiveBand{l.capitalize()}{k.capitalize()}{j.capitalize()}{i.capitalize()}(self):\n")
                        f.write(f"        colors = ['{l}', '{k}', '{j}', '{i}', '{h}']\n")
                        f.write(f"        result = createFormattedResistanceString(colors)\n")
                        f.write(f"        self.assertEquals(\"{createFormattedResistanceString(colors)}\", result)\n\n")

#print(count)

def capitalize(word):
    return word.capitalize

generateTest()
