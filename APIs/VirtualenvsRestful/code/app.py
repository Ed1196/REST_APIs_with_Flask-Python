from flask import Flask, jsonify, request
#Resource: The resource that the Api is concernt with
from flask_restful import Resource, Api
#Will allow us use JWT with our app
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

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

#In-memory list of items
items = []


#Item becomes a class with the Resource class properties due to inheritance
#This is a resource that is only allowed to be accessed via GET
#404: Not found
#200: Most populat HTTP status code for OK
class Item(Resource):
    #Forces authentication before we reach the get method, will call the 'identity()' method from security
    @jwt_required()
    def get(self, name):
        # 'next' is a function that can be called on a filter function to get the
        # first filter object found on 'items' list.
        # if the 'next' function doesn't find anything, return 'None'
        item = next(filter(lambda x: x['name'] == name,  items ), None)
        return {'item': item}, 200 if item is not None else 404

    #201: HTTP status code that stands for an item being created.
    #400: HTTP status code that stands for Bad Request
    #We want to make sure we have unique items
    def post(self, name):
        if next(filter(lambda x: x['name'] == name , items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()
        #Request will take the data from the body of an HTTP request and convert it into a dictionary
        # data will have the fields needed to create an item; data['price'] for example
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    #Will delete an item from the list by

class ItemList(Resource):
    def get(self):
        return {'items':items}

#add_resource: adds a resource to the API
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1/student/Edwin
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
