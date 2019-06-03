
class Exam:
    def __init__(self, id):
        self.examId = id
        self.stdList = []
        self.start = ''
        self.end = ''
        self.course = ''
        self.rooms = []

    def setTime(self, start, end):
        self.start = start
        self.end = end

    def setCourse(self, course):
        self.course = course

    def addRoom(self, room):
        self.rooms.append(room)

    def addStudent(self, student, chairNumber):
        self.stdList.append([student, chairNumber])