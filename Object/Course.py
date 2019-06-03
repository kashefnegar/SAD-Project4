class Course:
    def __init__(self, coursename):
        self.courseName = coursename
        self.professors = []

    def addProfessor(self, professor):
        self.professors.append(professor)

    def printName(self):
        print(self.courseName, end="")

    def printProfessors(self):
        for prof in self.professors:
            prof.printName()
