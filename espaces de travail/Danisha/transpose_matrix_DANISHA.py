def transpose(matrix):
    taille = len(matrix)
    return [[matrix[j][i] for j in range(taille)] for i in range(taille)]

matrix = [[4,4,4,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def transpose_right(matrix):
    return[list(reversed(row)) for row in transpose(matrix)]


matrix_transpose = transpose(matrix)
'''cette fonction permet de transposer la matrice a gauche'''
print("transpose gauche:")   
for line in matrix_transpose:
    print(line) 

matrix_transpose_right = transpose_right(matrix)
'''cette fonction permet de transposer la matrice a droite'''
print("transpose droite:")   
for line in matrix_transpose_right:
    print(line)     
