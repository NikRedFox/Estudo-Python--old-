pessoas = list()
dados = list()
totma = 0
totme = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totma += 1
    else:
        print(f'{p[0]} é menor de idade')
        totme += 1

print(f'Temos {totma} maiores e {totme} menores de idade')
print(pessoas)