# A Tuple is a collection which is ordered and UNchangeable(as opposed to lists). Allows duplicate members.
#uses () instead of [] like lists


# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)
fruits3 = ('Apples')
print(fruits3, type(fruits3))   #Apples <class 'str">  --- if don't include trailing comma, will consider it a string
                                #Apples <class 'tuple"> --- with trailing comma
# Get value
print(fruits[1])    #Oranges

# Can't change value
fruits[0] = 'Pears'  #TypeError: 'tuple' object does not support item assignment

# Delete tuple
del fruits2     #NameError: name 'fruits2' is not defined

# Get length
print(len(fruits))     #3




# A Set is a collection which is UNordered and UNindexed. NO duplicate members.
#{}

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)   #True

# Add to set
fruits_set.add('Grape') #{'Apples', 'Oranges', 'Mango', 'Grape'}

# Remove from set
fruits_set.remove('Grape')  #{'Apples', 'Oranges', 'Mango'}

# Add duplicate
fruits_set.add('Apples')    #{'Apples', 'Oranges', 'Mango'} --- no error, just doesn't add 'Apples' twice

# Clear set
fruits_set.clear()  #set() --- returns an empty set, still have set just empty

# Delete
del fruits_set      #NameError: name 'fruits_set' is not defined

print(fruits_set)
