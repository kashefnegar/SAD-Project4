class Course:
    def __init__(self, coursename):
        self.courseName = coursename
        self.Professors = []

    def setProfessor(self, professor):
        self.Professors.append(professor)


