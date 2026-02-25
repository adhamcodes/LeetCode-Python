"""
Task 1: The Custom Greeter (01_greeter.py)
Write a script that asks the user for their name using input(). 
Then, ask them for the year they were born. 
Calculate their current age (assume the current year is 2026), 
and print out a welcome message using an f-string that tells them their name and age.
(Hint: input() always brings in data as a string. 
You will need to convert the birth year to an int() before you can do math with it!)"""

name = input("Please enter your name: ")
Birth_year = input("Please enter the year you were born: ")

# Convert the birth year to an integer and calculate the age
current_year = 2026   
age = current_year - int(Birth_year)   

print(f"Welcome {name}! You are {age} years old.")

