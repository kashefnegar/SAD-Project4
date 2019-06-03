from Object.AttendanceList import AttendanceList
from Object.Exam import Exam
from Operation.StartAttendanceOp import StartAttendanceOp
from User.User import User_


class InputOp:
    def __init__(self):
        self.examsList = []
        self.activeUser = User_()
        self.defaultOrders = \
            {"login": self.login,
             "start": self.start,
             "getExamsList": self.getExamsList
             }
        self.isInfoGotten = False

    def newOrder(self, order):
        self.orders = order.split(" ")
        self.defaultOrders[self.orders[0]](self.orders)

    def login(self, info):
        self.activeUser.login(info[1], info[2])

    def start(self, info):
        if self.activeUser.isLoggedIn:
            self.Op = StartAttendanceOp()
            if self.Op.status == 200:
                self.isInfoGotten = True
                print("# Necessary Information is Saved")
            else:
                print("# Error Getting Information from Server")
        else:
            print("# You are not logged in")

    def getExamsList(self, info):
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
                for exam in self.Op.exams:
                    self.examsList.append(exam)
                self.printExamsList()
            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")

    def printExamsList(self):
        print(
            "=========================================== Exams List ==================================================")
        for exam in self.examsList:
            exam.printExam()
