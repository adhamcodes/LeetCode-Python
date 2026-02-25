"""At the top of your script, create two variables: db_user = "adhamcodes" and db_pass = "python123".
Next, ask the user to input a username and a password.
Use the logical and operator to check if both the inputted username and password match your database variables. 
If they do, print "Access Granted". If either of them is wrong, print "Access Denied".
"""
# Database credentials
db_user = "adhamcodes"
db_pass = "python123"

# Get user input
input_user = input("Enter your username: ")
input_pass = input("Enter your password: ")

# Check credentials
if input_user == db_user and input_pass == db_pass:
    print("Access Granted")
else:    
    print("Access Denied")

    