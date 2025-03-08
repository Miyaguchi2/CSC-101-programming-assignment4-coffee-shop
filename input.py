import data
import functions

if __name__ == '__main__':
    user_input = ""
    order_index_list = []
    while user_input != "done":
        user_input = input("Enter item number. Type 'done' when you are finished with the order, or 'close' to end the program: ")
        try:
            order_index_list.append(int(user_input))
        except ValueError:
            if user_input == "done":
                total_price = functions.adding_prices(order_index_list)
                total_time = functions.adding_time(order_index_list)
                order_num = functions.create_order_num()
                order = data.Order(total_price, total_time, order_num)
                print(order)
                order_index_list = []
                break
            else:
                user_input = input("Error, invalid input. enter an item number: ")
                order_index_list.append(int(user_input))
