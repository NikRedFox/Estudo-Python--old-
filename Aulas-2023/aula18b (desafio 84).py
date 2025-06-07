temp = list()
dados = list()
cont = 0
maior = menor = 0
r = 'S'
while r != 'N':
    temp.append((str(input('Nome: '))))
    temp.append(int(input('Peso: ')))
    if cont == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    r = str(input('Continuar? [S/N] ')).upper()
    cont +=1

print(f'{cont} pessoas foram cadastradas')
print(f'O maior peso foi {maior}Kg de ', end='')
for v in dados:
    if v[1] == maior:
        print(f'{v[0]}... ', end='')
print()
print(f'O menor peso foi {menor}Kg de ', end='')
for v in dados:
    if v[1] == menor:
        print(f'{v[0]}... ', end='')