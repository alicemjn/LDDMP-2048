# Projet de programmation du jeu 2048

Groupe LDDMP
Membres: Erwan Maugeri, Alice Mejane, Danisha Allagapen, Laurène Pan

Lien du github: https://github.com/alicemjn/LDDMP-2048.git <br/>

## Répartition du travail

Nous nous sommes répartis le travail de la manière suivante, tout en mettant nos travaux en commun au fur et à mesure pour assurer une cohérence, et avoir la validation de tous les membres du groupe :
* Alice : interface de la grille, de la page d'accueil et robot
* Laurène : robot et fonction game over
* Erwan : fonctionnement du jeu (déplacements, fusions, animations), intégration de toutes les différentes parties entre elles, supervision (une vue générale de tout le projet est nécessaire pour pouvoir imbriquer toutes les parties entre elles de manière cohérente et sans bugs)
* Danisha : calculs sur la matrice (transpositions, lecture de la matrice) , fonctions score et save (pas terminée)

Voir aussi la documentation [TAVAIL.md](./TRAVAIL.md) pour en apprendre plus sur notre méthodes de travail et de recherches pour ce projet.

## Executer le programme

Télécharger les fichiers [2048.py](./2048.py), [affichage.py](./affichage.py), [matrice.py](./matrice.py) et [mouvements.py](./mouvements.py) et executer le fichier "2048.py"

## Le Jeu

En exécutant le fichier "2048.py", la fenêtre d'accueil intéractive s'ouvre, et 4 modes de jeux différents sont proposés à l'utilisateur : "Classique", "Étendue", "Personnalisé" et "Compétitif":
* Classique : c'est le 2048 comme on le connaît: grille 4X4 et apparation aléatoire des blocs
* Etendue : ici, l'utilisateur joue sur une grille 8X8
* Personnalisé : grâce au "entry", l'utilisateur peut choisir une taille de grille personnalisée (5X5,7X7,...) et jouer en conséquence
* Compétitif : ce mode permet à l'utilisateur de jouer contre un robot, dans ce cas, les blocs n'aparaissent non plus aléatoirement, mais de facon à bloquer le joueur pour le faire perdre plus rapidement. Ce mode ne se joue qu'en grille 4X4 (bien qu'il serait possible d'ajouter une option personnalisable)

En cliquant sur un de ces 4 boutons, une autre fenêtre s'ouvre, affichant la grille (la grille est automatiquement peuplée c'est-à-dire qu'il y a déjà le premier bloc d'affiché dans la grille avant même que l'utilisateur ne commence à jouer), un label "2048", le score de l'utilisateur (évoluant à mesure qu'il joue) et le nombre du plus gros bloc de la grille.

Pour jouer, l'utilisateur utilise les flèches directionnelles de son clavier et les blocs aparaissent dans la grille en conséquence (en fonction du mode de jeu qu'il a choisi).

Lorsque le joueur a perdu (c'est-à-dire lorsqu'il n'y a plus de place pour qu'un bloc aparaisse dans la grille), une page "game over" s'affiche, et il suffit de retourner sur la fenetre d'acceuil pour relancer une partie. À noter qu'il est possible de lancer plusiseurs parties en même temps.

De plus, 3 boutons sont présents dans la barre des menus:
* Fichier : il permet d'enregistrer le fichier ou de l'importer (save et load)
* A propos : ce bouton renvoie au fichier README, au lien du github ou au fichier méthode de travail
* Pack de couleur : en cliquant dessus, l'utilisateur peut choisir parmis différent thème, qui impliquerait un changement de couleur de la grille, de ses contours, et des blocs. Par défaut, si l'utilisateur ne touche pas à ce bouton, la grille apparaît selon le thème classique du 2048 en ligne

## Le principe derrière le jeu

Développé en python avec le module tkinter, le jeu 2048 fonctionne avec une matrice qui est affichée à chaque déplacement des cubes dans la grille. Le programme ouvre d'abord une fenêtre racine. De là on peut ouvrir des fenetres de jeu indépendantes. Lorsque l'on lance une partie, on envoie à une fonction l'information de la taille de la grille. Le programme est dit dynamique c'est-à-dire qu'il fonctionne quel que soit le nombre de lignes et colonnes de la grille 2048. Les 3 premiers boutons sont donc identiques si ce n'est qu'ils ne renvoient pas le même nombre de colonnes/lignes à créer (boutons classique envoie 4 et boutons étendue 8). Le seul boutons qui diffère est le bouton "compétitif" qui active le robot qui analyse la grille et compte les déplacements du joueur.
L'utilisation d'une matrice pour le squelette du jeu 2048 garantit une certaine symétrie des déplacements pusique la direction "bas" pas exemple, est équivalente à la direction "droite" à une transposition de la matrice près (et l'utilisateur n'y voit que du feu puisuq'elle est remise à l'endroit avant d'être affichée).
