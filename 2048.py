import tkinter as tk
import mouvements as mv
import matrice as mx
import affichage as aff

# Création des fenêtres principales
# environnement Jeu et Menu Principal

racine = tk.Tk()
racine.config(width=610, height=610)
racine.resizable(False, False)

racine.title('2048')

# fonctions principales

def spawn(grille, game, pack, labels, DIM):
    """ La fonction spawn créer l'environnement dans les nouvelles fenetres ouvertes (voir fct start_game)
        - Création de la grille vide en fct du choix de l'utilisateur (grille 4X4, 8x8)
        - Création de la grille en tkinter
        - Ajout des éléements visuels comme le score """

    # dimensions
    DIM #taille des boutons
    n = len(grille)
    Grid_DIM = DIM*n + (n+1)*10

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

def start_game(taille, competitif, DIM):
    """ Creer une nouvelle fenetre de jeu "game". Peuple la fenetre avec la fonction spawn, active 
    les fcts de mouvements"""
    game = tk.Tk()
    game.config(bg="#ECECEC")
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

    # mettre le titre
    title2048 = tk.Label(game, text="2048", font=("Helvetica, Arial, sans-serif", 50, "bold"), fg="#776E65", bg="#ECECEC")
    title2048.place(x=30, height=80)

    # calcul de la largeur de la fenetre pour aligner les élements (score et game over)
    width = 90*len(grille) + (len(grille)+1)*10 + 60

    # score
    scoreBlock_container = tk.Label(game, bg="#BCAC9F")
    scoreBlock_container.place(x=(width-240), y=15, height=50, width=100)

    scoreBlock_text = tk.Label(scoreBlock_container, text="Score", font=("Helvetica, Arial, sans-serif", 15), bg="#BCAC9F", fg="#EEE4DA")
    scoreBlock_text.place(x=0, height=20, width=100)

    scoreBlock_nbr = tk.Label(scoreBlock_container, text="0", font=("Helvetica, Arial, sans-serif", 25), bg="#BCAC9F", fg="#FFFFFF")
    scoreBlock_nbr.place(x=0, y=20, height=20, width=100)

    # best block

    bestBlock_container = tk.Label(game, bg="#BCAC9F")
    bestBlock_container.place(x=(width-130), y=15, height=50, width=100)

    bestBlock_text = tk.Label(bestBlock_container, text="Meilleur", font=("Helvetica, Arial, sans-serif", 15), bg="#BCAC9F", fg="#EEE4DA")
    bestBlock_text.place(x=0, height=20, width=100)

    bestBlock_nbr = tk.Label(bestBlock_container, text="0", font=("Helvetica, Arial, sans-serif", 25), bg="#BCAC9F", fg="#FFFFFF")
    bestBlock_nbr.place(x=0, y=20, height=20, width=100)

    # initialiser le score
    scoreBlock_nbr.config(text=score[0])
    bestBlock_nbr.config(text=score[1])

    labels = {} # pour cibler les éléments plus tard, non dynamique puisque qu'il s'agit juste de ciblage

    #spawn
    spawn(grille, game, pack, labels, DIM)

    # affichage initial
    aff.affichage(grille, labels, pack.get())

    # fonctions de mouvements, uniques pour chaque fenetre

    def fleche(event, MAJ=None, c=0):
        """ Cette fonction permet de déplacer petit à petit les cubes dans la grille. Elle est récurssive cad 
        qu'à la fin de l'execution elle va se rapeller elle même après un certian laps de temps (DELAIS) ce 
        qui permet de créer l'animation des cubes qui bougent"""

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
                MAJ = mx.transpose_right(MAJ)
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
    def select_pack(value):
        """ Cette fonction permet de changer de pack de couleur (mise à jour de la variable pack et affichage
        de la nouvelle grille) """
        nonlocal pack
        pack = tk.StringVar(value=value) 
        spawn(grille, game, pack, labels, DIM)
        aff.affichage(grille, labels, pack.get())

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

    pack_menu.add_radiobutton(label="Par default", variable=pack, command=lambda: select_pack("default"))
    pack_menu.add_radiobutton(label="Moderne", variable=pack, command=lambda: select_pack("moderne"))
    pack_menu.add_radiobutton(label="Billard", variable=pack, command=lambda: select_pack("billard"))
    pack_menu.add_radiobutton(label="Squid Game", variable=pack, command=lambda: select_pack("squid_game"))
    pack_menu.add_radiobutton(label="Barbie", variable=pack, command=lambda: select_pack("barbie"))
    pack_menu.add_radiobutton(label="Android", variable=pack, command=lambda: select_pack("android"))
    pack_menu.add_radiobutton(label="Aveugle", variable=pack, command=lambda: select_pack("aveugle"))
    
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
        os.system('open '+ nom)
    elif systeme == 'Linux':
        os.system('xdg-open '+ nom)























# fentetre racine (boutons, menu, fct pour ouvrir des nouvelles parties)

couleur={"font_title" : "#776E65",
        "jaune" : "#EDC702",
        "gris" : "#A4937D",
        "orange" : "#F47D57",
        "red" : "red"}

# canvas avec titre 2048 et grille automatique

overlay_canvas = tk.Canvas(racine, bg="white", highlightthickness=0)
overlay_canvas.place(x=0, y=0, width=610, height=610)

# titre 2048 dans le canvas



# boutons par dessus le canvas

    # classique
frameclassique=tk.Frame(racine, bg=couleur["jaune"])
frameclassique.place(x=115, y=200, width=180, height=85)

classique1=tk.Label(frameclassique, text="Classique", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["jaune"], fg="white") 
classique1.place(x=0, y=5, width=180, height=30)

classique2=tk.Label(frameclassique, text="4x4", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["jaune"], fg="white")
classique2.place(x=0, y=38, width=180, height=35)

    # étendue
frameetendue=tk.Frame(racine, bg=couleur["gris"])
frameetendue.place(x=315, y=200, width=180, height=85)

etendue1=tk.Label(frameetendue, text="Étendue", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["gris"], fg="white") 
etendue1.place(x=0, y=5, width=180, height=30)

etendue2=tk.Label(frameetendue, text="8x8", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["gris"], fg="white")
etendue2.place(x=0, y=38, width=180, height=35)

    #personnalisé
frameperso=tk.Label(racine, bg=couleur["gris"])
frameperso.place(x=115, y=305, width=180, height=85)

perso1=tk.Label(frameperso, text="Personnalisé", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["gris"], fg="white")
perso1.place(x=5, y=2, width=180, height=40)

# Entry + fct qui empêche l'utilisateur de rentrer des valeurs non entières et supérieurs à 2 caratères

def validate_entry(text):
    """ Vérifie si le texte est vide (autorisé) ou un entier de max 2 caractères """
    if len(text) == 0:
        return True
    if len(text) <= 2 and text.isdigit():
        return True
    return False

vcmd = (racine.register(validate_entry), '%P')

perso_entree = tk.Entry(frameperso, bg="white", fg="black", 
                        font=("Helvetica, Arial, sans-serif", 20), 
                        borderwidth=0, highlightthickness=0,
                        validate="key", validatecommand=vcmd) # appel de la fct validate entry
perso_entree.place(x=40, y=40, width=70, height=30)

perso_ok=tk.Label(frameperso, text="Ok", font=("Helvetica, Arial, sans-serif", 15), bg="white", fg="grey")
perso_ok.place(x=117, y=40, height=30, width=30)

    #competitif
framecompetitif=tk.Frame(racine, bg=couleur["orange"])
framecompetitif.place(x=315, y=305, width=180, height=85)

competitif1=tk.Label(framecompetitif, text="Compétitif", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["orange"], fg="white")
competitif1.place(x=0, y=5, width=180, height=30)

competitif2=tk.Label(framecompetitif, text="4x4", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["orange"], fg="white")
competitif2.place(x=0, y=38, width=180, height=35)

# fonctions quand on clique sur les boutons (qui sont en réalité des Labels d'où ce système D)

def start_game_perso(event):
    """ Fonction intermédiaire de start_game() qui ouvre une grille personnalisé avec ce que l'utilisateur
    a saisit dans le widget entry du bouton personnalisé"""
    valeur = perso_entree.get()
    if valeur != "":
        if int(valeur) > 1:
            start_game(int(valeur), False, 90)

classique1.bind("<Button-1>", lambda event: start_game(4,False, 90))
classique2.bind("<Button-1>", lambda event: start_game(4,False, 90))

etendue1.bind("<Button-1>", lambda event: start_game(8,False, 90))
etendue2.bind("<Button-1>", lambda event: start_game(8,False, 90))

perso_ok.bind("<Button-1>", start_game_perso)

competitif1.bind("<Button-1>", lambda event: start_game(4,True, 90))
competitif2.bind("<Button-1>", lambda event: start_game(4,True, 90))

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

#animation du canvas

def animate(grille):
    """ tentative de focntion qui anime une grille en arrière plan """
    labels = {}
    pack_home = tk.StringVar(value="home")
    # spawn
    overlay_canvas.config(bg=getattr(aff, pack_home.get())["background"], highlightthickness=0)
    n = 6
    DIM=90
    for i in range(n):
        for j in range(n):
            # les labels
            new_Label = tk.Label(overlay_canvas, font=("Helvetica, Arial, sans-serif", 40, "bold"))
            new_Label.place(x=10 + j*(DIM+10), y=10 + i*(DIM+10), width=DIM, height=DIM)
            labels[(i,j)] = new_Label
    mx.cube(grille)
    aff.affichage(grille, labels, pack_home.get())

grille_background = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
animate(grille_background)

# boucler et afficher initialement la fenêtre racine

racine.mainloop()