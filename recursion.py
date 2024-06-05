# recursion is the process of defining something in terms of itself
# recursive functions
# a function can call other functions
# a function can also call itself, known as recursive function
def factorial(x):
    """This is a recursive function 
    to find the factorial of an interger"""
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
num = 7
print("The factorial of", num, "is", factorial(num))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Input
num = 5
# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))



# program to find sum of natural numbers using recursive function
def recur_sum(n):
    if n == 1:
        return n
    else:
        return n + recur_sum(n-1)
# change this value for a different result
num = 7
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))


# program to display fibbonacci sequence using recursion
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
# checks if the number of terms is valid
if nterms <= 0:
    print("please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))


# adv
# recursive functions enhance code readability and elegance
# they simplify complex tasks by breaking them down into simpler sub-problems
# recursive functions facilitate sequence generation more efficiently than nested iterations
# Dis
# recursion can sometimes make the logic harder to follow.
# recursive calls are resource-intensive, consuming more memory and time.
# debugging recursive functions can be challenging.