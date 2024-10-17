fin=open('abc.txt','a')
fin.write("Good Morning Om\n")
fin.close()
# print(fin)

f=open('xyz.txt','r')
# f.write('2323424354')
print(f.read())
f.close()