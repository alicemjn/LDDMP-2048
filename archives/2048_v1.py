# Erwan Maugeri
import tkinter as tk
import random as Ashkan

# initialisation de la fenêtre

racine = tk.Tk()
racine.title('2048')

# constantes et variables

SQUARE_SIDE, GRID_SPACING = 100 , 15

COLUMNS, ROWS = 4, 4 # a faire paramètrer par l'utilisateur ensuite

plateau = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
#              l1         l2         l3         l4
# on va pouvoir adapter dynamiquement cette liste mais pour 
# l'instant on fait une grille 4x4

frames = {} # on créer un dictionnaire pour référencer toutes les cases

couleurs = {
    "2": "#ece4db",
    "4": "#ebe0cb"
}

# Fonctions

def random_fill() :
    i, n = Ashkan.choice([(i, n) for i in range(4) for n in range(4) if plateau[i][n] == 0])
    plateau[i][n] = 2

def fill_grid() :
    for i in range(0, ROWS):
        for n in range(0, COLUMNS):
            key = f"{i},{n}"
            frames[key].config(bg="#cbc0b5")
            if frames[key].winfo_children(): # Vérifie s'il y a des enfants et les supprimes
                list(frames[key].winfo_children())[0].destroy()
            if plateau[i][n] != 0:
                frames[key].config(bg=couleurs[str(plateau[i][n])])
                tk.Label(frames[key], text=plateau[i][n], font=("Arial", 45), fg="#756e66", bg=couleurs[str(plateau[i][n])]).place(relx=0.5, rely=0.5, anchor="center")

def supprime_0() :
    #supprimer tt les 0
    for i in range(0, ROWS):
        while 0 in plateau[i]:
            plateau[i].remove(0)

def gauche() :
    #supprimer tt les 0
    supprime_0()
    # combiner
    for i in range(0, ROWS):
        if len(plateau[i]) > 1:
            if plateau[i][0] == plateau[i][1]:
                plateau[i][0] = plateau[i][0]*2
                plateau[i].pop(1)
    #remmetre les 0 à la fin
    for i in range(0, ROWS):
        while len(plateau[i]) != ROWS:
            plateau[i].append(0)
    # mettre à jour la grille
    random_fill()
    fill_grid()

def droite() :
    #supprimer tt les 0
    supprime_0()
    # combiner
    for i in range(0, ROWS):
        if len(plateau[i]) > 1:
            if plateau[i][-1] == plateau[i][-2]:
                plateau[i][-1] = plateau[i][-1]*2
                plateau[i].pop(-2)
    #remmetre les 0 au début
    for i in range(0, ROWS):
        while len(plateau[i]) != ROWS:
            plateau[i].insert(0, 0)
    # mettre à jour la grille
    random_fill()
    fill_grid()

# Creation de la grille

container = tk.Frame(racine, bg="#b9ada1") # contier la grille
container.grid(row=0, column=0, columnspan=2)

inner_container = tk.Frame(container, bg="#b9ada1")
inner_container.grid(row=0, column=0, padx=7, pady=7) # permet d'avoir une bordure

buttonL = tk.Button(racine, text="gauche", command=gauche)
buttonR = tk.Button(racine, text="droite", command=droite)
buttonL.grid(column=0, row=1)
buttonR.grid(column=1, row=1)

for i in range(0, ROWS):
    for n in range(0, COLUMNS):
        key = f"{i},{n}"
        frames[key] = tk.Frame(inner_container, bg="#cbc0b5", height=100, width=100)
        frames[key].grid(row=i, column=n, padx=7, pady=7)

# remplissage de la grille

random_fill()
fill_grid()

racine.mainloop()