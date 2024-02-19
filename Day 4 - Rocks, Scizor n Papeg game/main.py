import battle
import random
import os

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = True
while play == True:
    print("type \"exit\" to leave")
    choice = input("Type 0 for paper. 1 for rock or 2 for scissor ")
    if choice == "exit":
        os.system("cls")
        print("Thank you for playing!")
        break
    
    choice = int(choice)
    
    if choice >= 0 and choice < 3:
        print("You chose: \n")
        if choice == 0:
            print(paper)
        elif choice == 1:
            print(rock)
        else:
            print(scissors)

        computer_choice = random.randint(0,2)

        print("\nThe computer chose: \n")
        if computer_choice == 0:
            print(paper)
        elif computer_choice == 1:
            print(rock)
        else:
            print(scissors)

        winner = battle.battle(choice, computer_choice)

        if winner == 1:
            print("\nCongratiulations, YOU WON THE COMPUTER!")
        elif winner == 0:
            print("\nThats a tie! we are getting there")
        else:
            print("\nYou lost, the machine now rules the world")
            
    else: 
        os.system("cls")
        print("invalid number, try again")