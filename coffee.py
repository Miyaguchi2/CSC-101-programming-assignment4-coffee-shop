from operator import index

import data
from data import Order


def adding_prices(food_items:Order) -> int:
    waiter = input("What would you like to order today?")
    user_input = input()
    if user_input == food_items:
        print(food_items.time)

