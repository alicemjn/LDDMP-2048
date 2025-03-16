import random as Ashkan
import tkinter as tk

# fonctions

def afficher():
    print(grille[0])
    print(grille[1])
    print(grille[2])
    print(grille[3])
    print(' ')

def matrice_en_int():
    for n in range(len(grille)):  # Parcours des lignes
        for i in range(len(grille[n])):  # Parcours des colonnes
            if isinstance(grille[n][i], str):  # Vérifie si c'est une string
                grille[n][i] = int(grille[n][i])  # Convertit en int

def contient_zero():
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False

def cube():
    """ Cette fonction permet de remplir la grille tout
     en vérifiant que la place est libre pour un nouveau
      block """
    # choisir une position
    x = Ashkan.randint(0,LEN-1)
    y = Ashkan.randint(0,LEN-1)
    # vérifier si y'a déjà quelque chose dans cette case
    if grille[y][x] == 0:
        grille[y][x] = 2
    else:
        # vérifier que la grille n'est pas pleine
        if contient_zero() == False:
            print('perdu')
        else:
            # sinon recommencer (au bout d'un momment on trouvera la place)
            cube()

def move(sens, c=0):
    """ Ajoute les colonnes les unes après les autres. 'BLOQUE' les valeurs en mettant des
    guillements pour respecter les régles d'addition du jeu (2+2+4 = 4+4 et pas 8)"""
    # erreurs de définitions potentielles
    assert sens in ("gauche", "droite"), "La fonction move doit prendre en premier argument la direction du mouvement tel que move('sens') ou sens doit être 'gauche' ou 'droite' ou 'bas' ou 'haut'."

    # fonctions qui adaptenent les paramètres selon la direction
    if sens == "droite":
        fct_prem = lambda i: (LEN-1)-i
        fct_deu = lambda i: (LEN-1)-(i+1)
        fct_n_prem = lambda n: n
        fct_n_deu = lambda n: n
        fct_N = lambda n: n
        fct_fin = lambda n: 0
    elif sens == "gauche":
        fct_prem = lambda i: i
        fct_deu = lambda i: (i+1)
        fct_n_prem = lambda n: n
        fct_n_deu = lambda n: n
        fct_N = lambda n: n
        fct_fin = lambda n: LEN-1

    if c < LEN-1:
        for n in range(LEN):
            i = 0
            while i < LEN-1: # s'arrète è LEN-1 par ex pour une grille 4x4 à i=3
                prem = fct_prem(i)
                deu = fct_deu(i)
                n_prem = fct_n_prem(n)
                n_deu = fct_n_deu(n)
                N = fct_N(n)
                fin = fct_fin (n)

                if grille[n_prem][prem] == 0 or grille[n_deu][deu] == 0:
                    if isinstance(grille[n_prem][prem], int) and isinstance(grille[n_prem][prem], int): # il ne faut pas bloqué ses valeurs car elles ne sont pas issues d'une addition autre que + 0
                        grille[n_prem][prem] = grille[n_deu][deu] + grille[n_prem][prem]
                    else: # débloque la valeur ajoute 0 et rebloque la valeur
                        grille[n_prem][prem] = str( int(grille[n_deu][deu]) + int(grille[n_prem][prem]) )
                    
                    #supprimer et ajouter un 0 à la fin
                    grille[N].pop(deu)
                    grille[N].insert(fin, 0)
                    i = LEN
                elif grille[n_prem][prem] == grille[n_deu][deu] and isinstance(grille[n_prem][prem], int) and isinstance(grille[n_prem][prem], int): # additionne les valeurs égales auf si elles sont bloquées cad qu'elle proviennent déjà d'une addition précédente
                    grille[n_prem][prem] = str( grille[n_deu][deu] + grille[n_prem][prem]) # le str bloque l'addition
                    
                    #supprimer et ajouter un 0 à la fin
                    grille[N].pop(deu)
                    grille[N].insert(fin, 0)
                    i = LEN
                i += 1
        afficher()
        move(sens, c+1)
    else:
        matrice_en_int() # débloque toutes les valeurs
        cube() # ajoute une valeur en aléatoire
        afficher() # ... l'affiche

# tkinter

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
LEN = len(grille)

racine = tk.Tk()
racine.title('2048')

# directions

def bouge(event):
    assert event in ("gauche", "droite", "haut", "bas"), "La fonction ne reçoit pas cet argument"
    if event in {'gauche', 'droite'}:
        move(event)
    elif event == 'haut':
        pass
    elif event == 'bas':
        pass

# jeu

#mv.move("droite", grille)

racine.bind('<Up>', lambda event: bouge('haut'))
racine.bind('<Down>', lambda event: bouge('bas'))
racine.bind('<Left>', lambda event: bouge('gauche'))
racine.bind('<Right>', lambda event: bouge('droite'))

racine.mainloop()