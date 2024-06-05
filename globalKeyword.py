# 'global' keyword allows us to modify a variable outside the current scope, enabling changes to a global variable within a local context
# Can access but cannot modify a global variable from inside a function unless the global keyword is used
c = 1 # global variable
def add():
    print(c)
add()

# changing clobal variable from inside a function using global
c = 1
def add():
    global c # use global keyword
    c = c + 2 # increment c by 2
    print(c)
add()

# global keyword in nested functions
def outer_function():
    num = 20
    def inner_function():
        global num
        num = 25
    print("before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)
outer_function()
print("Outside both function: ", num)