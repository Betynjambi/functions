def greet():
    print("Hello, world!")
# call the function
greet()
print('Outside function')


# function Arguments
def greet(name):
    print("Hello", name)
# pass argument
greet("John")
greet("David")


# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)
# function call with two values
add_numbers(5, 4)

# parameter
def print_age(age): # age is a parameter
    print(age)
print_age(25) # 25 is an argument


# return statement
# function definition
def find_square(num):
    result = num * num
    return result
# function call
square = find_square(3)
print('Square:', square)

# pass statament
def future_function():
    pass
# this will execute without any action or error
future_function()


# library function
import math
square_root = math.sqrt(4)
print("Square Root of 4 is", square_root)
power = pow(2, 3)
print("2 to the power 3 is", power)


# default arguments in functions
def greet(name, message="Hello"):
    print(message, name)
greet("Alice", "Good Morning") # calling function with both arguments
greet("Bob") # calling function with only one argument


# write a function to check if a given number is prime or not
# a prime no. is only divisible by 1 and itself
# return True if the number is prime, otherwise return False
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True