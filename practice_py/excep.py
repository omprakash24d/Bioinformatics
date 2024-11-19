#Exception
x = 10

#y = 10/0
#print(x)
#hex(4)
try:
    print(x)
    #y = 10/0
except NameError:
    print('An exception NameError occured')
except ZeroDivisionError:
    print('ZeroDivisionError')
finally:
    print('finally works')

x = '-1'
#if x < 0:
    #raise Exception('no value below 0')
print(type(x))

if not type(x) is str:
    raise Exception('Only strings allowed')
print('Bye Bye')