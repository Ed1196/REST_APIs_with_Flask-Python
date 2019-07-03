from flask import Flask, jsonify, request, render_template

#FLASK is a class
#jsonify: Method that converts a dictionary to a JSON
#__name__ gives each file a unique name
#render_template: Will allow us to render html code from our app.py
#request: When a request is made to the api, it will be passed down in this variable, will have a JSON payload
app = Flask(__name__)

#Sample data: JSON(string with dictionary format); set of key value pairs
#List
stores = [
    {
        'name': 'My Store',
        'items': [
            {
            'name': 'My Item',
            'price': 19.99
            }

        ]
    }
]

#Browser side logic:
# POST: Verb used to send data
# GET: Verb used to retrieve data

#Server side logic:
# POST: Verb used to receive data
# GET: Verb used to send data back

#Online store simulation

#Specify what requests the app will understand
@app.route('/')
def homes():
    return render_template('index.html')

# POST: /store data: {name: }                        Will create a new store, with the given {name: }
# By default app.route uses 'GET' request, you must specify others
# method=[] : Will only allow this endpoint to be hit by a 'POST' request
@app.route('/store', methods=['POST'])
def create_store():
    #get_json: Converts the json string to a Python dictionarys
    request_data = request.get_json()
    new_store = {
        #We can access the stores data as a dictionary now
        'name': request_data['name'],
        'items': []
    }
    #Add the store to the list of stores
    stores.append(new_store)
    #return the store for checking purposes as a json object
    return jsonify(new_store)

# GET: /store/<string: name>                      Will get a store given a name
#method = [] will be GET if not specified
@app.route('/store/<string:name>') #http://127.0.0.1:5000/store/some_name
def get_store(name):
    #Iterate over stores
    for store in stores:
        if(store['name'] == name):
            #If the store name matches, return it
            return jsonify(store)
    #If none match, return an error message
    return jsonify({'message': 'Store not found!'})



# GET /store                                         Will retrieve a list of stores
#It's not neccessary to specify GET, but declaring it doesnt affect anything
@app.route('/store', methods=['GET'])
def get_stores():
    #If we return stores; then its a list and not a dictionary
    #We must return it in the format {'stores': stores}
    return jsonify({'stores': stores})

# POST: /store/<string: name>/item {name:, price:}   Will create an item in an specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    #get_json : Converts a json object to a Python dictionary
    request_data = request.get_json()

    for store in stores:
        if(store['name'] == name):
            #Now we can access new_element as a Python dictionary
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message' : 'Could not find the store!'})



# GET: /store/<string: name>/item             Will get all the items in an specific store
#metho = [] will be GET if not specified
@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])

    return jsonify({'message':'item not found!'})



#Port from where the app will run from
app.run(port=5000)
