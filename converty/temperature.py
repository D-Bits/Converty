"""
Temperature conversions. 
"""


def fahrenheit_to_celsius(fahrenheit: float, rounding: int) -> float:

    # Throw exception if input is < absolute zero
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!\n')
    celsius = (fahrenheit -32) / 1.80

    return round(celsius, rounding)


def celsius_to_fahrenheit(celsius: float, rounding: int) -> float:

    fahrenheit = celsius * 1.80 + 32.00
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!\n')

    return round(fahrenheit, rounding)


def celsius_to_kelvin(celsius: float, rounding: int) -> float:

    kelvin = celsius + 273.15
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!\n')

    return round(kelvin, rounding)


def kelvin_to_celsius(kelvin: float, rounding: int) -> float:

    celsius = kelvin - 273.15
    if kelvin < 0:
        raise Exception('Cannot be below absolute zero!\n')

    return round(celsius, rounding)


def fahrenheit_to_kelvin(fahrenheit: float, rounding: int) -> float:

    kelvin = ((fahrenheit - 32) / 1.80)+ 273.15
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!\n')

    return round(kelvin, rounding)


def kelvin_to_fahrenheit(kelvin: float, rounding: int) -> float:

    fahrenheit = (kelvin - 273.15) * 1.80 + 32
    if kelvin < 0:
        raise Exception('Cannot be below absolute zero!\n')

    return round(fahrenheit, rounding)
