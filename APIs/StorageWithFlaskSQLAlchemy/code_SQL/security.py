from werkzeug.security import safe_str_cmp

from models.user import UserModel


#TABLE LIKE DATABASE SIMULTAION
#If we have multiple mappings, we won't have to iterate over the list everytime we need a user.
users = [
    UserModel(1,'Edwin','password')
]

# 'Edwin': {
#    'id': 1
#    'username': 'Edwin'
#    }
    #This is the same as mapping by username, using set comprehension
#We can retrieve users by username
#No longer used reason='class User is now able to retrieve users from database')
username_mapping = {u.username: u for u in users}


#   1: {
#    'id': 1,
#    'username': 'Edwin',
#    'password': 'password'
#   }
    #This is the same as mapping by id, using set comprehension
#We can retrieve users by id
#No longer used reason='class User is now able to retrieve users from database')
userid_mapping = {u.id: u for u in users}


#Having different mappings immidetly allows us to access a users DATA
#by only using his id or username
    #userid_mapping[1]
    #username_mapping['Edwin']

#Authentication function that will check a username and password
#Gets triggered when we use the '/auth' endpoint
def authenticate(username, password):
    user = UserModel.findByUserName(username)
    #It is not safe to compare strings using == do to different systems and pyhton versions
    #if user is not None and password == user.password:
    if user and safe_str_cmp(password, user.password):
        return user

#JWT has a unique function 'identity(payload)'
    #payload: it's the contents of the JWT token, from where we can extract a username from
def identity(payload):
    user_id = payload['identity']
    return UserModel.findById(user_id)
