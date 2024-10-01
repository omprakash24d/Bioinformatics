def print_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    for row in matrix:
        print(row)  

print_matrix()

def print_matrix():
    matrix = []

    for i in range(4):  
        row = []  
        for j in range(1, 5):  
            row.append(i * 4 + j)  
        matrix.append(row)  

    for row in matrix:
        print(*row)  

print_matrix()

