soma = 0
cont = 0
for n in range(6):
    num = int(input(f'Digite o {n+1}° numero: '))
    if (num % 2) == 0:
        soma += num
        cont += 1
print(f'Foram informados {cont} numeros pares e sua soma é {soma}')