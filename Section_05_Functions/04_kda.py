"""Task 4: The KDA Ratio Calculator (04_kda.py)

Let's build a tool that calculates your match performance in Valorant or CS:GO.

    Define a function called calculate_kda that takes three parameters: kills, deaths, and assists.

    Inside the function, calculate the ratio using the formula: (kills + assists) / deaths. (Assume deaths will always be at least 1 for now to avoid a divide-by-zero error).

    Use an if/else block inside the function:

        If the ratio is greater than or equal to 2.0, print "Top Fragger!"

        Else, print "Keep practicing."

    return the calculated ratio.

    Outside the function, call it with your stats from a recent game, save the result to a variable, and print it."""

def calculate_kda(kills, deaths, assists):
    ratio = (kills + assists) / deaths
    if ratio >= 2.0:
        print("Top Fragger!")
    else:
        print("Keep practicing.")
    return ratio
kda_ratio = calculate_kda(10, 5, 3)
print(kda_ratio)