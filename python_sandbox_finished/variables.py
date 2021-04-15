#Single line comment
# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
#no ; at end in python, no var to assign variable, no int

# x = 1           # int = integer
# y = 2.5         # float
# name = 'John'   # str = string, can have single OR double quotes
# is_cool = True  # bool, must have capital T or F, not true/false

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math
a = x + y

# Casting
x = str(x)    #want to turn 1 into a string by force
y = int(y)    #turns y into an integer
z = float(y)  #won't go back to 2.5, turned into int=2, turned back into float=2

print(type(z), z)  #python3 uses ()
