class Course:
    def __init__(self, coursename):
        self.courseName = coursename
        self.professors = []

    def addProfessor(self, professor):
        self.professors.append(professor)


