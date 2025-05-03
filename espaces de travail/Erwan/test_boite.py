import tkinter as tk

# Creation des fenetres principales

racine = tk.Tk()
racine.title("2048")

game = tk.Tk()
game.title("204/ Mode classique")

def show_game():
    racine.withdraw()
    game.deiconify()

def show_racine():
    game.withdraw()
    racine.deiconify()

# Create buttons
button1 = tk.Button(racine, text="Go to Window 2", command=show_game)
button1.pack(pady=20, padx=50)

button2 = tk.Button(game, text="Go to Window 1", command=show_racine)
button2.pack(pady=20, padx=50)

# boucler et afficher initialement la racine

show_racine()

racine.mainloop()