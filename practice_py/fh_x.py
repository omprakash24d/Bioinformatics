#import time
fin = open('C:/Users/user/Documents/practice_py/aa/1bom.pdb','rt')

#print(fin.readline())
#print(fin.readline())

file_content = fin.readlines()
print(file_content)
print(type(file_content))
print(len(file_content))
#for fline in file_content:
    #print(fline)
    #time.sleep(1)
fout = open('new2.py','w')
fout.writelines(file_content)
    
    

