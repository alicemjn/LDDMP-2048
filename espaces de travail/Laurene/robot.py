import random as Ashkan 


M=[[0,0,0,0],
   [0,0,0,0],
   [0,4,5,8],
   [2,8,16,32]]


compteur_mouvement={
    "haut":3,
    "bas":38,
    "gauche":4,
    "droite":23}


def compteur (mouvement):
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1

def valeur( M , i , j ):
     ligne=len(M)
     if i +1 < ligne:
          dessous=M[i+1][j]
          if dessous ==2:
               M[i][j]=4
          elif dessous ==4:
               M[i][j]=2
          else:
               M[i][j]=2 if Ashkan.randint(1,10)<=9 else 4
               

def cube(M,compteur_mouvement):
   a =  max ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
   if a == "bas":
       for i in range(len(M)-1,-1,-1):  # Parcours des lignes de bas en haut
           case_vide=[]
           ligne= M[i]
           for j in range (len(ligne)):
                  if ligne[j]==0:
                    case_vide.append(j)
           if case_vide:
                    index_case=Ashkan.randint(0,len(case_vide)-1)
                    valeur (M, i , index_case)
                    print (M)
                    break
           
       
cube(M,compteur_mouvement)     

# afficher la matrice
print (M[0])
print (M[1])
print (M[2])
print (M[3])


import random as Afshkan

M=[[1,7,2,2],
   [6,9,9,20],
   [0,0,0,2],
   [2,8,16,32]]

def cube_max(M):
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
            if coord_ligne and coord_colone:
                M[coord_ligne+1][coord_colone]=2 if Afshkan.randint(1,10)<=9 else 4
                print(M)
                break 
               
 
   

cube_max(M)

