my_dict = {'name': 'Om', 'age': 21}
print(my_dict.get('city'))  # returns None

my_dict = {'name': 'Om', 'age': 21}
print(my_dict.get('city', 'Not Found'))  # returns 'Not Found'

my_dict = {'name': 'Om', 'age': 21}
try:
    print(my_dict['city'])
except KeyError:
    print('Key not found')

my_dict = {'name': 'Om', 'age': 21, 'city': 'CUSB'}
print(my_dict.get('city'))  # returns 'CUSB'
