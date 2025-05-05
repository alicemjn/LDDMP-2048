import random as Afshkan 


#M=[[0,0,0,0],
   ##[0,4,2,2],
   #[2,8,16,32]]


#compteur_mouvement={
    #"haut":3,
    #"bas":38,
    #"gauche":4,
    #"droite":23}


#def compteur (mouvement):
    #if mouvement in compteur_mouvement :
       # compteur_mouvement[mouvement]+=1

#def valeur( M , i , j ):
     #ligne=len(M)
     #if i+1 < ligne:
       #dessous=M[i+1][j]
       ###M[i][j]=4
       #elif dessous ==4:
               #M[i][j]=2
               

       
#def cube(M,compteur_mouvement):
   ##if a == "bas":
       #for i in range(len(M)-1,-1,-1):  # Parcours des lignes de bas en haut
           #case_vide=[]
           #ligne= M[i]
           #for j in range (len(ligne)):
                  #if ligne[j]==0:
                    #case_vide.append(j)
           #if case_vide:
                    #index_case=Afshkan.randint(0,len(case_vide)-1)
                    #M[i][index_case]= 2
                    #break

#cube(M,compteur_mouvement) 

# afficher la matrice


# ça marche pas encore très bien ...
# essaye:
# regarder 1ere ligne non complète en partant du bas (ça t'as fait normalement)
# parcourir cette ligne et noter les indices i et n de chaque case vide (=0) de la liste
# t'as donc une liste avec des couples i n 
# choisir aléatoirement un couple i n dans la liste
# on fixe le coupe i n de la case cible (on note ce couple choisit aléatoirement a)
# regrader la case d'en dessous c'est à dire
#   regarder la valeur de la case i n-1 (ou i-1 n selon ce que i et n représente [colonne ou ligne])
#   soit b cette valeur
#   si b = 2 placer un 4 à la case a
#   si b = 4 placer un 2 à la case a
#   else placer un 2 ou un 4 (aléatoirement où 2 à 9 fois + de chance d'apparaitre [voir fct cube])

#   deuxième partie ... (je vais la faire je pense)
#   un dico compte le nombres de déplacements
#   à chaque début de fct regarder quelle direction ressort le plus
#   obtenir la dernière direction jouée (via argument de la fonction) rappel la fct prend 3 arg: grille, dico, derbière direction
#   trouver la direction la moins jouée appelée preférence
#   si la dernière direction jouée n'est pas égale à préférence alors executer le programme décrit plus haut
#   sinon créer un programme sur le modèle de ce qui est écrit plus haut qui place un 2 en dessous de la meilleur case du joeur
# 
# Généralisation: jouer vers le bas est équivalent à jouer vers la droite si on transpose 1 fois la matrice de droite à gauche:
# [0,1]
# [0,1]
# <=>
# [0,0]
# [1,1]
# géneraliser avec ça : transformer les matrice en matrice ou la direction "préférence" devient systématiquement "haut"
import random as Ashkan 


M=[[10,0,0,0],
   [0,0,0,0],
   [0,4,2,0],
   [2,8,16,32]]


compteur_mouvement={
    "haut":12,
    "bas":1000,
    "gauche":21,
    "droite":60}




def compteur(compteur_mouvement, mouvement):
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1
        trie_cle = sorted(compteur_mouvement, key=lambda cle: compteur_mouvement[cle])
        a =   max ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
        b =   min ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
        c =   trie_cle[-2]
        print(a, b,c ,compteur_mouvement)


def cube_max(M,mouvement,compteur_mouvement):
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1
        print(compteur_mouvement)
    trie_cle = sorted(compteur_mouvement, key=lambda cle: compteur_mouvement[cle])
    a =   max ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
    b =   min ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
    c =   trie_cle[-2]
    print(compteur_mouvement, c)
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

                print(M)
                break
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

                print(M)
                break
cube_max(M,"droite",compteur_mouvement)


def cube_max2(M,mouvement,compteur_mouvement):
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1
        print(compteur_mouvement)
    trie_cle = sorted(compteur_mouvement, key=lambda cle: compteur_mouvement[cle])
    a =   max ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
    b =   min ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
    c =   trie_cle[-2]
    print(compteur_mouvement, c)
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

                print (M)
                break
           
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

                print (M)
                break



cube_max2(M,"bas",compteur_mouvement)