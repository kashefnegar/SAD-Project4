
class Exam:
    def __init__(self, id):
        self.ExamId = id
        self.StdList = []

    def setTime(self, start, end):
        self.start = start
        self.end = end