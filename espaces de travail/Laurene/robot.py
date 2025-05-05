import random as Ashkan 


M=[[2,0,0,25],
   [0,0,0,0],
   [0,0,0,0],
   [15,0,39,0]]


compteur_mouvement={
    "haut":123,
    "bas":1,
    "gauche":5,
    "droite}":23}



        
def cube(M,compteur_mouvement, mouvement) :  
#fonction compteur rajoute dans le dico le mouvement effectuer 
    if mouvement in compteur_mouvement :
        compteur_mouvement[mouvement]+=1
        trie_cle=sorted(compteur_mouvement, key=lambda cle: compteur_mouvement[1])
    a =   max ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
    b =   min ( compteur_mouvement, key= lambda cle :compteur_mouvement [cle] )
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

                print (M)
                break


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

                print (M)
                break


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

                print(M)
                break


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

                print(M)
                break


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
                    print(M)
                    break


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
                        print(M)
                        break


    

cube(M,compteur_mouvement,"bas")


#v1 pren en compte mouvement bas strat bas 
    #if a == "bas" and mouvement=="bas" :
       #for i in range(len(M)-1,-1,-1):  # Parcours des lignes de bas en haut
           #case_vide=[]
           #ligne= M[i]
           #for j in range (len(ligne)):
                #if ligne[j]==0:
                    #case_vide.append(j)
           #if case_vide:
                #index_case=Ashkan.randint(0,len(case_vide)-1)
                #index_case=case_vide[index_case]
                ##
                # dessous=M[i+1][j]
                    #if dessous ==2:
                        #M[i][index_case]=4
                    #elif dessous ==4:
                        #M[i][index_case]=2
                    #else:
                       # M[i][index_case]=2 if Ashkan.randint(1,10)<=9 else 4
                #else:
                   # M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4

                #print (M)
                #break

#v1 si strat bas et mouvement haut

    #if mouvement =="haut" and b=="haut" :   
      #ligne = len(M)
      #colone = len(M[0])
      #for i in range(1, ligne):  
        #if 0 in M[i]:  
            #max_val = -1
            #coord_ligne = None
            #coord_colone=None
            #for j in range(colone):
                #if M[i][j] == 0 and M[i - 1][j] > max_val:  
                    #max_val = M[i - 1][j]
                    #coord_ligne = i - 1 
                    #coord_colone=j
                   # if coord_ligne is not None and coord_colone is not None:
                       # M[coord_ligne+1][coord_colone]=2 if Ashkan.randint(1,10)<=9 else 4
                       #print(M)
                       #break

#v1 si strat haut mouvement haut


#if a == "haut" and mouvement == "haut":
        #for i in range(len(M)):  
            #case_vide = []
            #ligne = M[i]
            #for j in range(len(ligne)):
                #if ligne[j] == 0:
                    #case_vide.append(j)
            #if case_vide:
                #index_case = Ashkan.randint(0, len(case_vide) - 1)
                #index_case = case_vide[index_case] 
                #if i > 0:
                    #dessus = M[i - 1][index_case]
                    #if dessous == 2:
                       # M[i][index_case] = 4
                    #elif dessous == 4:
                       # M[i][index_case] = 2
                   # else:
                        #M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4
                #else:
                    #M[i][index_case] = 2 if Ashkan.randint(1, 10) <= 9 else 4

               # print(M)
               # break