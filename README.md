# functions
A function is a block of code that performs a specific task.
Arguments are inputs given to the function.
Function reusability and dynamism are achieved by passing different arguments in each call.
Function parameters are variables inside parentheses in its definition, acting as placeholders for data the function can process during execution, outlining the expected information type.
Return a value from the function using the return statement.
The pass statement is a placeholder for future code, preventing errors from empty blocks, often used for planned but unwritten code.
We only need to call library functions in Python, not create them. Examples include print(), sqrt(), and pow(). These functions are defined in modules, requiring inclusion in our program to use them.
User-Defined Functions: Custom tools tailored for specific tasks.
Standard Library Functions: Pre-packaged tools covering common tasks, efficient and reliable.
A variable scope specifies the region where we can access a variable.
A variable created inside a function is called a local variable and can only be accessed within that function.
Change the value of a nonlocal variable, the changes appear in the local variable.
Global keyword rules:Variables created inside a function are local by default.
Variables defined outside a function are global by default.
The global keyword allows reading and writing to a global variable inside a function.
Using the global keyword outside a function has no effect.
Base condition in recursion: Recursion ends when the number reduces to 1, known as the base condition.
Every recursive function must have a base condition to prevent infinite recursion.
Importing everything with the asterisk (*) symbol is discouraged in programming. It can cause duplicate definitions for identifiers and make the code less readable.
A module is a file that contains code to perform a specific task it may contain variables, functions, classes etc
A package is a directory containing multiple modules and other sub-packages
A directory must contain a file named __init__.py in order for Python to consider it as a package. T 
