my_variable = "Hello"

#This is a list(array) in python, we can add values to it
grades_list = [89, 91, 56, 78, 100, 100]
#VALID: grades_list.append(69)

#This is a tuple, it is immutable, size cannot be increased
grades_tuple = (77, 45, 23, 100)
#INVALID: grades_tuple.append(69)

#This is a set, which means it is unique and unordered
grades_set = {45, 78, 90, 100}

print(sum(grades_list)/len(grades_list))

print("LIST: " , grades_list)
print("TUPLE: " , grades_tuple)
print("SET: " , grades_set)


#LIST MANIPULATION
#This will allow us to add to our list
grades_list.append(69)
#VALID
grades_list[0] = grades_list[0] + 3

#TUPLE MANIPULATION: A tuple cannot be changed; it's immutable, unless we make a new one from two already existing tuples.
grades_tuple = grades_tuple + (100,)
#INVALID:
#grades_tuple[0] = 25

#SET MANIPULATION: We cannot not directly index to a value here since location is unordered
#INVALID:
#grades_set[0]= 30
#This is the way we add to a set
grades_set.add(60)
grades_set.add(60)

#Comparing sets that might have the same value in the same position
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# .intersection will be use to calculate the numbers that are in both sets
print(your_lottery_numbers.intersection(winning_numbers))

# .union will be used to unite two sets together while keeping the set properties; unordered and unique
print(your_lottery_numbers.union(winning_numbers))
# .difference will find the difference values betweeb two sets
print({1, 2, 3, 4}.difference({1, 2}))
