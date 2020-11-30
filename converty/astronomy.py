""" 
Conversions for metric, imperial, and various astronomical
measuring units (AU, light years, parsecs).
"""


def kilometers_to_au(kilos: float) -> float:

    au = kilos / 149597900
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(au, 2)


def au_to_kilometers(au: float) -> float:

    kilos = au * 149597900
    if au == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def miles_to_au(miles: float) -> float:

    au = miles / 92955825.9
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(au, 2)


def au_to_miles(au: float) -> float:

    miles = au * 92955825.9
    if au == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(miles, 2)


def kilometers_to_ly(kilos: float) -> float:

    ly = kilos / 9460730000000
    if ly == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(ly, 2)


def ly_to_kilometers(ly: float) -> float:

    kilos = ly * 9460730000000
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def miles_to_ly(miles: float) -> float:

    ly= miles / 5878625000000
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(ly, 2)


def ly_to_miles(ly: float) -> float:

    miles = ly * 5878625000000
    if ly == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(miles, 2)


def parsecs_to_ly(parsecs: float) -> float:

    ly = parsecs *  3.26156
    if parsecs == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(ly, 2)


def ly_to_parsecs(ly: float) -> float:

    parsecs = ly /  3.26156
    if ly == 0:
        raise Exception('Cannot calculate zero value!\n')

    return parsecs
