
import random as rd
COLS=4
ROL=4
grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

def contient_zero(grille):
    '''cette fonction verifie si toutes les cases sont remplies'''
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False           
def cube(grille):
    '''cette function affiche aleatoirement un 2 ou 4 dans la grille'''
    COLS=len(grille[0])
    ROW=len(grille)
    X0=rd.randint(0,COLS-1)
    y0=rd.randint(0,ROW-1)


    if grille[y0][X0]==0:
        grille[y0][X0]=rd.randint([2,4])
        return grille
    elif contient_zero(grille)==True:
        cube(grille)
    elif contient_zero(grille)==False:
        return "perdu"

var=cube(grille)        
if isinstance(var,list):
        for row in grille:
             print(row)

elif isinstance(var,str):
      print("perdu") 