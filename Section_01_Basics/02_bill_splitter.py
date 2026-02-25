"""
Ask for a bill total, calculate a 15% tip, add it to the total, ask how many people are splitting it, and print the final cost per person.
"""

# Get the bill total from the user
bill_total = input("Please enter your total bill: ")
# Convert the bill total to a float so we can do math with it
bill_total = float(bill_total)
# Calculate the tip (15% of the bill total)
tip = bill_total * 0.15
# Calculate the total amount including the tip
total = bill_total + tip

# Get the number of people splitting the bill
num_people = input("How many people are splitting the bill? ")
# Convert the number of people to an integer
num_people = int(num_people)

# Calculate the cost per person
cost = total / num_people

# Print the final cost per person 
print(f"Each person should pay: ${cost}")


