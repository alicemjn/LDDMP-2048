
grille = [[2,0,0,0],
          [2,0,0,0],
          [2,0,0,0],
          [2,0,0,0]]

def score(grille):
    
    assert isinstance(grille,list)and all(isinstance(row,list)for row in grille), 'Le nombre n\'est pas une matrice !'
    score=0
    for row in grille:
        for value in row:
          score+=value
    return score    
print(score(grille))      
                
