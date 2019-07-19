import sqlite3
from db import db



# db.Model: Extends db, tells sqlAlchemy entity that ItemModel
# will be an object that will be stored in a database.
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer,  primary_key = True)
    name = db.Column(db.String(80))
    # 5.99
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    #Return a JSON representation of a model
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        find_item = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(find_item, (name,))
        row = result.fetchone()
        connection.close()

        if row is not None:
            return cls(*row)

    def update_item(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        update_item = "UPDATE items SET price=? WHERE name=?"

        cursor.execute(update_item,(self.price, self.name ))
        connection.commit()
        connection.close()

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        store_item = "INSERT INTO items VALUES(?,?)"

        #Insert into the database
        cursor.execute(store_item,(self.name, self.price))
        connection.commit()
        connection.close()
