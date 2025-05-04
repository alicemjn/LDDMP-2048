
import random as rd
COLS=4
ROL=4
grille = [[2,4,2,4],
          [2,4,2,4],
          [2,4,2,4],
          [2,4,2,0]]

def contient_zero(grille):
    '''cette fonction verifie si toutes les cases sont remplies'''
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False

print(contient_zero(grille))