import random as Ashkan

# fonctions

def matrice_en_int(grille):
    for n in range(len(grille)):  # Parcours des lignes
        for i in range(len(grille[n])):  # Parcours des colonnes
            if isinstance(grille[n][i], str):  # Vérifie si c'est une string
                grille[n][i] = int(grille[n][i])  # Convertit en int

def contient_zero(grille):
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False

def is_game_over(grille):
    """Vérifie si aucun mouvement n'est possible."""
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