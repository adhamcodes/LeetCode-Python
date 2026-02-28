"""Task 5: The Keyboard Modder (05_keyboard_mod.py)

Let's pass a List into a function and modify it.

    Define a function called upgrade_board that takes two parameters: current_build (which will be a list) and new_part (which will be a string).

    Give new_part a default value of "Linear Switches".

    Inside the function, use .append() to add the new_part to the current_build list.

    return the updated list.

    Outside the function, create a starting list: my_wk68 = ["Base Kit", "Keycaps"].

    Call the function once using just the my_wk68 list (letting the default switches kick in), and print the result."""

def upgrade_board(current_build, new_part="Linear Switches"):
    current_build.append(new_part)
    return current_build
my_wk68 = ["Base Kit", "Keycaps"]
updated_build = upgrade_board(my_wk68)
print(updated_build)