# the __name__ variable is a special prefefined variable that represents the name of a Python file
# a directory is a collection of files and subdirectories
# a directory inside a directory is known as a subdirectory
# Python has the os module that provides many useful methods to work with directories and files 


# Exception Handling
# try...and except block
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 


# catching specific exceptions
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound


# try with else clause
# run a certain block of code if the code block inside try runs without any errors
# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
# exceptions in the else clause are not handled by the preceding except clauses


# try...finally
# the finally block is always executed no matter whether there is an exception or not
# the finally block is optional. And, for each try block, there can be only one finally block.
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")