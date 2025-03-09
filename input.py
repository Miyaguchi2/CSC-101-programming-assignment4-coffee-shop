import data
import functions

# takes the user input, (which should be index numbers) and appends it to a list
if __name__ == '__main__':
    user_input = ""
    order_index_list = []
    while user_input != "done": #while the user input does not equal the keyword "done", keep running the program.
        user_input = input("Enter item number. Type 'done' when you are finished with the order:  ")
        try:
            order_index_list.append(int(user_input))
        except ValueError: # checks for an invalid input. If the input is the keyword "done" then the functions will be called
            if user_input == "done":
                total_price = functions.adding_prices(order_index_list)
                total_time = functions.adding_time(order_index_list)
                order_num = functions.create_order_num()
                order = data.Order(total_price, total_time, order_num)
                print(order)
                order_index_list = []
            else: #if user_input is some other invalid input, then an error will pop up.
                user_input = input("Error, invalid input. enter an item number: ")
                order_index_list.append(int(user_input))
