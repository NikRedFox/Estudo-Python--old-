n1 = int(input('Digite um numero: '))
num = 1
r = 1
while num <= n1:
    r = r * num
    num += 1
print(f'O fatorial de {n1} é: {r}')