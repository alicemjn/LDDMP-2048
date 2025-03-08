# Erwan
# Notes: pour tester les animations, supprimer les "#" 
# dans les parties où y'a du code "masqué"

import tkinter as tk
import random as Ashkan

# dictionnaires
colors = {
    "case": "#cbc0b5",
    "contour": "#b9ada1",

    "font": "#756e66",
    "2": "#ece4db",
    "4": "#ebe0cb",
    "2048" : "#57beec"
}

plateau = [[0,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# fonctions
def contient_zero():
    for ligne in plateau:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False

def cube():
    """ Cette fonction permet de remplir la grille tout
     en vérifiant que la place est libre pour un nouveau
      block """
    # choisir une position
    x = Ashkan.randint(0,3)
    y = Ashkan.randint(0,3)
    # vérifier si y'a déjà quelque chose dans cette case
    if plateau[y][x] == 0:
        tk.Frame(container, bg=colors["2"], height=100, width=100).grid(row=y, column=x)
        plateau[y][x] = 2
    else:
        # vérifier que la grille n'est pas pleine
        if contient_zero() == False:
            print('perdu')
        else:
            # sinon recommencer (au bout d'un momment on trouvera la place)
            cube()

# fonctions directionnelles

def haut_key(x, y, y_0):
    if y >= y_0:
        block.place(x=x, y=y)
        y -= 20
        racine.after(5, haut_key, x, y, y_0)

def haut():
    x = block.winfo_x()
    y = block.winfo_y()
    y_0 = y
    for i in range(int(y_0/100)-1, -1, -1):
        if plateau[i][int(x/100)] == 0:
            y_0 = i * 100
        else:
            break
    haut_key(x, y, y_0)
    plateau[int(y/100)][int(x/100)] = 0
    plateau[int(y_0/100)][int(x/100)] = 2

def droite_key(x, y, x_0):
    if x <= x_0:
        block.place(x=x, y=y)
        x += 20
        racine.after(5, droite_key, x, y, x_0)

def droite():
    x = block.winfo_x()
    y = block.winfo_y()
    x_0 = x
    for i in range(int(x/100)+1, len(plateau[0])):
        if plateau[int(y/100)][i] == 0:
            x_0 = i * 100
        else:
            break
    droite_key(x, y, x_0)
    plateau[int(y/100)][int(x/100)] = 0
    plateau[int(y/100)][int(x_0/100)] = 2

def gauche_key(x, y, x_0):
    if x >= x_0:
        block.place(x=x, y=y)
        x -= 20
        racine.after(5, gauche_key, x, y, x_0)

def gauche():
    x = block.winfo_x()
    y = block.winfo_y()
    x_0 = x
    for i in range(int(x/100)-1, -1, -1):
        if plateau[int(y/100)][i] == 0:
            x_0 = i * 100
        else:
            break
    gauche_key(x, y, x_0)
    plateau[int(y/100)][int(x/100)] = 0
    plateau[int(y/100)][int(x_0/100)] = 2

def bas_key(x, y, y_0):
    if y <= y_0:
        block.place(x=x, y=y)
        y += 20
        racine.after(5, bas_key, x, y, y_0)

def bas():
    x = block.winfo_x()
    y = block.winfo_y()
    y_0 = y
    for i in range(int(y_0/100)+1, len(plateau)):
        if plateau[i][int(x/100)] == 0:
            y_0 = i * 100
        else:
            break
    bas_key(x, y, y_0)
    plateau[int(y/100)][int(x/100)] = 0
    plateau[int(y_0/100)][int(x/100)] = 2

# racine
racine = tk.Tk()
racine.title('2048')

# grid
container = tk.Frame(racine, height=400, width=400, bg=colors["case"])
container.grid(row=0, column=0, columnspan=3)

for i in range(4):
    container.grid_rowconfigure(i, minsize=100)
    container.grid_columnconfigure(i, minsize=100)

#button
tk.Button(racine, text="cube", command=cube).grid(row=5, column=1)
    #commandes
tk.Button(racine, text="haut", command=haut).grid(row=6, column=1)
tk.Button(racine, text="droite", command=droite).grid(row=7, column=2)
tk.Button(racine, text="gauche", command=gauche).grid(row=7, column=0)
tk.Button(racine, text="bas", command=bas).grid(row=8, column=1)

block = tk.Frame(container, bg=colors["2048"], height=100, width=100)
block.place(x=100, y=0)

racine.mainloop()