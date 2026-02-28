"""Task 2: The Return Statement (02_converter.py)

    Define a function called celsius_to_fahrenheit that takes one parameter: c.

    Calculate the Fahrenheit value using the formula: (c * 9/5) + 32.

    return that calculated value.

    Outside the function, call it with the number 30, save the result to a new variable, and then print() that variable."""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit_value = celsius_to_fahrenheit(30)
print(fahrenheit_value)
