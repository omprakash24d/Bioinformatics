def find_all_occurrences(main_string, substring):
    occurrences = []   
    index = 0

    while True:
        index = main_string.find(substring, index) #if found
        
        if index == -1: #not found
            break
        
        occurrences.append(index) #added to the list
        
        index += 1 #continue finding

    return occurrences

main_string = "This is a test string. This test is only a test."
substring = "test"
occurrences = find_all_occurrences(main_string, substring)

print("Occurrences of '{}' in the string: {}".format(substring, occurrences))
