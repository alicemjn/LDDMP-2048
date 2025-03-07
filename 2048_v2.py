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
    "4": "#ebe0cb"
}

plateau = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

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

#def bas(y=0):
#    if y <= 300:
#        block.place(x=0, y=y)
#        y += 20
#        racine.after(5, bas, y)

# racine
racine = tk.Tk()
racine.title('2048')

# grid
container = tk.Frame(racine, height=400, width=400, bg=colors["case"])
container.grid(row=0, column=0)

for i in range(4):
    container.grid_rowconfigure(i, minsize=100)
    container.grid_columnconfigure(i, minsize=100)

#button
tk.Button(racine, text="cube", command=cube).grid(row=5, column=0)
#tk.Button(racine, text="bas", command=bas).grid(row=6, column=0)

#block = tk.Frame(container, bg=colors["2"], height=100, width=100)
#block.place(x=0, y=0)

racine.mainloop()