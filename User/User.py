class User:
    def __init__(self, username, password):
        self.usernamae = username
        self.password = password
        self.isLoggedIn = False

    def login(self, username, password):
        if(self.username != username):
            print("You are not allowed to use the system")
        elif(self.password != password):
            print("The password is wrong")
        else:
            print("You are logged in")
            self.isLoggedIn = True