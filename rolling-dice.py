# loop  
# ask : roll dice or not ?
# if user enter 'y' or 'Y'
#      generate two random numbers 
#      print them
# if user enter n 
#     print thanks for playing
#     Terminate
    
# else
#    invalid choice

import random
while True:
    choice = input("Roll dice (y/n): ").strip().lower()
    
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"{die1}, {die2}")
        
    elif choice == 'n':
        print("Thanks for playing")
        break
    
    else:
        print("Invaild choice")