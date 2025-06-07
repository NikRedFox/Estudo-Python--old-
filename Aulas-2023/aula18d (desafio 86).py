#matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#for d in range(0, 3):
    #for c in range(0, 3):
        #matrix[d][c] = int(input('Digite um numero: '))

#for d in range(0, 3):
   #for c in range(0, 3):
       #print(f'[{matrix [d][d]: ^5}]', end='')
   #print()

matrix = [[], [], []]
for d in range(0, 3):
    matriz = []
    for c in range(0, 3):
        matriz.append(int(input('Digite um numero: ')))
        matrix[d].append(matriz[c])

for c in matrix:
    print(*c)