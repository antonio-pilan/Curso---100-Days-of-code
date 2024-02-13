import os

def beach(timer):
    os.system("cls")
    timer -= 1
    decision = input("You dig everywhere and nothing. Still Searching in Hawaii? yes or no? ")
    return timer, decision

def florest(timer):
    os.system("cls")
    timer -= 1
    decision = input("You walk. walk. walk. and nothing. Still Searching in Hawaii? yes or no? ")
    return timer, decision

def city(timer):
    os.system("cls")
    print("DUDE YOU JUST FOUND IT AT A GROCERY STORE!!!... it'a a... golden ticket wat?\n\n")
    return True

def hawaii(pais, timer, decision):
    while pais == "hawaii":
        if timer == 0:
            return 0, False
        
        os.system("cls")
        print("YAY, you're in Hawaii, where do you search?")
        
        dig = input("Beach,Florest or City? ")
        dig = dig.lower()
        ### Searching in Hawaii!!!!
        if dig == "beach":
            timer, decision = beach(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "hawaii"
            
        if dig == "florest":
            timer, decision = florest(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "hawaii"
                
        if dig == "city":
            winner = city(timer)
            pais = "Home"
            return 1, winner