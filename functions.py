import input

# this is used to change the menu that the program will process.
# the .txt file that is entered should have three lines, each with corresponding menu items, prices, and prep times.
# 3 lines in total

establishment = "ristorante_italia.txt"

#using the entered .txt file, initializes the three core lists for the program.
try:
    with open(establishment) as file:
        menu = file.readline().rstrip("\n").split("~")
        prices = file.readline().rstrip("\n").split("~")
        prep_time = file.readline().rstrip("\n").split("~")
except FileNotFoundError as e:
    print("Error: " + str(e))

# Prices function here



# Order number function here



# Time function here


