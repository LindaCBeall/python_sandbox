# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age)) #error if just put age - can't concatonate int
#better ways to insert variables: string formatting

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age)) #{name} is placeholder

# F-Strings (only available in python 3.6+)
print(f'Hello, my name is {name} and I am {age}') #similar to JS with $

# String Methods

s = 'helloworld'

# Capitalize string
print(s.capitalize())       #captalize =method=function

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub)) #counts number of h in string

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())        #['helloworld'], if s='hello world', then ['hello', 'world']

# Find position
print(s.find('r'))      #find position of letter r (starting with 0)

# Is all alphanumeric
print(s.isalnum())      #True, if s='hello world', then False b/c of space

# Is all alphabetic
print(s.isalpha())      #True, if s='hello world', then False b/c of space

# Is all numeric
print(s.isnumeric())    #false
