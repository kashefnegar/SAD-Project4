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
        print("Professors: ", end=" ")
        self.course.printProfessors()
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