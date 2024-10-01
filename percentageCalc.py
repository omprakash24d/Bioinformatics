# Write a program to calculate the percentage of a student while storing the marks in list use the for loop to generate the sum of marks.

#Without Function
num_subjects = int(input("Enter the number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total_marks = 0
for mark in marks:
    total_marks += mark

percentage = (total_marks / (num_subjects * 100)) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

#with function

def calculate_percentage():
    num_subjects = int(input("Enter the number of subjects: "))
    marks = []

    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total_marks = 0
    for mark in marks:
        total_marks += mark

    percentage = (total_marks / (num_subjects * 100)) * 100

    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")

calculate_percentage()

