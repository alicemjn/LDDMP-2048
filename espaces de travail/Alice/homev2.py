import tkinter as tk

couleur={"font" : "#756e66",
        "fond_général" : "#ECECEC",
        "couleur_font" : "#776E65",
        "fond_classique" : "#EEE4DA",
        "fond_autre" : "#CDC1B5",
        "bordure1" : "#DED4CA",
        "bordure2" : "#C3B4A5"}

racine = tk.Tk()
racine.configure(bg=couleur["fond_général"], height=520, width=440)
racine.title('home')

label2048 = tk.Label(racine, text="2048", font=("Helvetica, Arial, sans-serif", 80, "bold"), bg=couleur["fond_général"], fg=couleur["couleur_font"])
label2048.place(x=0, y=40, width=440, height=100)

#frame 

#classique

bordure1 = tk.Frame(racine, bg=couleur["bordure1"]) 
bordure1.place(x=52, y=177, width=156, height=96)

frameclassique=tk.Frame(bordure1, bg=couleur["fond_classique"])
frameclassique.place(x=3, y=3, width=150, height=90 )

#étendue

bordure2 = tk.Frame(racine, bg=couleur["bordure2"])
bordure2.place(x=237, y=177, width=156, height=96)

frameetendue=tk.Frame(bordure2, bg=couleur["fond_autre"])
frameetendue.place(x=3, y=3, width=150, height=90)

#personnalisé

bordure3 = tk.Frame(racine, bg=couleur["bordure2"])
bordure3.place(x=52, y=297, width=156, height=96)

frameperso=tk.Canvas(bordure3, bg=couleur["fond_autre"], highlightthickness=0)
frameperso.place(x=3, y=3, width=150, height=90 )

#competitif

bordure4 = tk.Frame(racine, bg=couleur["bordure2"])
bordure4.place(x=237, y=297, width=156, height=96)

framecompetitif=tk.Frame(bordure4, bg=couleur["fond_autre"])
framecompetitif.place(x=3, y=3, width=150, height=90 )


#label(bouttons)

#classique

classique1=tk.Label(frameclassique, text="Classique", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["fond_classique"], fg=couleur["couleur_font"]) 
classique1.place(x=5, y=2, width=140, height=40)

classique2=tk.Label(frameclassique, text="4x4", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["fond_classique"], fg=couleur["couleur_font"]) 
classique2.place(x=4, y=40, width=140, height=40)


#étendue

etendue1=tk.Label(frameetendue, text="Étendue", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["fond_autre"], fg=couleur["couleur_font"]) 
etendue1.place(x=5, y=2, width=140, height=40)

etendue2=tk.Label(frameetendue, text="8x8", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
etendue2.place(x=4, y=40, width=140, height=40)


#personnalisé

perso1=tk.Label(frameperso, text="Personnalisé", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
perso1.place(x=5, y=2, width=140, height=40)

perso_entrée = tk.Entry(frameperso, bg="white", fg="black", font=("Helvetica, Arial, sans-serif", 20), borderwidth=0, highlightthickness=0)
perso_entrée.place(x=30, y=52, width=50, height=25)

# boutons Ok proportions 38x38
perso_ok=tk.Label(frameperso, text="OK", font=("Helvetica, Arial, sans-serif", 16), bg="white", fg=couleur["couleur_font"])
perso_ok.place(x=103, y=52)

# ajout des contours boutons ok et entry (coins arrondis)
frameperso.create_oval(98, 45, 136, 83, fill="white", width=0)
        # on créer un rectangle et deux cercles pour le entry hauteur = 38
frameperso.create_oval(15, 45, 53, 83, fill="white", width=0)
frameperso.create_oval(57, 45, 95, 83, fill="white", width=0)
frameperso.create_rectangle(34,45,77,84, fill="white", width=0)

#compétitif

competitif1=tk.Label(framecompetitif, text="Compétitif", font=("Helvetica, Arial, sans-serif", 20), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
competitif1.place(x=5, y=2, width=140, height=40)

competitif2=tk.Label(framecompetitif, text="4x4", font=("Helvetica, Arial, sans-serif", 30, "bold"), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
competitif2.place(x=4, y=40, width=140, height=40)

racine.mainloop()