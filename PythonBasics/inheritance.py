
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    #When this gets inherited, then only Student fields and functions are available
    def friend(self, friend_name):
        return Student(friend_name, self.school)

    #This method will replace cls with the function that called it; either Student or WorkingStudent
    @classmethod
    def friendCLS(cls, friend_name, origin, salary):
        return cls(friend_name, origin.school,salary)

#Initial student
edwin = Student("Edwin", "Hunter")
#Student created from the friend() fucntion, from Student
newStudent1 = edwin.friend("Ariel")

print(newStudent1.name, " ", newStudent1.school)

#Inheritance: The WorkingStudent class will have all the methods and fields that
#the class Student will have.
class WorkingStudent(Student):
    #the __init__ can be re-implemented with more parameters
    def __init__(self, name, school, salary):
        #Student is a super class, since it's the class WorkingStudent is being derived from.
        super().__init__(name, school)
        self.salary = salary

#When we create an instance of WorkingStudent, then we can use the same methods
#as when working with student
ariel = WorkingStudent("Ariel", "LAGCC", 15.00)
print(ariel.name, " ", ariel.school, " ", ariel.salary)

newStudent2 = ariel.friend("Ariel")
#.name and .school are the only fields that are available in Student
#.salary is not available: newStudent2.salary.
#WorkingStudent does have a field .salary, but the method friend() still just
#returns a new Student object with just the .name and .school fields
print(newStudent2.name, " ", newStudent2.school)

#This object will use the function with the @classmethod decorator
#friendCLS will use the class that called it as the class that will be used as
#a template to create the new object.
newStudent3 = ariel.friendCLS("Edwin", ariel, 15.50)
print(newStudent3.name, " ", newStudent3.school, " ", newStudent3.salary)
