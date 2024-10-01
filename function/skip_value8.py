def print_even_numbers_skipping_eight():
    for number in range(1, 11):  
        if number % 2 == 0:
            if number == 8:  
                continue
            print(number)  

print_even_numbers_skipping_eight()

#total class: 50
# absent=7
