# notes de code:
# version condensé et corrigée de ce que j'ai fait précédement
# mais il manque les directions haut et bas
# pour cela trabsposer la matrice

import tkinter as tk
import mouvements as mv
import matrice as mx

# affichage de la matrice

def afficher(grille):
    # afficher la matrice dans le terminal
    for line in grille:
        print(line)
    # afficher la matrice dans la fenetre tkinter
    btn1.config(text=grille[0])
    btn2.config(text=grille[1])
    btn3.config(text=grille[2])
    btn4.config(text=grille[3])

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
        racine.after(100, lambda: fleche(event, MAJ, c=c+1))
    else:
        if MAJ == grille:
            # meme matrice au début et à la fin
            #print('pas de mouvements')
            pass
        else:
            grille = MAJ
            mx.matrice_en_int(grille)
            mx.cube(grille)
            afficher(grille)

# grille

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# éléments visuels (tkinter)

racine = tk.Tk()
racine.title('2048')

btn1 = tk.Label(racine, text="")
btn2 = tk.Label(racine, text="")
btn3 = tk.Label(racine, text="")
btn4 = tk.Label(racine, text="")

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=0)
btn3.grid(row=2, column=0)
btn4.grid(row=3, column=0)

racine.bind('<Up>', lambda event: fleche('haut'))
racine.bind('<Down>', lambda event: fleche('bas'))
racine.bind('<Left>', lambda event: fleche('gauche'))
racine.bind('<Right>', lambda event: fleche('droite'))

# initialisation

mx.cube(grille)
afficher(grille)

# boucle

racine.mainloop()