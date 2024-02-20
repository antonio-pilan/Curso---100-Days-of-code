import os
import password_generator as pg

print("Welcome to the PyPassoword Generator")

size = input("input the password size")
os.system("cls")

password = pg.generate_password(16)
print(password)

