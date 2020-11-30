""" 
Conversions for metric, imperial, and various astronomical
measuring units (AU, light years, parsecs).
"""


def kilometers_to_au(kilos: float, rounding: int) -> float:

    au = kilos / 149597900
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(au, rounding)


def au_to_kilometers(au: float, rounding: int) -> float:

    kilos = au * 149597900
    if au == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, rounding)


def miles_to_au(miles: float, rounding: int) -> float:

    au = miles / 92955825.9
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(au, rounding)


def au_to_miles(au: float, rounding: int) -> float:

    miles = au * 92955825.9
    if au == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(miles, rounding)


def kilometers_to_ly(kilos: float, rounding: int) -> float:

    ly = kilos / 9460730000000
    if ly == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(ly, rounding)


def ly_to_kilometers(ly: float, rounding: int) -> float:

    kilos = ly * 9460730000000
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, rounding)


def miles_to_ly(miles: float, rounding: int) -> float:

    ly= miles / 5878625000000
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(ly, rounding)


def ly_to_miles(ly: float, rounding: int) -> float:

    miles = ly * 5878625000000
    if ly == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(miles, rounding)


def parsecs_to_ly(parsecs: float, rounding: int) -> float:

    ly = parsecs *  3.26156
    if parsecs == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(ly, rounding)


def ly_to_parsecs(ly: float, rounding: int) -> float:

    parsecs = ly /  3.26156
    if ly == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(parsecs, rounding)
