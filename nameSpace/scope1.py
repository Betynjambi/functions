Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
# Namespace and Scope
#A namespace is a collection of names.
#In Python, namespace is imagined as mapping of every name defined to corresponding onjects.
#It is used to store the values of variables and other objects in the program, and to associate them with a specific name.
#This allows us to use the same name for different variables or objects in different parts of your code, without causing any conflicts or confusion.
#A local namespace is created when a function is called, which has all the namesdefined in it.
# Each module creates its own global namespace.
# Global Namespace(Module) while local Namesapce(Function).

# Variable Scope
#A scope is the portion of a program from where a namespace can be accessed directly without any prefix.
# At any given moment, there are at least three nested scopes: 1.)Scope of the current function which has local names, 2.)Scope of the module which has global names and 3.)Outermost scope which has built-in names.
#When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.
#If there is a function inside another function, a new scope is nested inside the local scope.

#global_var is in the global namespace
global_var = 10
def outer_function():
    # outer_var is in the local namespace
    outer_var = 20

    
    def outer_function():
        # outer_var is in the local namespace
        outer_var = 20
        
SyntaxError: unexpected indent
#global_var is in the global namespace
global_var = 10
def outer_function():
    # outer_var is in the local namespace
    outer_var = 20
    def inner_function():
        # inner_var is in the nested local namespace
        inner_var = 30
        print(inner_var)
    print(outer_var)
    inner_function()
# print the value of the global variable
print(global_var)
SyntaxError: invalid syntax


# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax


# global_var is in the global namespace
global_var = 10
def outer_function():
    #  outer_var is in the local namespace
    outer_var = 20

    
  def outer_function():
      #  outer_var is in the local namespace
      outer_var = 20
      
SyntaxError: unexpected indent



# global_var is in the global namespace
global_var = 10
def outer_function():
    #  outer_var is in the local namespace
    outer_var = 20
    
SyntaxError: multiple statements found while compiling a single statement
global _var = 10
SyntaxError: invalid syntax

global_var = 10
def outer_function()|:
    
SyntaxError: expected ':'
global_var = 10
def outer_function():
    outer_var = 20
    def inner_function():
        inner_var = 30
        print(inner_var)
    print(outer_var)
    inner_function()
print(global_var)
SyntaxError: invalid syntax
global_var = 10
def outer_function():
    outer_var = 20
    def inner_function():
        inner_var = 30
        print(inner_var)
    print(outer_var)
print(global_var)
SyntaxError: invalid syntax
# USE scope2.py BY VSCode TO GET THE CORRECT ANSWER WITH NO REDUNDANT ERROR. BTW THE ANSWER IS 10, 20 & 30.