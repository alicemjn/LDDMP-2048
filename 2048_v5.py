import tkinter as tk

# Création des fenêtres principales
# environnement Jeu et Menu Principal

racine = tk.Tk()
racine.title('2048')

# fonctions de navigation entre les fenêtres

def start_game():
    game = tk.Tk()
    game.title('2048 Mode classique')
    game.deiconify()

# boucler et afficher initialement la fenêtre racine
start_game()
start_game()
racine.mainloop()