from Object.Cards.IdentityCard import IdentityCard
from Object.Cards.ProfCard import ProfCard


class Professor:
    def __init__(self, firstname , lastname, id):
        self.profCard = ProfCard(firstname, lastname, id)
        self.identitiyCards = []
        self.addIdentityCard(firstname, lastname)

    def addIdentityCard(self, firstname, lastname):
        self.identitiyCards.append((IdentityCard(firstname, lastname)))

    def getProfId(self):
        return self.profCard.profId

    def printName(self):
        print("Professor Name : ", end="")
        print(self.profCard.firstName + " " + self.profCard.lastName, end=" ")
        print("Professor Id : ", end="")
        print(self.profCard.profId)