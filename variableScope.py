# local variables
# variables declared inside a function have a local scope and cannot be accessed outside the function
# variable declared outside a function is a global variable, accessible both inside and outside the function
#declare global variable
message = 'Hello'
def greet():
    #local variable
    message = 'Hello'
    print('Local', message)
greet()
# try to access message variable & outside greet() function
#print(message)
print('Global', message)


# nonlocal variables
# used in nested functions and exist outside the local and global scopes
# the 'nonlocal' keyword is used to create them
# outside function
def outer():
    message = 'local'

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal message
        
        message = 'nonlocal'
        print("inner:", message)
    inner()
    print("outer:", message)
outer()
