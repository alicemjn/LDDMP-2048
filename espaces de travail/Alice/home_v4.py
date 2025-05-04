# ce que j'ai changé par rapport à la v2:
# - J'ai enelvé la bordure (donc supprimé les "bordure 1 , 2, 3, 4" et changer l'element parent
#   des "frame" (frame classique, frameetendue etc) en mettant racine à la place de "bordure 1, 2 etc"
# - J'ai changé la taille des boutons (donc j'ai juste touché à x et y, à priori t'avais pas retenu 
#   par coeur les positions de chaque bouton donc ça change rien)
# - ET (le plus notable quand tu vas relire) j'ai regroupé les intructions du bouton avec les labels,
#   t'avais séparé les boutons des labels dans ton code et j'ai juste rassemblé pour avoir tout en continuité
#   par ex tu as frameetendue avec à la suite etendue1, vu que c'est le meme bouton j'ai mis ces instructions à la suite
#   plutot que de déclarer tous les frames puis déclaréer touts les labels [regarde le code tu vas capter] 
# - J'ai changé les couleurs dans ton dictionnaire

import tkinter as tk

couleur={"font_title" : "#776E65",
        "jaune" : "#EDC702",
        "gris" : "#A4937D",
        "orange" : "#F47D57",
        "red" : "red"}

racine = tk.Tk()
racine.configure(height=520, width=520)
racine.title('home')


overlay_canvas = tk.Canvas(racine, bg="red", highlightthickness=0)
overlay_canvas.place(x=0, y=0, width=520, height=520)

overlay_canvas.create_text(260, 80, text="2048", font=("Helvetica, Arial, sans-serif", 80, 'bold'), fill=couleur["font_title"])

# 2048 titre

#title = tk.Label(racine, text="2048", font=("Helvetica, Arial, sans-serif", 80, "bold"), fg=couleur["font_title"])
#title.place(x=0, y=0, height=150, width=520)

# boutons code: container puis texte sup puis texte inf

    # classique
frameclassique=tk.Frame(racine, bg=couleur["jaune"])
frameclassique.place(x=66, y=150, width=180, height=85)

classique1=tk.Label(frameclassique, text="Classique", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["jaune"], fg="white") 
classique1.place(x=0, y=5, width=180, height=30)

classique2=tk.Label(frameclassique, text="4x4", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["jaune"], fg="white")
classique2.place(x=0, y=38, width=180, height=35)

    # étendue
frameetendue=tk.Frame(racine, bg=couleur["gris"])
frameetendue.place(x=266, y=150, width=180, height=85)

etendue1=tk.Label(frameetendue, text="Étendue", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["gris"], fg="white") 
etendue1.place(x=0, y=5, width=180, height=30)

etendue2=tk.Label(frameetendue, text="8x8", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["gris"], fg="white")
etendue2.place(x=0, y=38, width=180, height=35)

    #personnalisé
frameperso=tk.Canvas(racine, bg=couleur["gris"], highlightthickness=0)
frameperso.place(x=66, y=255, width=180, height=85)

perso1=tk.Label(frameperso, text="Personnalisé", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["gris"], fg="white")
perso1.place(x=5, y=2, width=180, height=40)

perso_entrée = tk.Entry(frameperso, bg="white", fg="black", font=("Helvetica, Arial, sans-serif", 20), borderwidth=0, highlightthickness=0)
perso_entrée.place(x=34, y=50, width=50, height=25)

# boutons Ok proportions 38x38
perso_ok=tk.Label(frameperso, text="OK", font=("Helvetica, Arial, sans-serif", 13), bg="white")
perso_ok.place(x=114, y=49)

# ajout des contours boutons ok et entry (coins arrondis)
frameperso.create_oval(110, 42, 148, 80, fill="white", width=0)
        # on créer un rectangle et deux cercles pour le entry hauteur = 38
frameperso.create_oval(18, 42, 56, 80, fill="white", width=0)
frameperso.create_oval(60, 42, 98, 80, fill="white", width=0)
frameperso.create_rectangle(37,42,80,80, fill="white", width=0)

    #competitif
framecompetitif=tk.Frame(racine, bg=couleur["orange"])
framecompetitif.place(x=266, y=255, width=180, height=85)

competitif1=tk.Label(framecompetitif, text="Compétitif", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["orange"], fg="white")
competitif1.place(x=0, y=5, width=180, height=30)

competitif2=tk.Label(framecompetitif, text="4x4", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["orange"], fg="white")
competitif2.place(x=0, y=38, width=180, height=35)

racine.mainloop()