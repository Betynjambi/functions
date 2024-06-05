# Modules
# is a file that contains code to perform a specific task it may contain variables, functions, classes etc
# module addition
import math
print("The value of pi is", math.pi)

# import with remaining 
import math as m
print(m.pi)

# from...import statement
from math import pi
print(pi)

# import all names
from math import *
print("The value of pi is", pi)

import math
print(dir(math))