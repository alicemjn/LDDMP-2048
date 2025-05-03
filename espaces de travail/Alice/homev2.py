import tkinter as tk

couleur={"font" : "#756e66",
        "fond_général" : "#ECECEC",
        "couleur_font" : "#776E65",
        "fond_classique" : "#EEE4DA",
        "fond_autre" : "#CDC1B5",
        "bordure1" : "#DED4CA",
        "bordure2" : "#C3B4A5" }

racine = tk.Tk()
racine.configure(bg=couleur["fond_général"], height=520, width=440)
racine.title('home')


label2048 = tk.Label(racine, text="2048", font=(couleur["font"], 60, "bold"), bg=couleur["fond_général"], fg=couleur["couleur_font"])
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

frameperso=tk.Frame(bordure3, bg=couleur["fond_autre"])
frameperso.place(x=3, y=3, width=150, height=90 )

#competitif

bordure4 = tk.Frame(racine, bg=couleur["bordure2"])
bordure4.place(x=237, y=297, width=156, height=96)

framecompetitif=tk.Frame(bordure4, bg=couleur["fond_autre"])
framecompetitif.place(x=3, y=3, width=150, height=90 )


#label(bouttons)

#classique

classique1=tk.Label(frameclassique, text="classique", font=(couleur["font"], 15), bg=couleur["fond_classique"], fg=couleur["couleur_font"]) 
classique1.place(x=5, y=2, width=140, height=40)

classique2=tk.Label(frameclassique, text="4X4", font=(couleur["font"], 20, "bold"), bg=couleur["fond_classique"], fg=couleur["couleur_font"]) 
classique2.place(x=4, y=40, width=140, height=40)


#étendue

etendue1=tk.Label(frameetendue, text="étendue", font=(couleur["font"], 15), bg=couleur["fond_autre"], fg=couleur["couleur_font"]) 
etendue1.place(x=5, y=2, width=140, height=40)

etendue2=tk.Label(frameetendue, text="8X8", font=(couleur["font"], 20, "bold"), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
etendue2.place(x=4, y=40, width=140, height=40)


#personnalisé

perso1=tk.Label(frameperso, text="personnalisé", font=(couleur["font"], 15), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
perso1.place(x=5, y=2, width=140, height=40)

perso_entrée = tk.Entry(frameperso, bg=couleur["bordure2"], fg=couleur["font"], font=(couleur["font"], 14), borderwidth=0)
perso_entrée.place(x=8, y=45, width=90, height=38)

perso_ok=tk.Label(frameperso, text="OK", font=(couleur["font"], 15), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
perso_ok.place(x=98, y=45, width=50, height=35)

#compétitif

competitif1=tk.Label(framecompetitif, text="compétitif", font=(couleur["font"], 15), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
competitif1.place(x=5, y=2, width=140, height=40)

competitif2=tk.Label(framecompetitif, text="4X4", font=(couleur["font"], 20, "bold"), bg=couleur["fond_autre"], fg=couleur["couleur_font"])
competitif2.place(x=4, y=40, width=140, height=40)


racine.mainloop()