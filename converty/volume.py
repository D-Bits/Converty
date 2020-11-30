"""
Conversions for volume.
"""

def litres_to_gallons(litres: float, rounding: int) -> float:

    gallons = litres * 0.26417
    if litres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(gallons, rounding)


def gallons_to_litres(gallons: float, rounding: int) -> float:

    litres = gallons / 0.26417
    if gallons == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(litres, rounding)
