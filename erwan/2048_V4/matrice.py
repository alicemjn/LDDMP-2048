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

def cube(grille):
    """ Cette fonction permet de remplir la grille tout en vérifiant que la place est libre pour un nouveau block """
    LEN = len(grille)
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