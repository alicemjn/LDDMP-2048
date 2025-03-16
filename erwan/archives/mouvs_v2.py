# notes de code:
# version condensé et corrigée de ce que j'ai fait précédement
# mais il manque les directions haut et bas

LEN = 4
grille = [[0,0,0,0],
          [4,0,0,0],
          [2,0,1,1],
          [2,0,2,0]]

# def

def afficher(grille) :
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

def move(sens, grille, c=0):
    """ Ajoute les colonnes les unes après les autres. 'BLOQUE' les valeurs en mettant des
    guillements pour respecter les régles d'addition du jeu (2+2+4 = 4+4 et pas 8)"""
    # erreurs de définitions potentielles
    assert sens in ("gauche", "droite"), "La fonction move doit prendre en premier argument la direction du mouvement tel que move('sens') ou sens doit être 'gauche' ou 'droite' ou 'bas' ou 'haut'."

    # fonctions qui adaptenent les paramètres selon la direction
    if sens == "droite":
        fct_prem = lambda i,n: (LEN-1)-i
        fct_deu = lambda i,n: (LEN-1)-(i+1)
        fct_n_prem = lambda i,n: n

        fct_n_deu = lambda i,n: n
        fct_N_pop, fct_N_fin = lambda i,n: n, lambda i,n: n
        fct_fin = lambda i,n: 0
    elif sens == "gauche":
        fct_prem = lambda i,n: i
        fct_deu = lambda i,n: (i+1)
        fct_n_prem = lambda i,n: n
        fct_n_deu = lambda i,n: n
        fct_N_pop, fct_N_fin = lambda i,n: n, lambda i,n: n
        fct_fin = lambda i,n: LEN-1

    if c < LEN-1:
        for n in range(LEN):
            i = 0
            while i < LEN-1: # s'arrète è LEN-1 par ex pour une grille 4x4 à i=3
                prem = fct_prem(i,n)
                deu = fct_deu(i,n)
                n_prem = fct_n_prem(i,n)
                n_deu = fct_n_deu(i,n)
                N_pop = fct_N_pop(i,n)
                N_fin = fct_N_fin(i,n)
                fin = fct_fin(i,n)

                if grille[n_prem][prem] == 0 or grille[n_deu][deu] == 0:
                    if isinstance(grille[n_prem][prem], int) and isinstance(grille[n_prem][prem], int): # il ne faut pas bloqué ses valeurs car elles ne sont pas issues d'une addition autre que + 0
                        grille[n_prem][prem] = grille[n_deu][deu] + grille[n_prem][prem]
                    else: # débloque la valeur ajoute 0 et rebloque la valeur
                        grille[n_prem][prem] = str( int(grille[n_deu][deu]) + int(grille[n_prem][prem]) )
                    
                    #supprimer et ajouter un 0 à la fin
                    grille[N_pop].pop(deu)
                    grille[N_fin].insert(fin, 0)
                    i = LEN
                elif grille[n_prem][prem] == grille[n_deu][deu] and isinstance(grille[n_prem][prem], int) and isinstance(grille[n_prem][prem], int): # additionne les valeurs égales auf si elles sont bloquées cad qu'elle proviennent déjà d'une addition précédente
                    grille[n_prem][prem] = str( grille[n_deu][deu] + grille[n_prem][prem]) # le str bloque l'addition
                    
                    #supprimer et ajouter un 0 à la fin
                    grille[N_pop].pop(deu)
                    grille[N_fin].insert(fin, 0)
                    i = LEN
                i += 1
        afficher(grille)
        move(sens, grille, c+1)
    else:
        matrice_en_int() # débloque toutes les valeurs
        # cube() # ajoute une valeur en aléatoire
        afficher(grille) # ... l'affiche

# jeu

move("gauche", grille)