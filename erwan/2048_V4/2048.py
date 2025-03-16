# notes de code:
# version condensé et corrigée de ce que j'ai fait précédement
# mais il manque les directions haut et bas
# pour cela trabsposer la matrice

import tkinter as tk
import mouvements as mv
import matrice as mx
import time

# affichage de la matrice

def afficher(grille):
    for line in grille:
        print(line)

# directions

def fleche(event, MAJ=None, c=0):
    assert event in ("gauche", "droite", "haut", "bas"), "La fonction ne reçoit pas cet argument"

    global grille

    if MAJ is None: # copie de grille sans pointer vers le meme espace mémoire sinon
                    # on pointe vers la meme liste à la fin (pas bien compris ça)
        MAJ = [row[:] for row in grille]
    
    if c < len(MAJ)-1:
        #### mic mac
        if event == "haut" or event == "bas":
            MAJ = mx.transpose(MAJ)
        MAJ = mv.move(event, MAJ)
        
        if event == "haut" or event == "bas":
            # créer un transpose droite/gauche
            MAJ = mx.transpose(MAJ)
            MAJ = mx.transpose(MAJ)
            MAJ = mx.transpose(MAJ)
        afficher(MAJ)
        #time.sleep(0.1)
        fleche(event, MAJ, c=c+1)
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
          [0,0,0,1]]

# éléments visuels (tkinter)

racine = tk.Tk()
racine.title('2048')

racine.bind('<Up>', lambda event: fleche('haut'))
racine.bind('<Down>', lambda event: fleche('bas'))
racine.bind('<Left>', lambda event: fleche('gauche'))
racine.bind('<Right>', lambda event: fleche('droite'))

racine.mainloop()