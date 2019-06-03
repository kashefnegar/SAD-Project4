class Exam:
    def __init__(self, id):
        self.examId = id
        self.stdList = []
        # self.course = ''
        self.rooms = []

    def setTime(self, time):
        self.time = time

    def setCourse(self, course):
        self.course = course

    def addRoom(self, room):
        self.rooms.append(room)

    def addStudent(self, student, chairNumber):
        self.stdList.append([student, chairNumber])

    def getStudent(self, stdId):
        for std in self.stdList:
            if std[0].getId() == int(stdId):
                return std
        return -1

    def getProf(self, profId):
        for prof in self.course.professors:
            if prof.getProfId() == profId:
                return prof
        return -1

    def printExam(self):
        print("Exam Id : ", end=" ")
        print(self.examId, end="  +  ")
        print("Course : ", end=" ")
        self.course.printName()
        print("  +  ", end="")
        print("Rooms Number : ", end=" ")
        for room in self.rooms:
            room.printNumber()
        print()
        print("Professors: ")
        self.course.printProfessors()
        print("")
        print("")
        print("Students :")
        index = 1
        for student in self.stdList:
            print(index, end="")
            print(":")
            print("Name:", end=" ")
            student[0].printInfo()
            print("Chair:", end=" ")
            print(student[1])
            index += 1
        print("=========================================================================================================")

    def checkChair(self, chairNo):
        for item in self.stdList:
            if item[1] == int(chairNo):
                return False
        return True

    def checkId(self, id):
        for item in self.stdList:
            if item[0].getId() == int(id):
                return False
        return True