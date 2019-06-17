#Dictionaries can store data, but cannot do anything; call functions
lottery_player_dict = {
    'name'    : 'Edwin',
    'numbers' : (11, 22, 23, 25, 8, 45)
}

#Classes are blueprints of what an object can have, but unlike Dictionaries
#Each individual object can it's own identity
class lotteryPlayer:
    #Self is auto-generated for us
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

edwin = Student("Edwin", "Hunter College")
edwin.marks.append(98)
print(edwin.name)
print(edwin.school)
print(edwin.marks)
print("Average: ", edwin.avg())
