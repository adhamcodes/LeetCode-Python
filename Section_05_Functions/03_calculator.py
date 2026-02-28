"""Task 3: The Default Parameter (03_calculator.py)

    Define a function called calculate_total that takes two parameters: bill and tip_percent.

    Set the default value of tip_percent to 15 right inside the parentheses (e.g., tip_percent=15).

    Calculate the final price: bill + (bill * (tip_percent / 100)) and return it.

    Outside the function, call it once providing only a bill amount of 100 (letting the default 15% kick in).

    Call it a second time providing a bill of 100 AND a tip of 20 (overriding the default). Print both results."""

def calculate_total(bill, tip_percent=15):
    return bill + (bill * (tip_percent / 100))
total_with_default_tip = calculate_total(100)
total_with_custom_tip = calculate_total(100, tip_percent=20)
print(total_with_default_tip)
print(total_with_custom_tip)