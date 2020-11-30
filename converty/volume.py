"""
Conversions for volume.
"""

def litres_to_gallons(litres: float) -> float:

    gallons = litres * 0.26417
    if litres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(gallons, 2)


def gallons_to_litres(gallons: float) -> float:

    litres = gallons / 0.26417
    if gallons == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(litres, 2)
