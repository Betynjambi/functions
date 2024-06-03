# an argument is a value that is accepted by a function
# function arguments
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)
add_numbers(2,3)

# argument with default values
# assign default values to function arguments using the = operator
def add_numbers(a = 7, b = 8):
    sum = a + b
    print('Sum:', sum)
# function call with 2 arguments
add_numbers(2, 3)
# function call with 1 argument
add_numbers(a = 2)
# function call with no arguments
add_numbers()

# keyword argument
# arguments are assigned based on the name of the arguments
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('last Name:', last_name)
display_info(last_name= 'Cartman', first_name= 'Eric')

# arbitrary arguments
# arbitrary arguments let us pass a varying number of values to a function, denoted by an asterisk (*) before the parameter name
# program to find sum of multiple numbers
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum = ", result)
# function call with 3 arguments
find_sum(1, 2, 3)
# function call with 2 arguments
find_sum(4, 9)
# function call with 4 arguments
find_sum(7, 7, 7)


# Write a function to return a full name with a space in between
# For example, if the first_name is Jane and the last_name is Doe.
# The retuen value shpuld be Jane Doe.
def full_name(first_name, last_name):
    return first_name + " " + last_name
print(full_name("Jane", "Doe"))