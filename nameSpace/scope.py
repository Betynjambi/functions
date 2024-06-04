global_var = 10              #global_var is in the global namespace
def outer_function():
    outer_var = 20           #outer_var is in the local namespace
    def inner_function():
        inner_var = 30       #inner_var is in the nested local namespace
        print(inner_var)
    print(outer_var)
    inner_function()
print(global_var)            # print the value of the global variable
outer_function()             # call the outer function and print local and nested local variables


# use of global keyword
global_var = 10              # define global variable
def my_function():
    local_var = 20           # define local variable
    global global_var        # modify global variable value
    global_var = 30
print(global_var)            # print global variable value
my_function()                # call the function and modify the global variable
print(global_var)            # print the modified value of the global variable





