def battle(choice, computer_choice):
    #0 paper
    #1 rock
    #2 scissor
    if choice == computer_choice:
        return 0
    
    elif choice == 0:
        if computer_choice == 1:
            return 1
        else:
            return -1
    
    elif choice == 1:
        if computer_choice == 2:
            return 1
        else:
            return -1
        
    elif choice == 2:
        if computer_choice == 0:
            return 1
        else:
            return -1 