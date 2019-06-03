
class Exam:
    def __init__(self, id):
        self.ExamId = id
        self.StdList = []
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