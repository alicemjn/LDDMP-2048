import random as Ashkan

# fonctions

def matrice_en_int(grille):
    """ débloque les valeurs de la matrice (car pour bloquer des valeurs on mets les nombres en str, donc débloquer
    revient à passer les str en int, pas de soucis car meme si ce sont des str, ce sont quand meme des nombres)
    rappel: dans le 2048 16+8+8 font 16+16 et pas 32 ! (pour un seul déplacement)"""
    for n in range(len(grille)):  # Parcours des lignes
        for i in range(len(grille[n])):  # Parcours des colonnes
            if isinstance(grille[n][i], str):  # Vérifie si c'est une string
                grille[n][i] = int(grille[n][i])  # Convertit en int

def contient_zero(grille):
    """ regarde si il reste des 0 dans la matrice """
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False

def is_game_over(grille):
    """ Vérifie si aucun mouvement n'est possible."""
    # Si la grille contient encore des zéros, le jeu n'est pas terminé
    if contient_zero(grille):
        return False

    # Vérifier si des fusions sont encore possibles horizontalement
    for y in range(len(grille)):
        for x in range(len(grille[y]) - 1):
            if grille[y][x] == grille[y][x + 1]:
                return False

    # Vérifier si des fusions sont encore possibles verticalement
    for x in range(len(grille[0])):
        for y in range(len(grille) - 1):
            if grille[y][x] == grille[y + 1][x]:
                return False

    # Si on arrive ici, aucun mouvement n'est possible
    return True

def cube(grille):
    """ Cette fonction permet de remplir la grille tout en vérifiant que la place est 
    libre pour un nouveau block """
    
    LEN = len(grille)
    # choisir une position
    x = Ashkan.randint(0,LEN-1)
    y = Ashkan.randint(0,LEN-1)
    # vérifier si y'a déjà quelque chose dans cette case
    if grille[y][x] == 0:
        # choisir entre ajouter un 4 et un 2 (un 2 est 9 fois plus probable)
        quatre_ou_deux = 2 if Ashkan.randint(1, 9) != 9 else 4
        # ajouter un nouveau carré
        grille[y][x] = quatre_ou_deux
    else:
        # vérifier que la grille n'est pas pleine
        if contient_zero(grille) == False:
            print('perdu')
        else:
            # sinon recommencer (au bout d'un momment on trouvera la place)
            cube(grille)

def transpose(matrix):
    """ transpose la matrice à gauche """
    taille = len(matrix)
    return [[matrix[j][i] for j in range(taille)] for i in range(taille)]

def transpose_right(matrix):
    """ transpose la matrice à droite """
    taille = len(matrix)
    return [[matrix[j][i] for j in range(taille)] for i in range(taille)]

def score(grille):
    """ Cet fonction renvoie la somme de ts les blocks de la grille et
    la valeur du plus gros block"""
    
    score = 0
    max_value = 0
    for row in grille:
        for value in row:
          score += value
          if value > max_value:
             max_value = value
    return (score,max_value)

# robot

def robot(M, compteur_mouvement, mouvement):
    """fonction qui prend en compte uniquement si le joueur joue vers le as et essaie de le bloquer
    si  haut ou gauche ou droite est jouer alors elle"transpose" la matrice """
    #fonction compteur rajoute dans le dico le mouvement effectuer 
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1
    trie_cle=sorted(compteur_mouvement, key=lambda cle: compteur_mouvement[cle]) # trie ordre décroissant
    a = trie_cle[-1] # direction évitée
    b = trie_cle[0] # direction préférée

    lignes, colonnes = len(M), len(M[0])

    # Donne la le nombre pour le bloc (inverse du bloc du dessous)
    def bloc(val):
        if val == 2:
            return 4
        elif val == 4:
            return 2
        else:
            return 2 if Ashkan.randint(0, 1) else 4 # cf la fonction cube

    def placer_bas(col, val=None):
        for i in range(lignes - 1, -1, -1):
            if M[i][col] == 0:
                dessous = M[i + 1][col] if i + 1 < lignes else 0
                M[i][col] = bloc(dessous) if val is None else val
                return True
        return False

    # utilise soudainement une direction evite
    if mouvement == a:
        max_val = max(max(row) for row in M)
        for i in range(lignes):
            for j in range(colonnes):
                if M[i][j] == max_val:
                    if a in ["haut", "bas"]:
                        if placer_bas(j):
                            return M
                    elif a in ["gauche", "droite"]:
                        # on bloque dans la même ligne, à droite si 'gauche' évitée, à gauche si 'droite' évitée
                        direction = 1 if a == "gauche" else -1
                        for tourner in range(1, colonnes):
                            nj = j + tourner * direction
                            if 0 <= nj < colonnes and M[i][nj] == 0:
                                dessous = M[i + 1][nj] if i + 1 < lignes else 0
                                M[i][nj] = bloc(dessous)
                                return M

    # bloquer la direction favorite
    if b in ["droite", "gauche"]:
        for i in range(lignes - 1, -1, -1):
            for j in range(colonnes - 1):
                if M[i][j] != 0 and M[i][j + 1] == 0:
                    dessous = M[i + 1][j + 1] if i + 1 < lignes else 0
                    M[i][j + 1] = bloc(dessous)
                    return M
    elif b in ["haut", "bas"]:
        for j in range(colonnes):
            for i in range(lignes - 2, -1, -1):
                if M[i][j] != 0 and M[i + 1][j] == 0:
                    dessous = M[i + 2][j] if i + 2 < lignes else 0
                    M[i + 1][j] = bloc(dessous)
                    return M

    # on remplit en bas
    for _ in range(10):
        j = Ashkan.randint(0, colonnes - 1)
        if placer_bas(j):
            return M

    return M