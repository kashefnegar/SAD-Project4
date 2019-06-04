class setAttendance:
    def __init__(self):
        self.presentStudents = []
        self.isProfSigned = False

    def setExam(self, selectedExam):
        self.exam = selectedExam

    def addStd(self, selectedStd):
        self.presentStudents.append(selectedStd)

    def hasThisStd(self, student):
        for std in self.presentStudents:
            if std.stdCard.stdId == student.stdCard.stdId:
                return True
        return False

    def profSign(self):
        if not self.isProfSigned:
            self.isProfSigned = True
        else:
            print("# The professor has signed the roll call")

    def getPresentList(self):
        return self.presentStudents
