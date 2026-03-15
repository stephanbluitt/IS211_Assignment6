# conversions

#functions 
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins."""
    return round(celsius + 273.15, 2)

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit."""
    return round((celsius * 9/5) + 32, 2)

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins."""
    return round((fahrenheit - 32) * 5/9 + 273.15, 2)

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius."""
    return round(kelvin - 273.15, 2)

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit."""
    return round((kelvin - 273.15) * 9/5 + 32, 2)
