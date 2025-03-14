# Erwan
# Notes: NE PAS MODIFIER MON CODE SVP !!
#        -> créer un nouveau fichier Python_vi et copier coller ce code











# >>>>>>>>>  NE PAS MODIFIER MON CODE SVP !! <<<<<<<<<<<<<<












import tkinter as tk
import random as Ashkan
import time

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

# fonctions de delais car si on spam les flèches ça se marche dessus

dernier_appel = 0
delai = 0.1 # Délai en secondes

def peut_executer():
    global dernier_appel
    actuel = time.time()
    if actuel - dernier_appel >= delai:  # Vérifie si assez de temps s'est écoulé
        dernier_appel = actuel
        return True
    return False

# fonctions directionnelles

key_interval, key_delay = 20, 5 # 20, 5 pour une animation fluide

def haut_key(x, y, y_0):
    if y >= y_0:
        block.place(x=x, y=y)
        y -= key_interval
        racine.after(key_delay, haut_key, x, y, y_0)

def haut(event):
    if peut_executer():
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
        x += key_interval
        racine.after(key_delay, droite_key, x, y, x_0)

def droite(event):
    if peut_executer():
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
        x -= key_interval
        racine.after(key_delay, gauche_key, x, y, x_0)

def gauche(event):
    if peut_executer():
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
        y += key_interval
        racine.after(key_delay, bas_key, x, y, y_0)

def bas(event):
    if peut_executer():
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

# grille
container = tk.Frame(racine, height=400, width=400, bg=colors["case"])
container.grid(row=0, column=0, columnspan=3)

for i in range(4):
    container.grid_rowconfigure(i, minsize=100)
    container.grid_columnconfigure(i, minsize=100)

#button
tk.Button(racine, text="cube", command=cube).grid(row=5, column=1)
    
#commandes
racine.bind('<Up>', haut)
racine.bind('<Left>', gauche)
racine.bind('<Right>', droite)
racine.bind('<Down>', bas)

def touche_cube(event):
    cube()

racine.bind('c', touche_cube)

#label de tuto
tk.Label(racine, text="Utiliser les flèches directionnelles pour déplacer le cube bleu", wraplength=400, justify="left").grid(row=6, column=1)
tk.Label(racine, text='Appuyer sur "cube" pour placer des cubes aléatoirement sur le grille', wraplength=400, justify="left").grid(row=7, column=1)
tk.Label(racine, text='Un delais entre les clicks est imposé pour éviter de faire crash le jeu et que les appels à fonctions se supperposent', wraplength=400, justify="left").grid(row=8, column=1)

#le block bleu
block = tk.Frame(container, bg=colors["2048"], height=100, width=100)
block.place(x=100, y=0)

##
racine.mainloop()