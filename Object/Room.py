class Room:
    def __init__(self, roomnumber):
        self.roomNumber = roomnumber
        self.capacity = ""

    def printNumber(self):
        print(self.roomNumber, end=",")