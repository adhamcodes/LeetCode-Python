"""
Write a script that asks the user to input a number. Use the modulo operator (%) to figure out if the number is even or odd, and print out the result.
"""

# Get user input
num = input("Enter a number: ")
num = int(num)  # Convert the input to an integer

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
