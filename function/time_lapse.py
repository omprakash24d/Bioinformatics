import time

def time_lapse_example():
    print("Starting time lapse...")
    
    for i in range(1, 11):  
        print(i)  
        time.sleep(1)  

    print("Time lapse completed!")

time_lapse_example()
