def move(sens, grille):
    """ Ajoute les colonnes les unes après les autres. 'BLOQUE' les valeurs en mettant des
    guillements pour respecter les régles d'addition du jeu (2+2+4 = 4+4 et pas 8)"""
    # erreurs de définitions potentielles
    #assert sens in ("gauche", "droite"), "La fonction move doit prendre en premier argument la direction du mouvement tel que move('sens') ou sens doit être 'gauche' ou 'droite' ou 'bas' ou 'haut'."

    LEN = len(grille)
    # fonctions qui adaptenent les paramètres selon la direction
    if sens == "droite" or sens == "bas":
        fct_prem = lambda i: (LEN-1)-i
        fct_deu = lambda i: (LEN-1)-(i+1)
        fct_n_prem = lambda n: n
        fct_n_deu = lambda n: n
        fct_N = lambda n: n
        fct_fin = lambda n: 0
    elif sens == "gauche" or sens == "haut":
        fct_prem = lambda i: i
        fct_deu = lambda i: (i+1)
        fct_n_prem = lambda n: n
        fct_n_deu = lambda n: n
        fct_N = lambda n: n
        fct_fin = lambda n: LEN-1

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
    return grille