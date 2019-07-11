from security import authenticate, identity
from flask import Flask, jsonify, request

#Resource: The resource that the Api is concernt with
#reqparse: Will allow us to parse http request for only ther data that is needed
from flask_restful import Resource, Api, reqparse

#Will allow us use JWT with our app
from flask_jwt import JWT, jwt_required

from user import UserRegister
from items import Item, ItemList


app = Flask(__name__)
#Api: Allow us to add/remove/update resources, all have to be a class
api = Api(app)

#Key that will be use for decryption
app.secret_key = 'Edwin'

#JWT: Will create a new endpoint
    #we send JWT a user name and a password
        #then it will call the authenticate method
        #if authentication is good, a JWT token will be sent back and stored in jwt
    #JWT will only use the identity function when it sends a JWT token
jwt = JWT(app, authenticate, identity)  # /auth

#add_resource: adds a resource to the API
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1/student/Edwin
api.add_resource(ItemList, '/items')
#When this endpoint gets hit, the UserRegister post method gets called
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
