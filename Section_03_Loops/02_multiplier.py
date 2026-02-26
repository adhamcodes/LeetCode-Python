"""
Ask the user to input a number (e.g., 5). Use a for loop and the range() function to print the multiplication table for that number from 1 to 10.
"""

# Write your code below this line
num = input("Enter a number to see its multiplication table: ")
num = int(num)

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")