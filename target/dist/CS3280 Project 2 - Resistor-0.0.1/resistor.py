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
