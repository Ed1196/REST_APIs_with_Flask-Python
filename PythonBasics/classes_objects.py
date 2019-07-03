#Dictionaries can store data, but cannot do anything; call functions
lottery_player_dict = {
    'name'    : 'Edwin',
    'numbers' : (11, 22, 23, 25, 8, 45)
}

#Classes are blueprints of what an object can have, but unlike Dictionaries
#Each individual object can have it's own identity
class lotteryPlayer:
    #Self is auto-generated for us, will refeere to the object who was created.
    #ariel and edwin are both of type lotteryPlayer, but will have different values.
    def __init__(self, name):
        self.name = name
        self.numbers = ()

    def total(self):
        return sum(self.numbers)

#Creates a new object from the blueprint self
player_one = lotteryPlayer("Edwin")
player_one.numbers = (11, 22, 23, 25, 8, 45)
print(player_one.name)
print(player_one.numbers)
print(player_one.total(), '\n')

player_two = lotteryPlayer("Ariel")
player_two.numbers = (33, 47, 89, 12, 4, 13)
print(player_two.name)
print(player_two.numbers)
print(player_two.total(), '\n')

same_player = player_one == player_two
print("Are player one and two the same? " , same_player)

same_name = player_one.name == player_two.name
print("Do the players have the same name? ", same_name, '\n')

################################################################################

#Class for a student object
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        grades = sum(self.marks)
        numOfClasses = len(self.marks)
        average = grades / numOfClasses
        return average

    #Using self as a parameter
    def go_to_my_school(self):
        print("I go to {}".format(self.school))

    #Using the class as a parameter, instead of an instance of an object
    @classmethod
    #cls: It's the class Student being passed down as a parameter
    def go_to_school(cls):
        print("I'm going to school")

    #Use static decorator if you don't want to use cls or self
    @staticmethod
    def go_to_school_static():
        print("I'm going to school")




edwin = Student("Edwin", "Hunter College")
edwin.marks.append(98)
print(edwin.name)
print(edwin.school)
print(edwin.marks)
print("Average: ", edwin.avg())
#If the method has no classmethod decorator, then we use edwin.
edwin.go_to_my_school()
#If we use the classmethod decorator, then we can use edwin or Student
edwin.go_to_school()
Student.go_to_school()
#If we use the staticmethod decorator, then we use edwin or Student
edwin.go_to_school_static()
Student.go_to_school_static()

#Whenever we use object.method(), the self of the object gets passed by default
#with no need to declare it
