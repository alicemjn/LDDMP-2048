import tkinter as tk

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg='#cbc0b5', height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(4):
    for j in range(4):
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case))
racine.mainloop() # Lancement de la boucle principale