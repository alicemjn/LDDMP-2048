# Erwan MAUGERI
# Version comme décrite sur le What's App
# Principe: déplacer bloc par bloc les nombres dans la grille

import tkinter as tk

racine = tk.Tk()

# environnement python

def afficheCarre(carre): # afficher la matric dans le terminal
    for i in range(0, len(carre)):
        print(carre[i])

# matrice
plateau = [[0,2,0,2],
           [0,0,0,16],
           [0,0,0,32],
           [4,2,2,0]]

LENGTH = 4 # nombres de colonnes

# foctions de déplacement
def gauche(event):
    for n in range(LENGTH):
        for i in range(LENGTH):
            if plateau[n][i] != 0:
                b = i
                while b>0 and plateau[n][b-1] == 0:
                    plateau[n][b-1] = plateau[n][b]
                    plateau[n][b] = 0
                    b -= 1
    # regarder si il faut combiner
    elem_a_suppr = []
    i = 0
    while i < LENGTH:
        if plateau[n][i] == plateau[n][i+1]:
            plateau[n][i] = plateau[n][i+1]
    afficheCarre(plateau)

def droite(event): 
    for n in range(LENGTH):
        for i in range(LENGTH - 1, -1, -1):
            if plateau[n][i] != 0:
                b = i
                while b < LENGTH-1 and plateau[n][b+1] == 0:
                    plateau[n][b+1] = plateau[n][b]
                    plateau[n][b] = 0
                    b += 1
    afficheCarre(plateau)

def haut(event):
    for i in range(LENGTH):
        for n in range(LENGTH):
            if plateau[n][i] != 0:
                b = n
                while b > 0 and plateau[b-1][i] == 0:
                    plateau[b-1][i] = plateau[b][i]
                    plateau[b][i] = 0
                    b -= 1
    afficheCarre(plateau)

def bas(event):
    # déplacer
    for i in range(LENGTH):
        for n in range(LENGTH - 1, -1, -1):
            if plateau[n][i] != 0:
                b = n
                while b < LENGTH - 1 and plateau[b + 1][i] == 0:
                    plateau[b+1][i] = plateau[b][i]
                    plateau[b][i] = 0
                    b += 1
    afficheCarre(plateau)

racine.bind('<Up>', haut)
racine.bind('<Left>', gauche)
racine.bind('<Right>', droite)
racine.bind('<Down>', bas)

racine.mainloop()