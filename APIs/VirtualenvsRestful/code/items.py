import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items =[]

#Item becomes a class with the Resource class properties due to inheritance
#This is a resource that is only allowed to be accessed via GET
#404: Not found
#200: Most popular HTTP status code for OK
class Item(Resource):

    #This will parse the data before the function ever uses it and also allows us to put some
    #safeguards and restrictions on how the data is being passed down.
    #This request will stop, if the json payload does not have the correct 'price' format
    #The json payload could have multiple fields, but it will only take 'price'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be left blank!')

    #Forces authentication before we reach the get method, will call the 'identity()' method from security
    @jwt_required()
    def get(self, name):
        #THIS IS ALL THE SET UP NEEDED TO RETRIEVE AN ITEM FROM THE DB
        item = self.find_by_name(name)

        if item is not None:
            return item

        return {'message':'Item was not found!'}



    #201: HTTP status code that stands for an item being created.
    #400: HTTP status code that stands for Bad Request
    #We want to make sure we have unique items
    def post(self, name):
        #Check if the item is already in the database
        if self.find_by_name(name) is not None:
            return {'message':"Item '{}' already exists!".format(name)}, 400

        #Request will take the data from the body of an HTTP request and convert it into a dictionary
        # data will have the fields needed to create an item; data['price'] for example
        #depricated by reqparse: data = request.get_json()
        data = Item.parser.parse_args()

        #Create a JSON of the item
        item = {'name':name, 'price':data['price']}
        self.insert(item)


        return item, 201

    #Will delete an item from the list by filtering out the name of the item to be removed from the list
    def delete(self, name):
        item = self.find_by_name(name)

        if item is not None:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            delete_item = "DELETE FROM items WHERE name=?"
            cursor.execute(delete_item, (name,))
            connection.commit()
            connection.close()
            return {'message': 'Item succesfully deleted!'}

        return {'message':'Item was not found!'}


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

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        find_item = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(find_item, (name,))
        row = result.fetchone()

        if row is not None:
            return {'item': {'name': row[0],'price': row[1] }}

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        store_item = "INSERT INTO items VALUES(?,?)"

        #Insert into the database
        cursor.execute(store_item,(item['name'], item['price']))
        connection.commit()
        connection.close()


class ItemList(Resource):
    def get(self):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        return_items = "SELECT * FROM items"
        result = cursor.execute(return_items)
        row = result.fetch()
        if row is not None:
            items = cls(*row)
        else:
            user=None

        connection.close()
        return items
