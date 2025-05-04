import random as Ashkan
import config


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

def matrice_en_int(grille):
    for n in range(len(grille)):
        for i in range(len(grille[n])):
            if isinstance(grille[n][i], str) and grille[n][i].isdigit():
                grille[n][i] = int(grille[n][i])
            elif grille[n][i] == "X":
                pass

def contient_zero(grille):
    for ligne in grille:
        for nombre in ligne:
            if nombre == 0:
                return True
    return False


def cube(grille):
    """Remplit la grille en ajustant les probabilités des blocs à apparaître selon les blocs environnants."""
    LEN = len(grille)
    x = Ashkan.randint(0, LEN - 1)
    y = Ashkan.randint(0, LEN - 1)

    if grille[y][x] == 0:
        # Logique pour détermination du bloc
        bloc = None
        if config.mode == "classique":
            bloc = 2 if Ashkan.randint(1, 10) != 10 else 4
        elif config.mode == "difficile":
            total_voisins, count_2, count_4, count_8 = analyse_voisins(grille, x, y)
            bloc = probabilites_difficiles(total_voisins, count_2, count_4, count_8)
        elif config.mode == "Ô Rage, Ô Désespoir":
            count_X = sum(row.count('X') for row in grille)
            if count_X < 3 and Ashkan.random() < 0.1:  # Limiter le nombre d'apparitions 'X'
                bloc = 'X'
            else:
                total_voisins, count_2, count_4, count_8 = analyse_voisins(grille, x, y)
                bloc = probabilites_supra_hardcore(total_voisins, count_2, count_4, count_8)
        else:
            bloc = 2

        grille[y][x] = bloc
    else:
        if not contient_zero(grille):
            # Vérifier si le jeu est terminé
            if is_game_over(grille):
                print('perdu')
                return True  # Indique que le jeu est terminé
            else:
                # Il reste des mouvements possibles malgré l'absence de zéros
                return False
        else:
            cube(grille)  # Essayer une autre position

    return False  # Le jeu continue

def analyse_voisins(grille, x, y):
    LEN = len(grille)
    voisins = [
        grille[y - 1][x] if y > 0 else None,
        grille[y + 1][x] if y < LEN - 1 else None,
        grille[y][x - 1] if x > 0 else None,
        grille[y][x + 1] if x < LEN - 1 else None
    ]

    count_2 = voisins.count(2)
    count_4 = voisins.count(4)
    count_8 = voisins.count(8)
    total_voisins = count_2 + count_4 + count_8

    return total_voisins, count_2, count_4, count_8

def probabilites_difficiles(total_voisins, count_2, count_4, count_8):
    if total_voisins > 0:
        prob_2 = (count_2 / total_voisins) * 0.1
        prob_4 = (count_4 / total_voisins) * 0.5
        prob_8 = (count_8 / total_voisins) * 0.6
    else:
        prob_2, prob_4, prob_8 = 0.4, 0.5, 0.6

    random_choice = Ashkan.random()
    if random_choice < prob_2:
        bloc = 2
    elif random_choice < prob_2 + prob_4:
        bloc = 4
    else:
        bloc = 8

    return bloc

def probabilites_supra_hardcore(total_voisins, count_2, count_4, count_8):
    if total_voisins > 0:
        prob_2 = (count_2 / total_voisins) * 0.1
        prob_4 = (count_4 / total_voisins) * 0.2
        prob_8 = (count_8 / total_voisins) * 0.3
    else:
        prob_2, prob_4, prob_8 = 0.1, 0.2, 0.3

    random_choice = Ashkan.random()
    if random_choice < prob_2:
        bloc = 2
    elif random_choice < prob_2 + prob_4:
        bloc = 4
    elif random_choice < prob_2 + prob_4 + prob_8:
        bloc = 8
    else:
        bloc = 16

    return bloc

def transpose(matrix):
    taille = len(matrix)
    return [[matrix[j][i] for j in range(taille)] for i in range(taille)]