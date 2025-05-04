import tkinter as tk

# Création des fenêtres principales
# environnement Jeu et Menu Principal

racine = tk.Tk()
racine.title('2048')

# fonctions de navigation entre les fenêtres

def start_game():
    game = tk.Tk()
    game.title('2048 Mode classique')

# boucler et afficher initialement la fenêtre racine
bouton1 = tk.Button(racine, text="start", command=start_game)
bouton1.pack(padx=50, pady=50)

racine.mainloop()