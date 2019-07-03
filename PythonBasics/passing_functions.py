#The method gets passed down as a parameter
def methodception(another):
    #Once this fucntion gets called, the function inside it will be called right after
    return another()

#Simple function
def add_two_numbers():
    return 35 + 77

#DECLARATIVE/FUNCTIONAL PROGRAMING
#A fucntion that passes a function as a parameter
print(methodception(add_two_numbers))

#A lamda function is an anonymous function
print(methodception(lambda: 35 + 77))

my_list = [13, 45, 67, 34]
print(my_list)

#filter() takes in a function and an iterable
#function: lambda x: x!= 13
#iterable: my_list
print(list(filter(lambda x: x != 13, my_list)))

#WE CAN WRITE BOTH LAMBDA FUCNTIONS AS REGULAR FUNCTIONS
#This:
print((lambda x: x*5)(3))

#Can be written as this:
def multi(x):
    return x*5

#And used like this:
print(multi(3))

#WE CAN ALSO USE LIST COMPREHENSION INSTEAD OF THE filter() FUNCTION
#This:
list(filter(lambda x: x!=13, my_list))
#Can bew written using LIST COMPREHENSION:
print( [x for x in my_list if x != 13] )
