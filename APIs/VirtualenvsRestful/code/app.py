from security import authenticate, identity
from flask import Flask, jsonify, request

#Resource: The resource that the Api is concernt with
#reqparse: Will allow us to parse http request for only ther data that is needed
from flask_restful import Resource, Api, reqparse

#Will allow us use JWT with our app
from flask_jwt import JWT, jwt_required

from user import UserRegister


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

    #This will parse the data before the function ever uses it and also allows us to put some
    #safeguards and restrictions on how the data is being passed down.
    #This request will stop if the json payload does not have the correct 'price' format
    #The json payload could have multiple fields, but it will only take 'price'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be left blank!')

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

        #Request will take the data from the body of an HTTP request and convert it into a dictionary
        # data will have the fields needed to create an item; data['price'] for example
        #depricated by reqparse: data = request.get_json()
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    #Will delete an item from the list by filtering out the name of the item to be removed from the list
    def delete(self, name):
        global items

        #list(): converts the iterable pass down to it, to a list
        #filter(function, iterable) takes two parameters and returns an iterable with the values that passed the fucntion check
        #items will become a list where
        #   x is each individual value from items
        #   by accessing the field 'name' via x['name']
        #   we can compare it to the 'name' that was passed down when the endpoint was called
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':'List has been updated.'}

    #Will update an item if the specified name already exists, or update it if it doesn't
    def put(self,name):

        #Request will take the data from the body of an HTTP request and convert it into a dictionary
        # data will have the fields needed to create an item; data['price'] for example
        #depricated by reqparse: data = request.get_json()
        data = Item.parser.parse_args()

        #next will return the first item that has the same name as the paremeter passed down when the endpoint is called
        #filter will iterate over items and do function x['name'] == name for all items on the items list
        item = next(filter(lambda x: x['name'] == name,items), None)
        if item is None:
            item = {'name':name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items':items, 'size':len(items)}

#add_resource: adds a resource to the API
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1/student/Edwin
api.add_resource(ItemList, '/items')
#When this endpoint gets hit, the UserRegister post method gets called
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
