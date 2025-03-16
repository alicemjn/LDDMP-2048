# notes de code:
# version condensé et corrigée de ce que j'ai fait précédement
# mais il manque les directions haut et bas
# pour cela trabsposer la matrice

import tkinter as tk
import mouvements as mv
import matrice as mx

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

racine = tk.Tk()
racine.title('2048')

# affichage de la matrice

def afficher(grille):
    for line in grille:
        print(line)

# directions

def bouge(event, c=0):
    assert event in ("gauche", "droite", "haut", "bas"), "La fonction ne reçoit pas cet argument"
    
    if c < len(grille)-1:
        MAJ = mv.move(event, grille) # stocke la nouvelle matrice
        afficher(MAJ)
        bouge(event, c+1)
    else:
        if MAJ == grille: # regarde si la matrice à changé
            print('pas de déplacements')
        else:
            grille = MAJ # mets à jour la matrice
            mx.matrice_en_int(grille)
            mx.cube(grille)
            afficher(MAJ)

racine.bind('<Up>', lambda event: bouge('haut'))
racine.bind('<Down>', lambda event: bouge('bas'))
racine.bind('<Left>', lambda event: bouge('gauche'))
racine.bind('<Right>', lambda event: bouge('droite'))

racine.mainloop()