# Similar to array: A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]       #variable called numbers
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))      #same result as numbers, similar to JS newarray, not as common

# Get a value
print(fruits[1])        #Oranges

# Get the last value
print(fruits[-1])       #Pears



# Get length
print(len(fruits))      #4

# Append to list
fruits.append('Mangos') #['Apples', 'Oranges', 'Grapes', 'Pears', 'Mangos']

# Remove from list
fruits.remove('Grapes') #['Apples', 'Oranges', 'Pears', 'Mangos']

# Insert into position
fruits.insert(2, 'Strawberries')    #['Apples', 'Oranges', 'Strawberries', 'Pears', 'Mangos']

# Change value
fruits[0] = 'Blueberries'       #['Blueberries', 'Oranges', 'Strawberries', 'Pears', 'Mangos']

# Remove with pop, remove by position   
fruits.pop(2)                   #['Blueberries', 'Oranges', 'Pears', 'Mangos']

# Reverse list
fruits.reverse()            #['Mangos', 'Pears', 'Oranges', 'Blueberries']

# Sort list - alphabetically
fruits.sort()       #['Blueberries', 'Mangos', 'Oranges', 'Pears']

# Reverse sort - alpha from Z to A
fruits.sort(reverse=True)   #['Pears', 'Oranges', 'Mangos', 'Blueberries']

print(fruits)   #will only print last fruits. 
