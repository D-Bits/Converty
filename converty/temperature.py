"""
Temperature conversions. 
"""


def fahrenheit_to_celsius(fahrenheit: float) -> float:

    # Throw exception if input is < absolute zero
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!\n')
    celsius = (fahrenheit -32) / 1.80

    return round(celsius, 2)


def celsius_to_fahrenheit(celsius: float) -> float:

    fahrenheit = celsius * 1.80 + 32.00
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!\n')

    return round(fahrenheit, 2)


def celsius_to_kelvin(celsius: float) -> float:

    kelvin = celsius + 273.15
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!\n')

    return round(kelvin, 2)


def kelvin_to_celsius(kelvin: float) -> float:

    celsius = kelvin - 273.15
    if kelvin < 0:
        raise Exception('Cannot be below absolute zero!\n')

    return round(celsius, 2)


def fahrenheit_to_kelvin(fahrenheit: float) -> float:

    kelvin = ((fahrenheit - 32) / 1.80)+ 273.15
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!\n')

    return round(kelvin, 2)


def kelvin_to_fahrenheit(kelvin: float) -> float:

    fahrenheit = (kelvin - 273.15) * 1.80 + 32

    return round(fahrenheit, 2)
