def transpose(matrix):
    taille = len(matrix)
    return [[matrix[j][i] for j in range(taille)] for i in range(taille)]

matrix = [[4,4,4,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print("matrix")
for line in matrix:
    print(line)

def transpose_right(matrix):
    return[list(reversed(row)) for row in transpose(matrix)]

matrix_transpose = transpose(matrix)
print("transpose")
for line in matrix_transpose:
    print(line)

matrix_transpose = transpose(matrix_transpose)
print("transpose gauche:")   
for line in matrix_transpose:
    print(line) 

matrix_transpose_right = transpose_right(matrix_transpose)
print("transpose droite:")   
for line in matrix_transpose_right:
    print(line)     
