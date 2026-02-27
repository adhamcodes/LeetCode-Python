"""The Mini-Project: The Terminal Matchmaking Manager(Using Variables, User Input, If/Elif/Else, While Loops, For Loops, and Lists.)"""
"""Your mission is to build an interactive command-line application that manages a team roster for a tournament. The program needs to stay open and keep asking the user what they want to do until they explicitly tell it to shut down.

The Specifications:

    The Core Data: Start with an empty list called roster = [].

    The Main Engine: Create a while loop that keeps the program running continuously. (Hint: while True: is a great way to make an infinite loop, as long as you give it a way to break later!)

    The Interface: Every time the loop runs, print() a menu for the user with four options:

        [1] Add a player to the squad

        [2] View current squad

        [3] Remove a player from the squad

        [4] Exit system

    The Logic Gates: Get the user's input, and use an if / elif / else block to handle their choice:

        If 1: Ask the user to type a player's name, then .append() that name to your roster list. Print a success message like "Player added!"

        If 2: Check if the roster has players. If it does, use a for loop to print every name. If the list is empty, print "The squad is currently empty."

        If 3: Ask the user for the name of the player to kick. Use the .remove() method to take them out of the list. (Bonus points: use an if name in roster: check first so the program doesn't crash if they type a name that isn't there).

        If 4: Print a shutdown message and use the break command to smash out of the while loop and end the script.

        Else: If they type anything other than 1, 2, 3, or 4, print "Invalid command. Try again.""""

roster = []
while True:
    print("\nMenu:")
    print("[1] Add a player to the squad")
    print("[2] View current squad")
    print("[3] Remove a player from the squad")
    print("[4] Exit system")

    choice = input("Enter your choice: ")

    if choice == "1":
        player_name = input("Enter the player's name to add: ")
        roster.append(player_name)
        print("Player added!")
    elif choice == "2":
        if roster:
            print("Current squad:")
            for player in roster:
                print(player)
        else:
            print("The squad is currently empty.")
    elif choice == "3":
        player_name = input("Enter the player's name to remove: ")
        if player_name in roster:
            roster.remove(player_name)
            print("Player removed!")
        else:
            print("Player not found in the squad.")
    elif choice == "4":
        print("Shutting down the system. Goodbye!")
        break
    else:
        print("Invalid command. Try again.")

