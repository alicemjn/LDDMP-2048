# Erwan Maugeri
import tkinter as tk

# initialisation de la fenêtre

racine = tk.Tk()
racine.title('2048')

# constantes et variables

SQUARE_SIDE, GRID_SPACING = 100 , 15

COLUMNS, ROWS = 4, 4 # a faire paramètrer par l'utilisateur ensuite

plateau = [[0,2,0,0], [0,0,2,0], [0,0,0,0], [2,0,0,0]] 
#              l1         l2         l3         l4
# on va pouvoir adapter dynamiquement cette liste mais pour 
# l'instant on fait une grille 4x4

# Creation de la grille

container = tk.Frame(racine, bg="#b9ada1") # contier la grille
container.grid(row=0, column=0)

inner_container = tk.Frame(container, bg="#b9ada1")
inner_container.grid(row=0, column=0, padx=7, pady=7) # permet d'avoir une bordure

frames = {} # on créer un dictionnaire pour référencer toutes les cases

for i in range(0, ROWS):
    for n in range(0, COLUMNS):
        key = f"{i},{n}"
        frames[key] = tk.Frame(inner_container, bg="#cbc0b5", height=100, width=100)
        frames[key].grid(row=i, column=n, padx=7, pady=7)

# remplissage de la grille

def fill_grid() :
    for i in range(0, ROWS):
        for n in range(0, COLUMNS):
            if plateau[i][n] != 0:
                key = f"{i},{n}"
                frames[key].config(bg="#ece4db")
                tk.Label(frames[key], text=plateau[i][n], font=("Arial", 45), fg="#756e66", bg="#ece4db").place(relx=0.5, rely=0.5, anchor="center")
                

fill_grid()

racine.mainloop()