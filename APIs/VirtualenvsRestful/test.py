import sqlite3

#Will create a file data.db on our directory.
connection = sqlite3.connect('data.db')

#Variable that will allow us to traverse the database
cursor = connection.cursor()
#Write the query
create_table = "CREATE TABLE users (id int, username text, password text)"

#Then execute it
cursor.execute(create_table)

#Python tuple: Static data
user = (1, 'Edwin', 'password1')

#Inserting a user into the data.db
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

#Inserting multiple users into the data.db
users = [
    (2, 'Ariel', 'password2'),
    (3, 'O', 'password3')
]
#Will execute the insert query once for every item on the users list
cursor.executemany(insert_query, users)
#Query that will select everything from the table users
select_query = "SELECT * FROM users"
#cursor.execute(select_query): Will hold a list of users, making it an iterable
#row: will print each individual item on the list
for row in cursor.execute(select_query):
    print(row)


#Save the changes
connection.commit()

#Close the connection
connection.close()
