#THIS IS A CLASS MODEL THAT WILL BE USE TO CREATE ALL THE USERS.
#WILL REDUCE THE CODE NEEDED
class User:
    def __init__(self, _id, username, password):
    #Used _id instead as id, as it is a python keyword
        self.id = _id
        self.username = username
        self.password = password
