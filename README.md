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

Télécharger les fichiers [2048.py](./2048.py), [affichage.py](./affichage.py), [matrice.py](./matrice.py) et [mouvements.py](./mouvements.py).

En exécutant le fichier "2048.py", la page d'accueil intéractive s'ouvre, et 4 modes de jeux différents sont proposés à l'utilisateur : "Classique", "Étendue", "Personnalisé" et "Compétitif":
* Classique : c'est le 2048 comme on le connaît: grille 4X4 et apparation aléatoire des blocs
* Etendue : ici, l'utilisateur joue sur une grille 8X8
* Personnalisé : grâce au "entry", l'utilisateur peut choisir une taille de grille (5X5,7X7,...) et jouer en conséquence
* Compétitif : ce mode permet à l'utilisateur de jouer contre un robot, dans ce cas, les blocs n'aparaissent non pas aléatoirement, mais de facon à bloquer le joueur pour le faire perdre plus rapidement. Ce mode ne se joue qu'en grille 4X4

En cliquant sur un de ces 4 boutons, une autre page s'ouvre, affichant la grille (deux blocs sont déjà affichés dans la grille avant même que l'utilisateur commence à jouer), un label "2048", le score de l'utilisateur évoluant à mesure qu'il joue, ainsi que son meilleur score. 

De plus, 3 boutons sont présents dans la barre du haut :

  Fichier : il permet d'enregistrer le fichier ou de l'importer (save et load)
  Pack de couleur : en cliquant dessus, l'utilisateur peut choisir parmis différent thème, qui impliquerait un changement de couleur de la grille, de ses contours, et des blocs. Par défaut, si l'utilisateur ne touche pas à ce bouton, la grille apparaît selon le thème classique du 2048 en ligne
  A propos : ce bouton renvoie au fichier README, au lien du github ou au fichier méthode de travail

Pour jouer, l'utilisateur se sert des flèches haut, bas, gauche, droite du clavier, et les blocs aparaissent dans la grille en conséquence (en fonction du mode de jeu qu'il a choisi).
Lorsque le joueur a perdu (c'est-à-dire lorsqu'il n'y a plus de place pour qu'un bloc aparaisse dans la grille), une page "game over" s'affiche, et un bouton "recommencer" renvoie à la page d'accueil et permet de choisir le mode voulu, puis rejouer.
