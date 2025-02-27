class Order:
    def __init__(self, cost:float, time:int, order_num:str):
        self.cost = cost
        self.time = time
        self.order_num = order_num

    def __str__(self):
        return "Order Number: {}\nTotal due: ${}\nYour order will be ready in {} minutes.".format(self.order_num, self.cost, self.time)

    def __repr__(self):
        return "Order Number: {}\nTotal due: ${}\nYour order will be ready in {} minutes.".format(self.order_num, self.cost, self.time)