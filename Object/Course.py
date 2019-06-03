class Course:
    def __init__(self, coursename):
        self.courseName = coursename
        self.Professors = []

    def addProfessor(self, professor):
        self.Professors.append(professor)


