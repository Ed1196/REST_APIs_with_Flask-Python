should_continue = True

if should_continue:
    print("Hello")

known_people = ["Edwin", "Ariel", "Erik", "Mayra"]
person = input("Enter the person you know: ")

#if statement will the check to see if the array contains the string via the 'in' keyword
if person in known_people:
    # .format(person) will replace the '{}' with the value of person
    print("You know {}".format(person))
else:
    # .format(person) will replace the '{}' with the value of person
    print("You don't {}".format(person))


######--METHODS--#####
def who_do_you_know():
    #Ask for a user for a list of people they known people
    list_people = input("Enter list of names separate it with a space: ")
    #Split the string into a list
    data = list_people.split(",")

    #Remove unneccessary whitespaces
    list_cleaned = []
    for name in data:
        # .strip() will remove blank spaces from the start and the ende
        list_cleaned.append(name.strip())
    #Return that list
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
