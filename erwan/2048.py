# Erwan MAUGERI
# code

import tkinter as tk
import random as Ashkan
import time

# interface

racine = tk.Tk()

btn1 = tk.Label(racine, text="")
btn2 = tk.Label(racine, text="")
btn3 = tk.Label(racine, text="")
btn4 = tk.Label(racine, text="")

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=0)
btn3.grid(row=2, column=0)
btn4.grid(row=3, column=0)

# paramètres de base

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,2,2,4]]

LENGHT, DELAIS = 4, 60

# fonctions

def afficheCarre(carre): # afficher la matrice dans la fenetre
    btn1.config(text=carre[0])
    btn2.config(text=carre[1])
    btn3.config(text=carre[2])
    btn4.config(text=carre[3])

def ajouter_zero_col(n, position):
    grille[n].insert(position, 0)

def matrice_en_int():
    for n in range(len(grille)):  # Parcours des lignes
        for i in range(len(grille[n])):  # Parcours des colonnes
            if isinstance(grille[n][i], str):  # Vérifie si c'est une string
                grille[n][i] = int(grille[n][i])  # Convertit en int

dernier_appel = 0
spam_delay = 0.1 # Délai en secondes

def peut_executer():
    global dernier_appel
    actuel = time.time()
    if actuel - dernier_appel >= spam_delay:  # Vérifie si assez de temps s'est écoulé
        dernier_appel = actuel
        return True
    return False

def contient_zero():
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False

def cube():
    """ Cette fonction permet de remplir la grille tout
     en vérifiant que la place est libre pour un nouveau
      block """
    # choisir une position
    x = Ashkan.randint(0,LENGHT-1)
    y = Ashkan.randint(0,LENGHT-1)
    # vérifier si y'a déjà quelque chose dans cette case
    if grille[y][x] == 0:
        grille[y][x] = 2
    else:
        # vérifier que la grille n'est pas pleine
        if contient_zero() == False:
            print('perdu')
        else:
            # sinon recommencer (au bout d'un momment on trouvera la place)
            cube()

# fonctions de déplacement

def droite(c=0):
    if c < 4:
        for n in range(LENGHT):
            i = 1
            while i < LENGHT:
                if grille[n][LENGHT-i] == 0 or grille[n][LENGHT-i-1] == 0: # avant dernière ou dernière = 0 ?
                    grille[n][LENGHT-i] = int(grille[n][LENGHT-i]) + int(grille[n][LENGHT-1-i]) # on additionne avant dernière et dernière
                    grille[n].pop(LENGHT-1-i) # on supprime avant dernière
                    ajouter_zero_col(n, 0) # on ajoute des 0 à la fin pour garder la meme taille
                    i = LENGHT
                elif grille[n][LENGHT-i] == grille[n][LENGHT-1-i] and isinstance(grille[n][LENGHT-1-i], int): # avant dernière = dernière ?
                    grille[n][LENGHT-i] = str(grille[n][LENGHT-i] + grille[n][LENGHT-1-i]) # on additionne avant dernière et dernière ET on bloque la valeur
                    grille[n].pop(LENGHT-1-i) # on supprime avant dernière
                    ajouter_zero_col(n, 0) # on ajoute des 0 à la fin pour garder la meme taille
                    i = LENGHT
                i += 1
        c += 1
        afficheCarre(grille)
        racine.after(DELAIS, droite, c)
    else:
        matrice_en_int() # débloque toutes les valeurs
        cube()
        afficheCarre(grille)

def gauche(c=0):
    if c < 4:
        for n in range(LENGHT):
            i = 0
            while i < LENGHT-1:
                if grille[n][i] == 0 or grille[n][i+1] == 0:
                    grille[n][i] = int(grille[n][i]) + int(grille[n][i+1]) # on add 1ere et 2eme
                    grille[n].pop(i+1) # on supprime avant dernière
                    ajouter_zero_col(n, LENGHT-1) # on ajoute des 0 à la fin pour garder la meme taille
                    i = LENGHT
                elif grille[n][i] == grille[n][i+1] and type(grille[n][i])== int: # 2eme = 1ere ?
                    grille[n][i] = str(grille[n][i] + grille[n][i+1]) # on additionne avant 2eme et 1ere ET on bloque la valeur
                    grille[n].pop(i+1) # on supprime 2eme
                    ajouter_zero_col(n, LENGHT-1) # on ajoute des 0 à la fin pour garder la meme taille
                    i = LENGHT
                i += 1
        c += 1
        afficheCarre(grille)
        racine.after(DELAIS, gauche, c)
    else:
        matrice_en_int() # débloque toutes les valeurs
        cube()
        afficheCarre(grille)

##

def haut(c=0):
    if c < 4:
        for n in range(LENGHT):
            i = 0
            while i < LENGHT - 1:
                if grille[i][n] == 0 or grille[i+1][n] == 0:
                    grille[i][n] = int(grille[i][n]) + int(grille[i+1][n])  # Additionne case du haut et celle du dessous
                    for k in range(i+1, LENGHT-1):  # Décale la colonne vers le haut
                        grille[k][n] = grille[k+1][n]
                    grille[LENGHT-1][n] = 0  # Ajoute un 0 en bas
                    i = LENGHT  # Sortie de boucle
                elif grille[i][n] == grille[i+1][n] and isinstance(grille[i][n], int):
                    grille[i][n] = str(grille[i][n] + grille[i+1][n])  # Fusion et blocage
                    for k in range(i+1, LENGHT-1):
                        grille[k][n] = grille[k+1][n]
                    grille[LENGHT-1][n] = 0
                    i = LENGHT
                i += 1
        c += 1
        afficheCarre(grille)
        racine.after(DELAIS, haut, c)
    else:
        matrice_en_int()
        cube()
        afficheCarre(grille)

def bas(c=0):
    if c < 4:
        for n in range(LENGHT):
            i = LENGHT - 1
            while i > 0:
                if grille[i][n] == 0 or grille[i-1][n] == 0:
                    grille[i][n] = int(grille[i][n]) + int(grille[i-1][n])  # Additionne case du bas et celle du dessus
                    for k in range(i-1, 0, -1):  # Décale la colonne vers le bas
                        grille[k][n] = grille[k-1][n]
                    grille[0][n] = 0  # Ajoute un 0 en haut
                    i = 0  # Sortie de boucle
                elif grille[i][n] == grille[i-1][n] and isinstance(grille[i][n], int):
                    grille[i][n] = str(grille[i][n] + grille[i-1][n])  # Fusion et blocage
                    for k in range(i-1, 0, -1):
                        grille[k][n] = grille[k-1][n]
                    grille[0][n] = 0
                    i = 0
                i -= 1
        c += 1
        afficheCarre(grille)
        racine.after(DELAIS, bas, c)
    else:
        matrice_en_int()
        cube()
        afficheCarre(grille)

# appel des fonctions

def bouge_droite(event):
    if peut_executer():
        droite()
        

def bouge_gauche(event):
    if peut_executer():
        gauche()


def bouge_haut(event):
    if peut_executer():    
        haut()

def bouge_bas(event):
    if peut_executer():
        bas()

# jeu

cube()
afficheCarre(grille)

racine.bind('<Up>', bouge_haut)
racine.bind('<Left>', bouge_gauche)
racine.bind('<Right>', bouge_droite)
racine.bind('<Down>', bouge_bas)

racine.mainloop()