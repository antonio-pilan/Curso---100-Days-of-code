import hawaii
import japan
import rio

import os

print("\n\nYou are watching your TV and you just saw in the news!\n\n"
      
      "IS TREASURE HUNTING SEASON\n\n"
      "Who find the secret treasure hidden by the BIG TECHs will earn\n" 
      "1 million dollars and a fulltime job in whatever BIG TECH you want!\n\n"
      "You pack your stuff and start hunting, it could be anywhere in one of this 5 locations: Hawaii, Japan or Rio"
      "where do you start? Remember, everyone is looking for it!\n\n")

input("Press Enter to Start")
os.system("cls")

timer = 3
winner = False

while timer != 0 and winner == False:
    
    pais = input("Hawaii, Japan or Rio. Type the name of the place you'll search  ")
    pais = pais.lower()
    change = False
    decision = "yes"
    
    if pais == "hawaii":
        timer, winner = hawaii.hawaii(pais, timer, decision)
        
    elif pais == "japan":
        timer, winner = japan.tokyo(pais, timer, decision)
        
    elif pais == "rio":
        timer, winner = rio.rio(pais, timer, decision)
        

                
if timer == 0:
    os.system("cls")
    print("Sheesh, you lost the race. Someone found the treasure first")
if winner == True:
    print("You are rich and got the best job in the world... Now go and conquer the world")