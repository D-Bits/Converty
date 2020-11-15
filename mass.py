"""
Unit conversions for mass.
"""


def pounds_to_kilograms(pounds):

    kilos = pounds / 2.2046
    if pounds == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def kilograms_to_pounds(kilos):

    pounds = kilos * 2.2046
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(pounds, 2)


def ounces_to_grams(ounces):

    grams = (ounces / 0.035274)
    if ounces == 0:
        raise Exception('Cannot calculate zero value!\n')

    return grams


def grams_to_ounces(grams):

    ounces = grams * 0.035274
    if grams == 0:
        raise Exception('Cannot calculate zero value!\n')
            
    return ounces


# Display the available unit conversions, prompt the user to choose
def mass_choices():

    print()

    for key, val in mass_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a mass conversion: '))
    print()

    if conversion == 1:
        user_lbs = float(input('Enter an amount in pounds to be converted to kilos: '))
        print(f'{user_lbs}lbs equals {pounds_to_kilograms(user_lbs)}kgs.')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 2:
        user_kilos = float(input('Enter an amount in kilograms to be converted to pounds: '))
        print(f'{user_kilos}kgs equals {kilograms_to_pounds(user_kilos)}lbs.')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 3:
        user_oz = float(input('Enter an amount in ounces to be converted to grams: '))
        print(f'{user_oz}oz. equals {ounces_to_grams(user_oz)}g.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 4:
        user_g = float(input('Enter an amount in grams to be converted to ounces: '))
        print(f'{user_g} g. equals {grams_to_ounces(user_g)} oz.\n')
        input("Conversion complete. Press enter to exit.")
    else:
        raise Exception('Invalid value entered.\n')