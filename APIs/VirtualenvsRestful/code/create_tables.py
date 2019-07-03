import sqlite3

connection = sqlite3.connect('data.db')
coursor = connection.cursor()

#Query for the table that needs to be made
#id has to be auto-incremented via 'INTEGER PRIMARY KEY'
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

coursor.execute(create_table)

#Save the changes
connection.commit()

#Close the connection
connection.close()
