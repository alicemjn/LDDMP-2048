# score de la grille

grille=[[1,0,0,0],[2,0,0,0],[8,0,0,0],[1028,0,0,0]]
                                       
                                       
def score(grille):
    assert isinstance(grille,list) and all(isinstance(row,list)for row in grille), 'Le nombre n\'est pas une matrice !'
    score = 0
    max_value = 0
    for row in grille:
        for value in row:
          score += value
          if value > max_value:
             max_value = value
    return score ,max_value   

print(score(grille))  

                
