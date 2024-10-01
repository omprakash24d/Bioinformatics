def exit_loop_on_condition():
    for number in range(1, 11):  
        if number == 5:  # Condition to exit the loop
            print("Exiting the loop at number:", number)
            break  # Exit the loop when the condition is met
        print(number)  # Print the current number


exit_loop_on_condition()
