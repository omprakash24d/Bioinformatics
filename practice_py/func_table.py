
x = 4/2
print(x)
x = 4%2
print(x)
#exit()


import time

def table (num): 
    for i in range (1,11,1):
        print (num," * ", i,'=',num*i)

#exit()
#for x in range (1,21,1):
    #table(x)
    ##print("\n")

#table(5)
for x in range (2,3,1):
    print('x.. = ',x)
    #time.sleep(5)
    if (x == 3):
        break
        #continue
        #pass
    for i in range (1,11,1):
        print (x," * ", i,'=',x*i)
        
    
    print("##############")
    #exit()
    


print("pass ss pass")

def add(a,b):
    #sum = 0
    sum = a + b
    #print("Sum of numbers inside =", sum)
    return sum
   
x = add(3,5)
print("Sum of numbers outside =", x)

sum1 = x + 2
print("Sum1 =", sum1)

y = [2,3]
def addition(*args):
    print(type(args))
    sum = args[0] + args[1]
    #print("Sum of numbers inside =", sum)
    return sum
   
x = addition(4,4)
print("Sum of numbers addition outside =", x)


def my_func(stu1,stu2,stu3):
    print(stu3)
#kwargs

my_func(stu1 = 'A',stu2 = 'V',stu3 = 'Z')

def my_func1(**kwargs):
    print(kwargs['age'])
    
    a_list = [kwargs['name'],kwargs['age'],kwargs['gender']]
      
    print("List inside func :",type(a_list),a_list)
    return (a_list)
    
    
my_out_list = my_func1(name = 'A',age = 21,gender = 'M/F')
print("List outside func :",type(my_out_list), my_out_list)

xc = lambda a : a * 10
print(xc(5))