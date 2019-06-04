from Object.Student import Student
from Operation.StartAttendanceOp import StartAttendanceOp
from Operation.setAttendance import setAttendance
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
             "deleteStudent": self.deleteStudent,
             "rollCallStudent": self.rollCallStudent
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

                        temp = setAttendance()
                        temp.setExam(self.selectedExam)
                        self.Op.attendance.append(temp)

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
                    self.selectedStd = self.selectedExam.getStudent(info[1])
                    if self.selectedStd != -1:
                        self.isStdSelected = True
                        print(
                            "=========================================== Student Info ================================================")
                        print("Student Name :", end="")
                        self.selectedStd[0].printInfo()
                        print("Chair Number :", end="")
                        print(self.selectedStd[1])
                        print(
                            "=========================================================================================================")
                        print("# Is the information correct?[Y/N]")
                        answer = input()
                        if answer == 'y' or answer == 'Y':
                            self.newOrder("rollCallStudent")
                        else:
                            self.isStdSelected = False
                            print("# The Information for this student is wrong")
                            print("# Do you want to delete it from list?[Y/N]")
                            answer = input()
                            if answer == 'y' or answer == 'Y':
                                self.newOrder("deleteStudent " + info[1])

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
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
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
            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")

    def rollCallStudent(self, info):
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
                if self.isStdSelected and self.isExamSelected:
                    print("# Accept roll call?[Y/N]")
                    answer = input()
                    if answer == 'y' or answer == 'Y':
                        if not self.Op.findAttendance(self.selectedExam).hasThisStd(self.selectedStd[0]):
                            self.selectedStd[0].setPresent()
                            self.Op.findAttendance(self.selectedExam).addStd(self.selectedStd[0])
                        else:
                            print("# This student has been added")
                elif not self.isExamSelected:
                    print("# No exam is selected")
                else:
                    print("# No student is selected")
            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")

    def deleteStudent(self, info):
        if self.activeUser.isLoggedIn:
            if self.isInfoGotten:
                if self.isExamSelected:
                    self.selectedExam.deleteStd(info[1])
                else:
                    print("# No exam is selected")
            else:
                print("# You need to enter 'start' first")
        else:
            print("# You are not logged in")
