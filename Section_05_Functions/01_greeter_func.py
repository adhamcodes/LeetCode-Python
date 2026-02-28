"""Task 1: The Reusable Greeter (01_greeter_func.py)

    Define a function called welcome_player that takes one parameter: username.

    Inside the function, print a formatted string: "Connecting to server... Welcome, [username]!"

    Outside the function, call welcome_player() three separate times, passing in a different name string each time."""

def welcome_player(username):
    print(f"Connecting to server... Welcome, {username}!")
welcome_player("Alice")
welcome_player("Bob")
welcome_player("Charlie")