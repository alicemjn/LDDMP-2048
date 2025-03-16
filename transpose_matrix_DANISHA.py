def transpose(matrix):
    taille = len(matrix)
    return [[matrix[j][i] for j in range(taille)] for i in range(taille)]

matrix = [[4,4,4,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print("matrix")
for line in matrix:
    print(line)

matrix_transpose = transpose(matrix)
print("transpose")
for line in matrix_transpose:
    print(line)