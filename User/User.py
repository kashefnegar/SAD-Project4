class User_:
    def __init__(self):
        self.username = "k"
        self.password = "n"
        self.name = ""
        self.isLoggedIn = False

    def login(self, username, password):
        if self.username != username:
            print("# You are not allowed to use the system")
        elif self.password != password:
            print("# The password is wrong")
        else:
            print("# You are logged in")
            self.isLoggedIn = True
