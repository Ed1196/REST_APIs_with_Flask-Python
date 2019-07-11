import sqlite3
from flask_restful import Resource, reqparse

#THIS IS A CLASS MODEL THAT WILL BE USE TO CREATE ALL THE USERS.
#WILL REDUCE THE CODE NEEDED
class User:
    def __init__(self, _id, username, password):
    #Used _id instead as id, as it is a python keyword
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findByUserName(cls, username):

        parser = reqparse.RequestParser()
        parser.add_argument('username',
            type=str,
            required=True,
            help='This field cannot be left blank!')
        parser.add_argument('password',
            type=str,
            required=True,
            help='This field cannot be left blank!')


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

class UserRegister(Resource):

    #Variable that will allow us to parse the data
    parser = reqparse.RequestParser()
    #Here is where we specify the fields that we want from the payload
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field cannot be left blank!')
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field cannot be left blank!')

    def post(self):
        #We store the data that we parsed into a variable
        data = UserRegister.parser.parse_args()

        #Check if user already exists: Use the findByUserName method from User
        if(User.findByUserName(data['username']) ):
            return {'message':'User already exists'}, 409



        #Init connection to the database
        connection = sqlite3.connect('data.db')
        #Create a cursor that will allow us to traverse the database
        cursor = connection.cursor()

        #Since the id is auto-incremented, we must type NULL
        create_user = "INSERT INTO users VALUES(NULL,?,?)"
        #We use the data from the parser to create a new user
        cursor.execute(create_user, (data['username'], data['password']) )

        connection.commit()
        connection.close()

        return {'message':'User was created succesfully!'}, 201
