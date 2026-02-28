"""Task 6: The Garage Converter (06_garage.py)

This is the ultimate test: combining Functions, Lists, and for loops.

    Define a function called convert_top_speeds that takes one parameter: kmh_list.

    Inside the function, create an empty list called mph_list = [].

    Write a for loop to go through every speed in kmh_list.

    For each speed, divide it by 1.609 to get the mph value, and .append() that new value to your mph_list.

    After the loop finishes, return the mph_list.

    Outside the function, create a list of car speeds: jdm_speeds = [180, 250, 280]. Pass it into your function, save the result, and print it."""

def convert_top_speeds(kmh_list):
    mph_list = []
    for speed in kmh_list:
        mph_value = speed / 1.609
        mph_list.append(mph_value)
    return mph_list
jdm_speeds = [180, 250, 280]
converted_speeds = convert_top_speeds(jdm_speeds)
print(converted_speeds)