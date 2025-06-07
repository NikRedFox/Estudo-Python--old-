matrix = [[], [], []]
soma = 0
coluna3 = 0
maior = 0
for d in range(0, 3):
   for c in range(0, 3):
        num = int(input('Digite um numero: '))
        matrix[d].append(num)
        if num % 2 == 0:
           soma += num
        if d == 1 and maior < num:
            maior = num

for row in matrix:
    print(' '. join(['[' + str(num) + ']' for num in row]))
for row in matrix:
    coluna3 += row[2]
print(f'A soma de todos os numeros pares foi: {soma}')
print(f'A soma dos numeros na terceira coluna foi: {coluna3}')
print(f'O maior numero da segunda linha é: {maior}')