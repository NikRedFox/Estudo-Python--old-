n1 = 0
n2 = 0
count = 0
while n1 != 999:
    n1 = int(input('Digite um numero: '))
    count += 1
    n2 += n1
print(f'Foram digitados {count} numeros, e, sua soma é {n2}')