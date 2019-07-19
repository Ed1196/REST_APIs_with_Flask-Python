import sqlite3

connection = sqlite3.connect('data.db')
coursor = connection.cursor()

#Query for the table that needs to be made
#id has to be auto-incremented via 'INTEGER PRIMARY KEY'
create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,     name text,    price real)"


coursor.execute(create_users_table)
coursor.execute(create_items_table)

items_sample_data = "INSERT INTO items VALUES('testItem', 3.50)"

coursor.execute(items_sample_data)

#Save the changes
connection.commit()

#Close the connection
connection.close()
