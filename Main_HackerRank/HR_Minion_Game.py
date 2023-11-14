import numpy as n

def minion_game(string):
    
    # Cadena de caracteres siempre en mayuscula
    vocales=["A","E","I","O","U"]
    vocal_begin=[]
    consonant_begin=[]
    # Separar consonantes de vocales
    for letter in string:
        if letter in vocales:
            vocal_begin.append(letter)
        elif letter is not vocales:
            consonant_begin.append(letter)
    
    # print(vocal_begin)
    # print(consonant_begin)

# Aplicar la funcion del juego
minion_game("BANINU")