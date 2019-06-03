from Operation.InputOp import InputOp

if __name__ == "__main__":
    mainOp = InputOp()
    order = "login k n"
    mainOp.newOrder(order)
    order = "start"
    mainOp.newOrder(order)
    order = "getExamsList"
    mainOp.newOrder(order)
    # while True:
    #     print("# Enter what you want:")
    #     order = input()
    #     mainOp.newOrder(order)
    #     print("------------------------------------")
