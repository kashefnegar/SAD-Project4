from Object.Cards.IdentityCard import IdentityCard
from Object.Cards.ProfCard import ProfCard


class Professor:
    def __init__(self, firstname , lastname, id):
        self.profCard = ProfCard(firstname, lastname, id)
        self.identitiyCards = []
        self.addIdentityCard(firstname, lastname)

    def addIdentityCard(self, firstname, lastname):
        self.identitiyCards.append((IdentityCard(firstname, lastname)))
