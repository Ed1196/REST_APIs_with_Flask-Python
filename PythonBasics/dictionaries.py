#Dictionaries are list, with more complex components
my_set = {1, 2, 5}

#Dictionaries will have the format "key" : "value"
#These use the "{}" set brackets, but unlike sets, we are able to access
#individual elements via their key
my_dict = {'name': 'Edwin' , 'age': 23}


lottery_player = {
    'name' : 'Edwin',
    'numbers' : (23, 11, 45, 76, 22)
}

#Accessing/Manipulating dictionary elements
lottery_player['name'] = 'Ariel'
print(lottery_player['name'])
print(sum(lottery_player['numbers']))

#This is an array/list of
colleges = [
    {
        'name' : 'Hunter College',
        'location' : 'Manhattan'
    },
    {
        'name' : 'Queens College',
        'location' : 'Queens'
    }
]

def displayAllColleges(list):
    for item in list:
        for field in item:
            print(item[field])

displayAllColleges(colleges)
