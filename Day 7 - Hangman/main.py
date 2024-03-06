import functions
import os

input("Welcome to the HANGAME. Please press any button to continue")
os.system("cls")

word = functions.pick_word()
gameover = False
player = list("_" * len(word))
hangman = ""
test = "hangman"
c = 0

while gameover == False:
    print("Guess the word: ", end='')
    for letter in player:
        print(f"{letter} ", end='')
    
    print(f"\n\nwatch out... {hangman}\n\n")
        
    choice = input("\n\ninsert a letter: ")
    
    i=0
    check=0
    while i < len(player):
        if word[i] == choice:
            player[i] = choice
        else:
            check += 1
        i += 1
        
    if check == len(player):
        hangman += test[c]
        c += 1
    
    if c == 7:
        gameover = "you lose"
        pass
    elif "".join(player) == word:
        gameover = "you win... for now"
        pass
    

    os.system("cls")
print(gameover)