import random

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