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
        raise ValueError("Colors list cannot be None.")

    if colors == []:
        raise ValueError("The colors list cannot be empty.")

    if len(colors) < 4:
        raise ValueError("The colors list must contain at least four colors.")

    if len(colors) > 5:
        raise ValueError("The colors list must contain at least four colors.")

    if len(colors) == 4:
        (band1, band2, band3, band4) = colors
        for band in colors:
            if not isValidColor(band):
                raise ValueError(band + " is not a valid color")


def isValidColor(color):
    '''
    Returns true if the color is a valid color,
    false otherwise

    @param color    the color being tested

    @return true if the color is valid,
    false otherwise
    '''
    return color in valid_colors
