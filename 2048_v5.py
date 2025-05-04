import tkinter as tk
import mouvements as mv
import matrice as mx
import affichage as aff

# Création des fenêtres principales
# environnement Jeu et Menu Principal

racine = tk.Tk()
racine.title('2048')

# fonctions principales

def spawn(grille, game, pack, labels):
    """ La fonction spawn créer l'environnement dans les nouvelles fenetres ouvertes (voir fct start_game)
        - Création de la grille vide en fct du choix de l'utilisateur (grille 4X4, 8x8)
        - Création de la grille en tkinter
        - Ajout des éléements visuels comme le score """

    # dimensions
    DIM = 90 # taille des boutons
    n = len(grille)
    Grid_DIM = 90*n + (n+1)*10

    # afficher le Canvas
    container = tk.Canvas(game, width=Grid_DIM, height=Grid_DIM, bg=getattr(aff, pack.get())["background"], highlightthickness=0)
    container.grid(row=1, column=0, padx=30, pady=(80, 30))

    #remplir le canvas
    for i in range(n):
        for j in range(n):
            # les labels
            new_Label = tk.Label(container, font=("Helvetica, Arial, sans-serif", 40, "bold"))
            new_Label.place(x=10 + j*(DIM+10), y=10 + i*(DIM+10), width=DIM, height=DIM)
            labels[(i,j)] = new_Label


# fonctions de navigation entre les fenêtres

def start_game(taille, competitif):
    """ Creer une nouvelle fenetre de jeu "game". Peuple la fenetre avec la fonction spawn, active 
    les fcts de mouvements"""
    game = tk.Tk()
    pack = tk.StringVar(value="default") # pack de couleur par defaut

    if taille == 4:
        if competitif == True:
            game.title('2048 Mode compétitif 4x4')
        else:
            game.title('2048 Mode classique')
    else:
        game.title('2048 Grille ' + str(taille)+"x"+str(taille))
    
    # création de la grille et peuple la nouvelle fenetre avec spawn
    # creer une grille vide
    grille = [[0 for _ in range(taille)] for _ in range(taille)]
    mx.cube(grille)
    score = mx.score(grille)

    # score
    scoreBlock_container = tk.Label(game, bg="#BCAC9F")
    scoreBlock_container.place(x=230, y=15, height=50, width=100)

    scoreBlock_text = tk.Label(scoreBlock_container, text="Score", font=("Helvetica, Arial, sans-serif", 15), bg="#BCAC9F", fg="#EEE4DA")
    scoreBlock_text.place(x=0, height=20, width=100)

    scoreBlock_nbr = tk.Label(scoreBlock_container, text="0", font=("Helvetica, Arial, sans-serif", 25), bg="#BCAC9F", fg="#FFFFFF")
    scoreBlock_nbr.place(x=0, y=20, height=20, width=100)

    # best block

    bestBlock_container = tk.Label(game, bg="#BCAC9F")
    bestBlock_container.place(x=340, y=15, height=50, width=100)

    bestBlock_text = tk.Label(bestBlock_container, text="Meilleur", font=("Helvetica, Arial, sans-serif", 15), bg="#BCAC9F", fg="#EEE4DA")
    bestBlock_text.place(x=0, height=20, width=100)

    bestBlock_nbr = tk.Label(bestBlock_container, text="0", font=("Helvetica, Arial, sans-serif", 25), bg="#BCAC9F", fg="#FFFFFF")
    bestBlock_nbr.place(x=0, y=20, height=20, width=100)

    # initialiser le score
    scoreBlock_nbr.config(text=score[0])
    bestBlock_nbr.config(text=score[1])

    # mettre le titre
    title2048 = tk.Label(game, text="2048", font=("Helvetica, Arial, sans-serif", 50, "bold"), fg="#776E65")
    title2048.place(x=30, height=80)

    labels = {} # pour cibler les éléments plus tard, non dynamique puisque qu'il s'agit juste de ciblage

    #spawn
    spawn(grille, game, pack, labels)

    # affichage initial
    aff.affichage(grille, labels, pack.get())

    # fonctions de mouvements, uniques pour chaque fenetre

    def fleche(event, MAJ=None, c=0):
        assert event in ("gauche", "droite", "haut", "bas"), "La fonction ne reçoit pas cet argument"

        nonlocal grille
        DELAIS = 65

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
            aff.affichage(MAJ, labels, pack.get())
            racine.after(DELAIS, lambda: fleche(event, MAJ, c=c+1))
        else:
            if MAJ == grille:
                # meme matrice au début et à la fin
                if mx.is_game_over(grille) == True:
                    # on a perdu !
                    # placer le texte game over
                    gameOVER = tk.Label(game, text="GAME OVER", font=("Helvetica, Arial, sans-serif", 60, "bold"), fg="white", bg="black")
                    y = 80 + (90*len(grille) + (len(grille)+1)*10 + 30)/2 - 65 
                    width = 90*len(grille) + (len(grille)+1)*10 + 60
                    gameOVER.place(x=0, y=y, height=100, width=width)
                    # fermer la fct (arret du jeu)
                    return
            else:
                grille = MAJ
                mx.matrice_en_int(grille)
                mx.cube(grille)
                aff.affichage(grille, labels, pack.get())
                score = mx.score(grille)
                scoreBlock_nbr.config(text=score[0])
                bestBlock_nbr.config(text=score[1])

    # fonction de changelent de pack
    def select_pack():
        print(pack.get())

    # gestion de l'entrée
    game.bind('<Up>', lambda event: fleche('haut'))
    game.bind('<Down>', lambda event: fleche('bas'))
    game.bind('<Left>', lambda event: fleche('gauche'))
    game.bind('<Right>', lambda event: fleche('droite'))

    # menu de jeu (avec changement de pack)
    menubar_game = tk.Menu(game)
    game.config(menu=menubar_game)

        # Menu "Fichier"
    file_menu = tk.Menu(menubar_game, tearoff=0)
    menubar_game.add_cascade(label="Fichier", menu=file_menu)

    file_menu.add_command(label="Enregistrer le fichier JSON", accelerator="Cmd+S")
    file_menu.add_command(label="Importer...", accelerator="Cmd+O")

        # Menu "à propos"
    about_menu = tk.Menu(menubar_game, tearoff=0)
    menubar_game.add_cascade(label="À propos", menu=about_menu)

    about_menu.add_command(label="README", command=lambda: ouvrir_fichier_ext('readme.md'))
    about_menu.add_command(label="Github", command=lambda: ouvrir_fichier_ext('https://github.com/alicemjn/LDDMP-2048'))
    about_menu.add_command(label="Méthode de travail", command=lambda: ouvrir_fichier_ext('TRAVAIL.md'))
    about_menu.add_command(label="version: v5", state='disabled')
     
        # Menu "Pack de couleur"
    pack_menu = tk.Menu(menubar_game, tearoff=0)
    menubar_game.add_cascade(label="Pack de couleur", menu=pack_menu)

    pack_menu.add_radiobutton(label="Par default", value="default", variable=pack, command=select_pack)
    pack_menu.add_radiobutton(label="Moderne", value="moderne", variable=pack, command=select_pack)
    pack_menu.add_radiobutton(label="Billard", value="billard", variable=pack, command=select_pack)
    pack_menu.add_radiobutton(label="Squid Game", value="squid_game", variable=pack, command=select_pack)
    pack_menu.add_radiobutton(label="Barbie", value="barbie", variable=pack, command=select_pack)
    pack_menu.add_radiobutton(label="Android", value="android", variable=pack, command=select_pack)
    pack_menu.add_radiobutton(label="Aveugle", value="aveugle", variable=pack, command=select_pack)
    
    pack_menu.invoke(0) # coche default par défaut puisque c'est tjrs la veleur par défaut






















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
















# fentetre racine (boutons, menu, fct pour ouvrir des nouvelles parties)

button1 = tk.Button(racine, text="open", command=lambda: start_game(4, False))
button1.grid(row=0)
















# menu de la racine (sans changement de pack)

menubar = tk.Menu(racine)
racine.config(menu=menubar)

    # Menu "Fichier"
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=file_menu)

file_menu.add_command(label="Enregistrer le fichier JSON", accelerator="Cmd+S")
file_menu.add_command(label="Importer...", accelerator="Cmd+O")

    # Menu "à propos"
about_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="À propos", menu=about_menu)

about_menu.add_command(label="README", command=lambda: ouvrir_fichier_ext('readme.md'))
about_menu.add_command(label="Github", command=lambda: ouvrir_fichier_ext('https://github.com/alicemjn/LDDMP-2048'))
about_menu.add_command(label="Méthode de travail", command=lambda: ouvrir_fichier_ext('TRAVAIL.md'))
about_menu.add_command(label="version: v5", state='disabled')

# boucler et afficher initialement la fenêtre racine

racine.mainloop()