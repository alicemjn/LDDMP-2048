# notes de code:
# version condensé et corrigée de ce que j'ai fait précédement
# mais il manque les directions haut et bas
# pour cela trabsposer la matrice

import tkinter as tk
import mouvements as mv
import matrice as mx
import affichage as aff

# Spawn

labels = {} # pour cibler les éléments plus tard, non dynamique puisque qu'il s'agit juste de ciblage

def spawn(grille, racine, pack):
    # dimensions
    DIM = 90 # taille des boutons
    n = len(grille)
    Grid_DIM = 90*n + (n+1)*10

    # afficher le Canvas
    container = tk.Canvas(racine, width=Grid_DIM, height=Grid_DIM, bg=getattr(aff, pack)["background"], highlightthickness=0)
    container.grid(row=0, column=0, padx=0, pady=0, columnspan=3)

    #remplir le canvas
    for i in range(n):
        for j in range(n):
            # les labels
            new_Label = tk.Label(container, font=("Helvetica", 30, "bold"))
            new_Label.place(x=10 + j*(DIM+10), y=10 + i*(DIM+10), width=DIM, height=DIM)
            labels[(i,j)] = new_Label

# affichage

def afficher(grille):
    """ Cette fonction permet d'envoyer en packets le dictionnaire label et la grille vers la fonction 
    d'affichage stocké dans le fichier dédié aux fonctions d'affichage """
    aff.affichage(grille, labels, pack)

# fonctions de déplacements

DELAIS = 100 # ICI régler le délais de l'animation

def fleche(event, MAJ=None, c=0):
    assert event in ("gauche", "droite", "haut", "bas"), "La fonction ne reçoit pas cet argument"

    global grille

    if MAJ is None: # copie de grille sans pointer vers le meme espace mémoire sinon
                    # on pointe vers la meme liste à la fin (pas bien compris ça)
        MAJ = [row[:] for row in grille]
    
    if c < len(MAJ)-1:
        if event == "haut" or event == "bas":
            MAJ = mx.transpose(MAJ)
        MAJ = mv.move(event, MAJ)
        
        if event == "haut" or event == "bas":
            # créer un transpose droite/gauche
            MAJ = mx.transpose(MAJ)
            MAJ = mx.transpose(MAJ)
            MAJ = mx.transpose(MAJ)
        afficher(MAJ)
        racine.after(DELAIS, lambda: fleche(event, MAJ, c=c+1))
    else:
        if MAJ == grille:
            # meme matrice au début et à la fin
            print('pas de mouvements')
            pass
        else:
            grille = MAJ
            mx.matrice_en_int(grille)
            mx.cube(grille)
            afficher(grille)

# fonctions de vitesse de défilment (provisoire)

def lent() :
    global DELAIS
    DELAIS += 5
    texte = str(DELAIS) + " ms"
    label_vitesse.config(text=texte)

def vite() :
    global DELAIS
    DELAIS -= 5
    texte = str(DELAIS) + " ms"
    label_vitesse.config(text=texte)


# grille

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# grille pour tester les paks => (supprimer le # avant grille)
#grille = [[0,0,0,512],[2,4,8,16],[32,64,128,256],[1024,2048,4086,4096*2]]

# grosse grille 8x8 pour tester => (supprimer le # avant grille)
grille = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

# éléments visuels (tkinter)

racine = tk.Tk()
racine.title('2048')

btn1 = tk.Button(racine, text="plus lent", command=lent)
btn2 = tk.Button(racine, text="plus vite", command=vite)
texte = str(DELAIS) + " ms"
label_vitesse = tk.Label(racine, text=texte)

btn1.grid(row=1, column=2)
btn2.grid(row=1, column=0)
label_vitesse.grid(row=1, column=1)

# pack de couleurs

choix = ["default", "modern", "billard", "squid_game", "barbie"]

def change_pack():
    global pack
    current_index = choix.index(pack)
    next_index = (current_index + 1) % len(choix)
    pack = choix[next_index]
    spawn(grille, racine, pack)
    afficher(grille)

pack = "default"

btn3 = tk.Button(racine, text="changer de pack", command=change_pack)
btn3.grid(row=2, column=1)

# gestion de l'entrée

racine.bind('<Up>', lambda event: fleche('haut'))
racine.bind('<Down>', lambda event: fleche('bas'))
racine.bind('<Left>', lambda event: fleche('gauche'))
racine.bind('<Right>', lambda event: fleche('droite'))

# initialisation

mx.cube(grille)
spawn(grille, racine, pack)
afficher(grille)

# boucle

racine.mainloop()