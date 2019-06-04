class setAttendance:
    def __init__(self):
        self.present_student = []
        self.isProfSigned = False

    def setExam(self, selectedExam):
        self.exam = selectedExam

    def addStd(self, selectedStd):
        self.present_student.append(selectedStd)

    def hasThisStd(self, student):
        for std in self.present_student:
            if std.stdCard.stdId == student.stdCard.stdId:
                return True
        return False

    def profSign(self):
        if not self.isProfSigned:
            self.isProfSigned = True
        else:
            print("# The professor has signed the roll call")
