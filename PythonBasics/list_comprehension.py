my_list = [0, 1, 2, 3, 4]

#Different way of creating a list
#A 'for' loop will
an_equal_list = [x for x in range(5)] #an_equal_list = [0, 1, 2, 3]
print(an_equal_list)

#List that will create a list from num from a range from 0 to 9 and to the power of 2
multiply_list = [x ** 2 for x in range(10)]
print(multiply_list)

#This will create a list of even numbers
even_list = [x for x in range(20) if x%2 == 0]
print(even_list)

#Making a formatted list from a list of people
people_you_know = ["Edwin", "Ariel", "Jack"]
cleaned_list_name = [name.strip().lower() for name in people_you_know]
print(cleaned_list_name)

#Simplifying if_statement.py with list comprehension
######--METHODS--#####
def who_do_you_know():
    #Ask for a user for a list of people they known people
    list_people = input("Enter list of names separate it with a space: ")

    #Split the list by ",", remove unneccessary whitespaces and make everything lowercase 
    list_cleaned = [name.strip().lower() for name in list_people.split(",")]

    return list_cleaned
    #pass: do nothing
    pass

def ask_user(list_people):
    #Ask user for a name
    name = input("Enter a name: ")
    #See if the name is in the list of people they know
    if name in list_people:
        #Print out that they know that person
        print("You know {}".format(name))
    #pass: do nothing
    pass

######--Using Methods--######
ask_user(who_do_you_know())
