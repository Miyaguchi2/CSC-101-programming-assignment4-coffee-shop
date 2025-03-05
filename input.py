import functions

if __name__ == '__main__':
    user_input = ""
    order_index_list = []
    while user_input != "close":
        while user_input != "done":
            user_input = input("Enter item number. Type 'done' when you are finished with the order, or 'close' to end the program: ")
            try:
                order_index_list.append(int(user_input))
            except ValueError:
                if user_input == "done":
                    print(order_index_list)
                    # call all functions in functions.py
                    user_input = input("Enter item number. Type 'done' when you are finished with the order, or 'close' to end the program: ")
                elif user_input == "close":
                    print("Stopping execution...")
                    exit()
                else:
                    user_input = input("Error, invalid input. enter an item number: ")
