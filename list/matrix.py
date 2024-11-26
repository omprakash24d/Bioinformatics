# prompt: Write a program to print the metrics of 3*5 using a list without function

# Create a 3x5 matrix using nested lists
matrix = []
for i in range(3):
    row = []
    for j in range(5):
        row.append(i * 5 + j + 1)  # Fill with some values
    matrix.append(row)
for row in matrix:
    print(row)
    
