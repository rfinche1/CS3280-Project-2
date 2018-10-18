valid_colors = ['black', 'brown', 'red', 'orange',
                'yellow', 'green', 'blue', 'violet',
                'grey', 'white', 'gold', 'silver']


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

    colorsContainsOnlyValidColors(colors)

    if len(colors) == 4:
        validateFourBandResistorColorsList(colors)

    if len(colors) == 5:
        validateFiveBandResistorColorsList(colors)

    return True


def isValidColor(color):
    '''
    Returns true if the color is a valid color,
    false otherwise

    @param color    the color being tested

    @return true if the color is valid,
    false otherwise
    '''
    return color in valid_colors


def isFirstBandValid(color):
    '''
    Returns true if the color of the first band is
    a valid color for that band, and false otherwise.

    @param color    the color of the band

    @preconditions color != 'gold' or color != 'silver'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['gold', 'silver']
    return color not in invalidBandColors


def isSecondBandValid(color):
    '''
    Returns true if the color of the second band is
    a valid color for that band, and false otherwise

    @param color    the color of the band

    @preconditions color != 'gold' or color != 'silver'

    @return true if the band is a valid color,
    false otherwise
    '''
    invalidBandColors = ['gold', 'silver']
    return color not in invalidBandColors


def isFifthBandValid(color):
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


def validateFourBandResistorColorsList(colors):
    '''
    TODO: Spec
    '''
    (band1, band2, band3, band4) = colors

    if not isFirstBandValid(band1):
        raise ValueError(band1 + ' is not allowed in the first band.')

    if not isSecondBandValid(band2):
        raise ValueError(band2 + ' is not allowed in the second band.')

    return True


def validateFiveBandResistorColorsList(colors):
    '''
    TODO: Spec
    '''
    (band1, band2, band3, band4, band5) = colors

    if not isFirstBandValid(band1):
        raise ValueError(band1 + ' is not allowed in the first band.')

    if not isSecondBandValid(band2):
        raise ValueError(band2 + ' is not allowed in the second band.')

    if not isFifthBandValid(band5):
        raise ValueError(band5 + ' is not allowed in the fifth band.')

    return True


def colorsContainsOnlyValidColors(colors):
    '''
    TODO: Spec
    '''
    for band in colors:
        if not isValidColor(band):
            raise ValueError(str(band) + ' is not a valid color.')
