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
last = 0

while gameover == False:
    print("Guess the word: ", end='')
    for letter in player:
        print(f"{letter} ", end='')
    
    print(f"\n\nwatch out... {hangman}\n\n")
        
    choice = input("\n\ninsert a letter: ")
    
    i=0
    check=0
    while i < len(player):
        if word[i] == choice.lower():
            player[i] = choice
        else:
            check += 1
        i += 1
        
    if check == len(player):
        hangman += test[c]
        c += 1
        last = 1
    elif check != len(player):
        last = 2
    
    if c == 7:
        gameover = "you lose"
        pass
    elif "".join(player) == word:
        gameover = "you win... for now"
        pass
    

    os.system("cls")
    if last == 1:
        print("wrong...")
    elif last == 2:
        print("ok...")
    elif last == 0:
        continue
    
print("Guess the word: ", end='')
for letter in player:
    print(f"{letter} ", end='')

print(f"\n\nwatch out... {hangman}\n\n")
print(gameover)

choice = input("Would you like to add new word? y/n \n")

if choice.lower() =="y":
    functions.add_word()
    
print("See ya")
