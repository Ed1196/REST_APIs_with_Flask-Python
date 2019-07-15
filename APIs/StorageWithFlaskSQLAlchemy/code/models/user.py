import sqlite3

#THIS IS A CLASS MODEL THAT WILL BE USE TO CREATE ALL THE USERS.
#WILL REDUCE THE CODE NEEDED
class UserModel:
    def __init__(self, _id, username, password):
    #Used _id instead as id, as it is a python keyword
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findByUserName(cls, username):

        #Set up connection
        connection = sqlite3.connect('data.db')

        #Set up a coursur using the connection
        cursor = connection.cursor()

        #query that is going to be used to find the user with the given 'username'
        query = "SELECT * FROM users WHERE username=?"

        #PArameters always have to be in a form of a tuple, if only one value then do (variable,)
        result = cursor.execute(query, (username,))

        #Will fetch the first row from results, will equals none if there isn't a result
        row = result.fetchone()

        if row is not None:
            #row[0] = id, row[1] = username row[2] = password
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"

        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(*row)
        else:
            user=None

        connection.close()
        return user
