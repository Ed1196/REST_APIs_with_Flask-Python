def my_method(arg1, arg2):
    return arg1 + arg2;

print( my_method(6, 6) )

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6;

print( my_long_method(6, 5, 4, 3, 2, 1) )

def my_list_addition(list_args):
    return sum(list_args);

#Requires the use of a lists; []
print( my_list_addition([3, 3, 3, 3, 3]) )

def addition_simplify(*args):
    return sum(args)

#Does not require the use of a list; []
print(addition_simplify(4, 8, 12, 16))

#Allows us to have a list of arguments: 12, 34, 52
#it also allows us to have arguments with names: name = "Edwin" location = "US"
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['location'])

print( what_are_kwargs(12, 34, 52, name = "Edwin", location = "US") )

#Simplifying the Inheritance student

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    #def friendCLS(cls, friend_name, origin, salary):
    #this was the old method, which
    #confined us to a single field, salary. With *args, we can have multiple extra fields
    def friendArgs(self, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

    @classmethod
    def friendKwArgs(self, origin, friend_name, **kwargs):
        return cls(friend_name, origin.school, **kwargs)

class WorkingStudent(Student):
    #If an object made with this class calls the inherited function friend; then we can add
    #as many new parameters to __init__ since *args allows us to have a list of elements
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

    def printAll(self):
        print(self.name, self.school, self.salary, self.job_title)


ariel = WorkingStudent("Ariel", "Hunter", 15, "Junior Technician")
ariel.printAll()

#def __init__(self, name, school, salary, job_title)
#On this init it doesn't matter the order, it will match keywords
edwin = WorkingStudent("Edwin", "LAGCC", job_title="Nothing", salary = 20)
edwin.printAll()
