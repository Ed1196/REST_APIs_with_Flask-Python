a = 5;
b = 10;
my_variable = 56;
string_single = 'Single Quotes';
string_double = "Double Quotes";
#print(string_double);

#Method Definition
def my_print_method(my_parameter):
    print(my_parameter);

#Method Call
my_print_method("Hello World!");

#Method Definition
def my_multiply_method(param_1, param_2):
    return param_1 * param_2;

#my_multiply_method will execute first, then my_print_method
#Two method calls
my_print_method(my_multiply_method(5,3));
