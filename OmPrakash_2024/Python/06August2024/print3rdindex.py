# Wap to print 3rd index of the string

my_name = input("Please Enter Your name:-")
thirdindex= my_name[3]
char_fromLast= my_name[::-1]
len_my_name= len(my_name)
print(f"The third index of your name is, {thirdindex} and your reverse character of your name is {char_fromLast} and your name is of {len_my_name} characters, whose last index is {my_name[-1]}")

# 1. Python program to remove character from string

character = "Om Prakash"
removecharacter ="Om"
print(character.replace(removecharacter,""))

# 4. Python program to check string is palindrome or not

string= input("Please provide the string:")
if string==string[::-1]:
    print("It is a palindrome"),
else:
    print("It is not a palindrome"),

# 5. Python code to check given character is digit or not
check_character= input("Please enter Your Name:")
if check_character >='0' and check_character >='9':
    print("It is a digit"),
else:
    print("It is a character"),
