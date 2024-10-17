#WAP to modift the existing string
name='Om Prakash'
newString= name[1:]+'Kumar'
#print(newString)
#WAP to print series even number of a string
number='123456789'
print(number[1::2])
#WAP to print series odd number of a string
print(number[2::2])
print(type(number))
print(str.lower(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.swapcase())
print(name.count("r"))
print(name.isalnum())
print(name.isdigit())
print(name.replace("O","P"))
name1='Om Pr  akash  '
name1.strip()
print(name1.strip())
print(name1.replace(" ",""))
table=5
for i in range(1,10):
	print(f"{table}*{i} = {table*i}")
print(name[::-1])
name2='Minnim'
new_name= name2[::-1]
if name2==new_name:
	print("It is a palindrome"),
else:
	print("Not a palindrome")
	
print("Done")
print(name.lower())

#prev way
line_one = "The sky has given over"
line_one_words=line_one.split().append("fyi")
print(line_one_words)

#suggested change
line_one = "The sky has given over"
line_one_words=line_one.split()
line_one_words.append("fyi")
print(line_one_words)

#new way
line_one = "The sky has given over"
line_one_words = ' '.join([line_one, 'fyi']).split()
print(line_one_words)

name34=name.lower().split()
print(name34)

