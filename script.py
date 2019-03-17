import os
clear = os.system("clear")
clear

print("\nSimple Menu TEXT")


choice = ''


while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] HTML")
    print("[2] PHP")
    print("[3] Python")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
    # Respond to the user's choice.
    if choice == '1':
        print("\nHTML is FUN\n")
        clear
    elif choice == '2':
        print("\nHere we go Mark Zuckerberg\n")
        clear
    elif choice == '3':
        print("\nIs not a Snake \n")
        clear
    elif choice == 'q':
        print("\nThanks You. ... Have nice day.\n")
        clear
    else:
        print("\nSorry i think you wrong selected.\n")
        clear
        
# Print a message that we are all finished.
print("Thanks again, bye now.")