import os

def cristo(timer):
    os.system("cls")
    timer -= 1
    decision = input("Dude the view is amazing... But nothing here, You sure gonna still searching in Rio? yes or no ")
    return timer, decision

def ipanema(timer):
    os.system("cls")
    timer -= 1
    decision = input("There is A LOT of people here... i Dont think you'll find something. Still Searching in Rio? yes or no? ")
    return timer, decision

def jacarezinho(timer):
    os.system("cls")
    timer -= 1
    decision = input("I THINK... there's not a good idea... Still Searching in Rio? yes or no? ")
    return timer, decision

def rio(pais, timer, decision):
    while pais == "rio":
        if timer == 0:
            return 0, False
    
        os.system("cls")
        print("Is that BRAZILIAN FUNK? YAHOOO you're in Brazil! where do you search?")
        
        dig = input("Cristo,Ipanema or Jacarezinho? ")
        dig = dig.lower()
        ### Searching in Hawaii!!!!
        if dig == "cristo" and timer > 0:
            timer, decision = cristo(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "rio"
            
        if dig == "ipanema" and timer > 0:
            timer, decision = ipanema(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "rio"
                
        if dig == "jacarezinho" and timer > 0:
            timer, decision = jacarezinho(timer)
            if decision == "no":
                pais = "Home"
                return timer,False
            else:
                pais = "rio"