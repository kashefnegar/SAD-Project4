from Operation.InputOp import InputOp

if __name__ == "__main__":
    mainOp = InputOp()
    order = "login k n"
    mainOp.newOrder(order)
    order = "start"
    mainOp.newOrder(order)
    # order = "getExamsList"
    # mainOp.newOrder(order)
    order = "getExamList 2012"
    mainOp.newOrder(order)
    order = "getStudentInfo 1008"
    mainOp.newOrder(order)
    # order = "getStudentInfo 1008"
    # mainOp.newOrder(order)
    order = "getExamList 2012"
    mainOp.newOrder(order)
    # order = "getStudentInfo 1001"
    # mainOp.newOrder(order)
    # order = "getProfInfo 12312"
    # mainOp.newOrder(order)
    # order = "getExamList 2012"
    # mainOp.newOrder(order)
    # while True:
    #     print("# Enter what you want:")
    #     order = input()
    #     mainOp.newOrder(order)
    #     print("------------------------------------")
