#Iterable: strings, sets, lists, tuples and more

my_string = "Hello"

#######--FOR LOOPS--#########

#   index    iterable
for char in my_string:
    print(char)

numbers = [3, 4, 7, 2, 9]

#  index  iterable
for num in numbers:
    # **: is the same as taking a number to the power of 2
    print(num ** 3)

#######--WHILE LOOPS--#########
continue_printing = True;
while continue_printing == True:
    print(10)
    continue_printing = input("Do you wish to continue?(Y/N)")
    if(continue_printing == 'Y'):
        continue_printing = True
    elif(continue_printing == 'N'):
        continue_printing = False
    else:
        print("Wrong input!")
        continue_printing = True
