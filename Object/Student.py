from Object.Cards.IdentityCard import IdentityCard
from Object.Cards.StudentCard import StudentCard


class Student:
    def __init__(self, firstname, lastname, id):
        self.stdCard = StudentCard(firstname, lastname, id)
        self.identitiyCards = []
        self.addIdentityCard(firstname, lastname)

    def addIdentityCard(self, firstname, lastname):
        self.identitiyCards.append((IdentityCard(firstname, lastname)))
