"""
Conversions for length measurements.
"""


def feet_to_meters(feet):

    meters = feet / 3.2808
    if feet == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(meters, 2)


def meters_to_feet(meters):

    feet = meters * 3.2808
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(feet, 2)


def miles_to_kilos(miles):

    kilos = miles / 0.62137
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def kilos_to_miles(kilos):

    miles = kilos * 0.62137
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')
            
    return round(miles, 2)


def length_choices():

    print()

    for key, val in length_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a length conversion: '))

    if conversion == 1:
        user_feet = float(input('Enter an amount of feet to be converted into meters: '))
        print(f'{user_feet} ft equals {feet_to_meters(user_feet)} m.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 2:
        user_meters = float(input('Enter an amount of meters to be converted into feet: '))
        print(f'{user_meters} m equals {meters_to_feet(user_meters)} ft.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 3:
        user_miles = float(input('Enter an amount of miles to be converted to kilometers: '))
        print(f'{user_miles} mi equals {miles_to_kilos(user_miles)} kms.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 4:
        user_kilos = float(input('Enter an amount of kilometers to be converted to miles: '))
        print(f'{user_kilos} kms equals {kilos_to_miles(user_kilos)} mi.\n')
        input("Conversion complete. Press enter to exit.")
    else:
        raise Exception('Invalid value entered.')