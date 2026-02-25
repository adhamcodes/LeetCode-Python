"""Ask the user for their test score (0-100). Write an if/elif/else chain that prints their letter grade:

    90 or above: "A"

    80 to 89: "B"

    70 to 79: "C"

    Below 70: "F" """

# Get user input
score = input("Enter your test score (0-100): ")
score = int(score)  # Convert the input to an integer

# Determine the letter grade
if score >= 90:
    print("Your grade is: A")
elif score >= 80:
    print("Your grade is: B")
elif score >= 70:
    print("Your grade is: C")
else:
    print("Your grade is: F") 

    