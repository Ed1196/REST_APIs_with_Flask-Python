#DECORATOR: Functions that get called before another fucntion
import functools

#This defines our decorator
def my_decorator(func):
    @functools.wraps(func)
    #This will create a function that will wrap around the parameter function being passed down
    #This will allow us to add logic to before and after the fucntion
    def func_that_runs_func():
        #Execute before the fucntion
        print("In the decorator, before the parameter func is called!")
        #Execute the function
        func()
        #Execute after the function
        print("func has already been called!\n")
    #Will return the fucntion that will replace the function that used the @my_decorator
    return func_that_runs_func

#Here @my_decorator is applied to my_function
#my_function gets passed down to my_decorator as a parameter

@my_decorator
def my_function_1():
    print("I am the function!")

my_function_1()

#CREATING A DECORATOR WITH ARGUMENTS
#Takes in the parameter
#Requires us to go a level deeper
def decorator_with_arguments(number):
    #takes the function
    def my_decorator(func):
        #Will allow us to wrap around our function
        @functools.wraps(func)
        #Inside this function, the logic that will be used is declared
        #*args and **kwargs gives us room if arguments or key word arguments will be needed in the future
        def func_that_runs_func(*args, **kwargs):
            if number == 56:
                print("Number is 56! Execure function.")
                func(*args, **kwargs)
            else:
                print("Number is not 56! Don't execute.")
        #Return func
        return func_that_runs_func
    #Return the decorator
    return my_decorator


@decorator_with_arguments(56)
def my_function_2(x,y):
    print("I am function 2!")
    print(x + y)

my_function_2(5,6)
