from User.User import User_


class InputOp:
    def __init__(self, order):
        self.activeUser = User_()
        self.order = order
        self.defaultOrders = \
            { "login" : self.login
            }

        self.orders = order.split(" ")
        self.defaultOrders[self.orders[0]](self.orders)

    def login(self, info):
        self.activeUser.login(info[1], info[2])
