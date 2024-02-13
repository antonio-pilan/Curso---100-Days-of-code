import os

def shibuya(timer):
    os.system("cls")
    timer -= 1
    decision = input("Apparently Mahito is going crazy, You sure gonna still searching in Japan? yes or no ")
    return timer, decision

def shinjuku(timer):
    os.system("cls")
    timer -= 1
    decision = input("Dude you read the manga, Satoru Gojo is about to use the craziest PURPLE ever seen. Still Searching in Japan? yes or no? ")
    return timer, decision

def fuji(timer):
    os.system("cls")
    timer -= 1
    decision = input("I THINK... there's another place with a great vulcan... Still Searching in Japan? yes or no? ")
    return timer, decision

def tokyo(pais, timer, decision):
    while pais == "japan":
        if timer == 0:
            return 0, False
    
        os.system("cls")
        print("OKAERI... Now you're in Tokyo! where do you search?")
        
        dig = input("Shibuya,Shinjuku or Fuji? ")
        dig = dig.lower()
        ### Searching in Hawaii!!!!
        if dig == "shibuya" and timer > 0:
            timer, decision = shibuya(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "japan"
            
        if dig == "shinjuku" and timer > 0:
            timer, decision = shinjuku(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "japan"
                
        if dig == "fuji" and timer > 0:
            timer, decision = fuji(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "japan"