import tkinter as tk
import random as Ashkan

# Création des fenêtres principales
# environnement Jeu et Menu Principal

racine = tk.Tk()
racine.title('2048')

# fonctions de navigation entre les fenêtres

def col_aleatoire():
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    r= Ashkan.randint(0,255)
    g= Ashkan.randint(0,255)
    b= Ashkan.randint(0,255)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def start_game():
    game = tk.Tk()
    game.title('2048 Mode classique')
    game.deiconify()

    def background():
        hey = col_aleatoire()
        game.config(background=hey)

    bouton2 = tk.Button(game, text="background", command=background)
    bouton2.pack(padx=50, pady=50)

# boucler et afficher initialement la fenêtre racine
bouton1 = tk.Button(racine, text="start", command=start_game)
bouton1.pack(padx=50, pady=50)

racine.mainloop()