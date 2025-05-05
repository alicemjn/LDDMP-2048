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

def robot(M,compteur_mouvement, mouvement):
    """  """
    #fonction compteur rajoute dans le dico le mouvement effectuer 
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1
    trie_cle=sorted(compteur_mouvement, key=lambda cle: compteur_mouvement[cle])
    a =   trie_cle[0]
    b =   trie_cle[-1]
    c =   trie_cle[1]      

    # decide de lapparition du cube si la strategie est bas gauche et si le mouvement 
    # effctuer est bas ou gauche                
    
    if (a == "bas" and c=="gauche") and (mouvement == "bas" or mouvement=="gauche"):
       for i in range(len(M)-1,-1,-1):  # Parcours des lignes de bas en haut
           case_vide=[]
           ligne= M[i]
           for j in range (len(ligne)):
                if ligne[j]==0:
                    case_vide.append(j)
           if case_vide:
                
                index_case=case_vide[0]
                if i < len(M) - 1:
                    dessous=M[i+1][j]
                    if dessous ==2:
                        M[i][index_case]=4
                    elif dessous ==4:
                        M[i][index_case]=2
                    else:
                        M[i][index_case]=2 if Ashkan.randint(1,10)<=9 else 4
                else:
                    M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4

                return M


    # decide de lapparition du cube si la strategie est bas droite et si le mouvement 
    # effctuer est bas ou droite
    
    if (a == "bas" and c=="droite") and (mouvement == "bas" or mouvement=="droite"):
       for i in range(len(M)-1,-1,-1):  # Parcours des lignes de bas en haut
           case_vide=[]
           ligne= M[i]
           for j in range (len(ligne)):
                if ligne[j]==0:
                    case_vide.append(j)
           if case_vide:
                
                index_case=case_vide[-1]
                if i < len(M) - 1:
                    dessous=M[i+1][j]
                    if dessous ==2:
                        M[i][index_case]=4
                    elif dessous ==4:
                        M[i][index_case]=2
                    else:
                        M[i][index_case]=2 if Ashkan.randint(1,10)<=9 else 4
                else:
                    M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4
                return M


    # decide de lapparition du cube si la strategie est haut gauche et si le mouvement 
    # effctuer est haut ou gauche

    if (a == "haut" and c=="gauche")and( mouvement == "haut" or mouvement=="gauche"):
        for i in range(len(M)):  
            case_vide = []
            ligne = M[i]
            for j in range(len(ligne)):
                if ligne[j] == 0:
                    case_vide.append(j)
            if case_vide:
                
                index_case = case_vide[0] 
                if i > 0:
                    dessus = M[i - 1][index_case]
                    if dessus == 2:
                        M[i][index_case] = 4
                    elif dessus == 4:
                        M[i][index_case] = 2
                    else:
                        M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4
                else:
                    M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4
                
                return M

    # decide de lapparition du cube si la strategie est haut droite et si le mouvement 
    # effctuer est haut ou droite

    if (a == "haut" and c=="droite") and (mouvement == "haut" or mouvement=="droite"):
        for i in range(len(M)):  
            case_vide = []
            ligne = M[i]
            for j in range(len(ligne)):
                if ligne[j] == 0:
                    case_vide.append(j)
            if case_vide:
                
                index_case = case_vide[-1] 
                if i > 0:
                    dessus = M[i - 1][index_case]
                    if dessus == 2:
                        M[i][index_case] = 4
                    elif dessus == 4:
                        M[i][index_case] = 2
                    else:
                        M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4
                else:
                    M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4

                return M


    #decide de la position du cube si strat haut et mouveent bas         
    
    if mouvement == "bas" and b == "bas":   
        ligne = len(M)
        colone = len(M[0])
        for i in range(ligne - 2, -1, -1):  # Parcours des lignes de bas en haut
            if 0 in M[i]:  
                max_val = -1
                coord_ligne = None
                coord_colone = None
                for j in range(colone):
                    if M[i][j] == 0 and M[i + 1][j] > max_val:  # Comparaison avec la ligne en dessous
                        max_val = M[i + 1][j]
                        coord_ligne = i + 1 
                        coord_colone = j
                if coord_ligne is not None and coord_colone is not None:
                    M[coord_ligne - 1][coord_colone] = 2 if Ashkan.randint(1, 10) <= 9 else 4
                    return M


    #decide de la position du cube si strat bas et mouvement haut

    if mouvement =="haut" and b=="haut" :   
      ligne = len(M)
      colone = len(M[0])
      for i in range(1, ligne):  
        if 0 in M[i]:  
            max_val = -1
            coord_ligne = None
            coord_colone=None
            for j in range(colone):
                if M[i][j] == 0 and M[i - 1][j] > max_val:  
                    max_val = M[i - 1][j]
                    coord_ligne = i - 1 
                    coord_colone=j
                    if coord_ligne is not None and coord_colone is not None:
                        M[coord_ligne+1][coord_colone]=2 if Ashkan.randint(1,10)<=9 else 4
                        return M

    #si le compteur ne permet pas encore le fonctionement du programme ou le joueur nas pas de strategie
    
    else :
        case_vide=[]
        for j in range(len(M[0])):       
          for i in range(len(M)):      
           if M[i][j] == 0:
            case_vide.append((i, j))  

        if case_vide:
          index = Ashkan.randint(0, len(case_vide) - 1)
          i, j = case_vide[index]
          M[i][j] = 2 if Ashkan.randint(1, 10) <= 9 else 4
        else:
            print("perdu")