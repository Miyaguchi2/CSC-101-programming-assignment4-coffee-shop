from os import write

import input

# this is used to change the menu that the program will process.
# the .txt file that is entered should have three lines, each with corresponding menu items, prices, and prep times.
# 3 lines in total
establishment = "ristorante_italia.txt"

# "order_tracker.txt" keeps track of the total orders to ensure that each new order has a unique order number
order_nums = "order_tracker.txt"

#using the entered .txt file, initializes the three core lists for the program.
try:
    with open(establishment) as file:
        menu = file.readline().rstrip("\n").split("~")
        prices = file.readline().rstrip("\n").split("~")
        prep_time = file.readline().rstrip("\n").split("~")
except FileNotFoundError as e:
    print("Error: " + str(e))

# uses the order_nums variable to initialize the total_orders variable.
try:
    with open(order_nums) as file:
        total_orders = int(file.readline())
except FileNotFoundError as e:
    print("Error: " + str(e))

# Prices function here
order_list = [0,2,3]

x = 0
for idx in order_list:
    x = x + float(prices[idx])

# Order number function here
# this function outputs a unique string everytime it is called, which acts as an order number
# no input is required
def create_order_num() -> str:
    global total_orders
    with open(order_nums, "w") as file:
        file.write(str(total_orders + 1))

    if total_orders < 10:
        order_num = "00" + str(total_orders)
    elif total_orders < 100:
        order_num = "0" + str(total_orders)
    else:
        order_num = str(total_orders)

    return order_num

# Time function here


