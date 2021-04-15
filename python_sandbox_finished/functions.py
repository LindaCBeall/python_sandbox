# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello1(name):
    print(f'Hello {name}')
sayHello1('John Doe')   #Hello John Doe

def sayHello(name='Sam'):   #default value, doesn't require argument when you call it
    print(f'Hello {name}')
sayHello()  #Hello Sam

# Return values
def getSum(num1, num2):
    total = num1 + num2 #total=variable
    return total

getSum(1,2) #No result b/c needs print
print(getSum(1,2))  #3

num=getSum(3,4)
print(num)  #7



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2 #his prettier extension turned it into def and removed lambda


print(getSum(10, 3))    #13

