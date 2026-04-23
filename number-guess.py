# Generate the random number 
# Loop 
#    Ask user to make a guess
#    If not valid number 
#         print invalid number
#     If number <  guess
#        print too low 
#     IF number > guess
#        print too high
       
#     else 
#     print well done

import random
number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter the guess between 1 to 100: "))
        
        if guess < number:
            print("Too Low")
        
        elif guess > number:
            print("Too High")
        
        else:
            print("Well done")     
            break   
    
    except ValueError:
        print("Enter a valid number")
        
 