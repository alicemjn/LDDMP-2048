import tkinter as tk

grille = [[2,4,8,16],
          [32,64,128,256],
          [512,1024,2048,4096],
          [0,0,0,0]]

boutons = [] #stock les boutons pour pouvoir ensuite les parcourir et les mettre à jour


def generer_boutons(racine, n):
    #génère et place les boutons (labels)

    global boutons
    taille_bouton = 90

    for i in range(n):   
        ligne = [] #stock les boutons par ligne
        for j in range(n):
            valeur = grille[i][j]  #récupère la valeur correspondante dans la grille
            btn = tk.Label(racine, text=str(valeur), font=("#756e66",20), bg=color_case(valeur))
            btn.place(x=10 + j * 100, y=10 + i * 100, width=taille_bouton, height=taille_bouton) 
            ligne.append(btn) #ajoute le bouton à la liste ligne 
        boutons.append(ligne) #ajoute la ligne à la liste boutons
        print(ligne)
        print(boutons)



def afficher(n):
    #met à jour les valeurs (text) prises par les cases de la grille, et leur associe une couleur en appelant la fonction color_case
    for i in range(n):
        for j in range(n):
            value = grille[i][j]
            boutons[i][j].config(text=str(value) if value != 0 else "", bg=color_case(value))  #si value est égale à 0, aucun texte n'est affiché


def color_case(valeur):
    colors = {0:"#cdc1b4", 2:"#eee4da" , 4: "#ebe0cb", 8:"#e8b481", 16:"#e89e6c", 32:"#e68367", 64:"#e46847", 128:"#e8d07f",
              256:"#e8cd72", 512:"#edcc61", 1024:"#e4c655", 2048: "#edc22e", 4096: "#57beec"}
    return colors.get(valeur)  #retourne la couleur associée à la valeur dans le dictionnaire


racine = tk.Tk()
racine.title('2048')
racine.geometry('410x410')

canva = tk.Canvas(racine, bg="#b9ada1", height=410, width=410)
canva.place(x=0, y=0)

generer_boutons(racine, 4)
afficher(4)

racine.mainloop()