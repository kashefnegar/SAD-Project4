from Object.Cards.IdentityCard import IdentityCard
from Object.Cards.StudentCard import StudentCard


class Student:
    def __init__(self, firstname, lastname, id):
        self.stdCard = StudentCard(firstname, lastname, id)
        self.identitiyCards = []
        self.addIdentityCard(firstname, lastname)
        self.isRollCalled = False

    def addIdentityCard(self, firstname, lastname):
        self.identitiyCards.append((IdentityCard(firstname, lastname)))

    def printInfo(self):
        print(self.stdCard.firstName + " " + self.stdCard.lastName, end=" \t")
        print("Student Id: ", end="")
        print(self.stdCard.stdId, end="\t")
        print("Present: ", end="")
        print(self.isRollCalled, end="\t")

    def getId(self):
        return self.stdCard.stdId

    def setPresent(self):
        self.isRollCalled = True