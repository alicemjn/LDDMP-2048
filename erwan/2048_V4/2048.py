# notes de code:
# version condensé et corrigée de ce que j'ai fait précédement
# mais il manque les directions haut et bas
# pour cela trabsposer la matrice

import tkinter as tk
import mouvements as mv

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

racine = tk.Tk()
racine.title('2048')

# directions

def bouge(event, c=0):
    assert event in ("gauche", "droite", "haut", "bas"), "La fonction ne reçoit pas cet argument"
    
    if c < len(grille)-1:
        print(mv.move(event, grille))
        bouge(event, c+1)
    else:
        print('fini')

# jeu

#mv.move("droite", grille)

racine.bind('<Up>', lambda event: bouge('haut'))
racine.bind('<Down>', lambda event: bouge('bas'))
racine.bind('<Left>', lambda event: bouge('gauche'))
racine.bind('<Right>', lambda event: bouge('droite'))

racine.mainloop()