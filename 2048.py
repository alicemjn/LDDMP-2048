import tkinter as tk
import mouvements as mv
import matrice as mx
import affichage as aff

# Spawn

racine = tk.Tk()
racine.title('2048')
racine.resizable(False, False)

labels = {} # pour cibler les éléments plus tard, non dynamique puisque qu'il s'agit juste de ciblage

def spawn(grille, racine, pack):
    # dimensions
    DIM = 90 # taille des boutons
    n = len(grille)
    Grid_DIM = 90*n + (n+1)*10

    # afficher le Canvas
    container = tk.Canvas(racine, width=Grid_DIM, height=Grid_DIM, bg=getattr(aff, pack)["background"], highlightthickness=0)
    container.grid(row=1, column=0, padx=30, pady=(80, 30))

    #remplir le canvas
    for i in range(n):
        for j in range(n):
            # les labels
            new_Label = tk.Label(container, font=("Helvetica, Arial, sans-serif", 40, "bold"))
            new_Label.place(x=10 + j*(DIM+10), y=10 + i*(DIM+10), width=DIM, height=DIM)
            labels[(i,j)] = new_Label
    score = mx.score(grille)
    scoreBlock_nbr.config(text=score[0])
    bestBlock_nbr.config(text=score[1])

# affichage

def afficher(grille):
    """ Cette fonction permet d'envoyer en packets le dictionnaire label et la grille vers la fonction 
    d'affichage stocké dans le fichier dédié aux fonctions d'affichage """
    aff.affichage(grille, labels, pack_value.get())

# fonctions de déplacements

DELAIS = 65 # ICI régler le délais de l'animation

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
            pass
        else:
            grille = MAJ
            mx.matrice_en_int(grille)
            mx.cube(grille)
            afficher(grille)
            score = mx.score(grille)
            scoreBlock_nbr.config(text=score[0])
            bestBlock_nbr.config(text=score[1])

# pack de couleur

def select_pack():
    spawn(grille, racine, pack_value.get())
    afficher(grille)

# autres fonctions

def ouvrir_fichier_ext(nom):
    """ Cette fonction permet d'ouvrir des fichiers avec leur application par défault dans 
    l'os de l'utilisateur. Elle commence par regarder l'os de l'utilisateur et ouvre le 
    fichier via le nom donné en argument. """

    import os
    import platform

    systeme = platform.system() # regarde l'os parce que pas forcément la meme commande
    if systeme == 'Windows':
        os.startfile(nom)
    elif systeme == 'Darwin':
        os.system('open '+nom)
    elif systeme == 'Linux':
        os.system('xdg-open '+nom)

# grille

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

pack_value = tk.StringVar(value="default")

# grille pour tester les paks => (supprimer le # avant grille)
grille = [[0,0,0,2],[4,8,16,32],[64,128,256,512],[1024,2048,4096,4096*2]]

# grosse grille 8x8 pour tester => (supprimer le # avant grille)
#grille = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]



#### Menu

# création du container

menubar = tk.Menu(racine)
racine.config(menu=menubar)

# Menu "Fichier"

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=file_menu)

file_menu.add_command(label="Enregistrer le fichier JSON", accelerator="Cmd+S")
file_menu.add_command(label="Importer...", accelerator="Cmd+O")

# Menu "Pack de couleur"

pack_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Pack de couleur", menu=pack_menu)

pack_menu.add_radiobutton(label="Par default", value="default", variable=pack_value, command=select_pack)
pack_menu.add_radiobutton(label="Moderne", value="moderne", variable=pack_value, command=select_pack)
pack_menu.add_radiobutton(label="Billard", value="billard", variable=pack_value, command=select_pack)
pack_menu.add_radiobutton(label="Squid Game", value="squid_game", variable=pack_value, command=select_pack)
pack_menu.add_radiobutton(label="Barbie", value="barbie", variable=pack_value, command=select_pack)
pack_menu.add_radiobutton(label="Android", value="android", variable=pack_value, command=select_pack)
pack_menu.add_radiobutton(label="Aveugle", value="aveugle", variable=pack_value, command=select_pack)

# Menu "à propos"

about_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="À propos", menu=about_menu)

about_menu.add_command(label="README", command=lambda: ouvrir_fichier_ext('readme.md'))
about_menu.add_command(label="Github", command=lambda: ouvrir_fichier_ext('https://github.com/alicemjn/LDDMP-2048'))
about_menu.add_command(label="Méthode de travail", command=lambda: ouvrir_fichier_ext('TRAVAIL.md'))
about_menu.add_command(label="version: v4.1", state='disabled')

# titre

title2048 = tk.Label(racine, text="2048", font=("Helvetica, Arial, sans-serif", 50, "bold"), fg="#776E65")
title2048.place(x=30, height=80)

# score

scoreBlock_container = tk.Label(racine, bg="#BCAC9F")
scoreBlock_container.place(x=230, y=15, height=50, width=100)

scoreBlock_text = tk.Label(scoreBlock_container, text="SCORE", font=("Helvetica, Arial, sans-serif", 15), bg="#BCAC9F", fg="#EEE4DA")
scoreBlock_text.place(x=0, height=20, width=100)

scoreBlock_nbr = tk.Label(scoreBlock_container, text="0", font=("Helvetica, Arial, sans-serif", 25), bg="#BCAC9F", fg="#FFFFFF")
scoreBlock_nbr.place(x=0, y=20, height=20, width=100)

# best block

bestBlock_container = tk.Label(racine, bg="#BCAC9F")
bestBlock_container.place(x=340, y=15, height=50, width=100)

bestBlock_text = tk.Label(bestBlock_container, text="Meilleur", font=("Helvetica, Arial, sans-serif", 15), bg="#BCAC9F", fg="#EEE4DA")
bestBlock_text.place(x=0, height=20, width=100)

bestBlock_nbr = tk.Label(bestBlock_container, text="0", font=("Helvetica, Arial, sans-serif", 25), bg="#BCAC9F", fg="#FFFFFF")
bestBlock_nbr.place(x=0, y=20, height=20, width=100)

# gestion de l'entrée

racine.bind('<Up>', lambda event: fleche('haut'))
racine.bind('<Down>', lambda event: fleche('bas'))
racine.bind('<Left>', lambda event: fleche('gauche'))
racine.bind('<Right>', lambda event: fleche('droite'))

# initialisation

mx.cube(grille)
spawn(grille, racine, pack_value.get())
afficher(grille)

# boucle

racine.mainloop()