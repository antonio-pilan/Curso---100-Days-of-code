import string
import random

def generate_password(size):

    password = ""
    
    for i in range(1,size+1):
        n = random.randint(1,4)
        if n == 1:
            password += string.digits[random.randint(0,len(string.digits) - 1)]
        elif n == 2:
            password += string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase) - 1)]
        elif n == 3:
            password += string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase) - 1)]
        elif n == 4:
            password += string.punctuation[random.randint(0,len(string.punctuation) - 1)]
    
    return password
