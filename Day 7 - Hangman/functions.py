import random
import os

def pick_word():
    with open("words.txt") as arquivo:
        linhas = arquivo.readlines()

    words = []
    for linha in linhas:
        linha = linha.split(",")
        for word in linha:
            words.append(word)
            
    word = words[random.randint(0,len(words) - 1)]

    return word

def add_word():
    os.system("cls")
    new_word = input("insert your new word: ")
    with open("words.txt", "a") as arquivo:
        linhas = arquivo.writelines(f",{new_word}")