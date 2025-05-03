import random as Afshkan 


M=[[0,0,0,0],
   [0,0,0,0],
   [0,0,2,2],
   [4,8,16,32]]


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
               M[i][j]=2 if Afshkan.randint(1,10)<=9 else 4
               


       
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
                    index_case=Afshkan.randint(0,len(case_vide)-1)
                    valeur (M, i , index_case)
                    print (M)
                    break
           
       
cube(M,compteur_mouvement)              


