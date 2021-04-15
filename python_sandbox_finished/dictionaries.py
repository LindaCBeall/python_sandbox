# A Dictionary is a collection which is UNordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))     #{'first_name': 'John', 'last_name': 'Doe', 'age': 30} <class 'dict'>

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')   = instead of :

# Get value
print(person['first_name'])     #John, in JS would be person.first_name
print(person.get('last_name'))  #Doe, same as above but less common

# Add key/value
person['phone'] = '555-555-5555'    #{'first_name': 'John','last_name': 'Doe','age': 30,'phone' : '555-555-5555'}


# Get dict keys
print(person.keys())    #dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get dict items
print(person.items())   #dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30), ('phone', '555-555-5555')])

# Copy dict
person2 = person.copy() #copies person into person2, similar to JS spread
person2['city'] = 'Boston'
print(person2)  #{'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '555-555-5555', 'city': 'Boston'}

# Remove item
del(person['age'])
person.pop('phone') #alternate method to remove
print(person)   #{'first_name': 'John', 'last_name': 'Doe'}

# Clear
person.clear()
print(person)   #{}

# Get length
print(len(person2)) #5 key value pairs in person2




# List [] of dict {}
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])    #Kevin
