from Object.Student import Student
from Operation.StartAttendanceOp import StartAttendanceOp
from User.User import User_


class InputOp:
    def __init__(self):
        self.examsList = []
        self.activeUser = User_()
        self.defaultOrders = \
            {"login": self.login,
             "start": self.start,
             "getExamsList": self.getExamsList,
             "getExamList": self.getExamList,
             "getStudentInfo": self.getStudentInfo,
             "getProfInfo": self.getProfInfo,
             "addStudent": self.addStudent,
             }
        self.isInfoGotten = False
        self.isExamSelected = False
        self.isStdSelected = False
        self.isProfSelected = False

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

    def getExamList(self, info):
        self.isExamSelected = False
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
                for exam in self.Op.exams:
                    if exam.examId == int(info[1]):
                        print(
                            "============================================ Exam Info ==================================================")
                        self.selectedExam = exam
                        self.selectedExam.printExam()
                        self.isExamSelected = True

                if not self.isExamSelected:
                    print("# No exam with this id was found")

            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")

    def getStudentInfo(self, info):
        self.isStdSelected = False
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
                if self.isExamSelected:
                    std = self.selectedExam.getStudent(info[1])
                    if std != -1:
                        self.isStdSelected = True
                        print(
                            "=========================================== Student Info ================================================")
                        print("Student Name :", end="")
                        std[0].printInfo()
                        print("Chair Number :", end="")
                        print(std[1])
                        print(
                            "=========================================================================================================")
                    else:
                        print("# Student not found")
                        print("# Do you want to add student manually?[Y/N]")
                        answer = input()
                        if answer == 'y' or answer == 'Y':
                            self.newOrder("addStudent")

                else:
                    print("# No exam is selected")
            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")

    def getProfInfo(self, info):
        self.isProfSelected = False
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
                if self.isExamSelected:
                    prof = self.selectedExam.getProf(info[1])
                    if prof != -1:
                        self.isProfSelected = True
                        print(
                            "========================================== Professor Info ===============================================")
                        prof.printName()
                        print(
                            "=========================================================================================================")
                    else:
                        print("# Professor not found")
                else:
                    print("# No exam is selected")
            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")

    def addStudent(self, info):
        print("# Enter student first name:")
        firstname = input()
        print("# Enter student last name:")
        lastname = input()
        print("# Enter student id:")
        id = input()
        print("# Enter student chair number:")
        chairNumber = input()

        if self.selectedExam.checkChair(chairNumber) and self.selectedExam.checkId(id):
            print("# Does the professor accept this:[Y/N]")
            answer = input()
            if answer == 'y' or answer == 'Y':
                std = Student(firstname, lastname, id)
                self.selectedExam.addStudent(std, chairNumber)
        else:
            print("# Check entered information")