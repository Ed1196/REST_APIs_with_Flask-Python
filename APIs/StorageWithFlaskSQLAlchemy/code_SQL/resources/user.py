import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

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
        if(UserModel.findByUserName(data['username']) ):
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
