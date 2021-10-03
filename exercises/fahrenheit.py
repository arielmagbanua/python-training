def fahrenheit(temperature_in_celsius):
    """Converts and returns the fahrenheit equivalent of temperature in celsius.

    Parameters:
    temperature_in_celsius (int|double): The input temperature in celsius

    Returns:
    double: The temperature in fahrenheit.
    """

    fahrenheit = ((9 / 5) * temperature_in_celsius) / 32
    return fahrenheit


