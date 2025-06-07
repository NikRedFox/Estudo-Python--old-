maior = 0
menor = 0
n1 = 0
n2 = 0
count = 0
r = 'S'
while r != 'N':
    n1 = int(input('Digite um numero: '))
    r = str(input('Gostaria de digitar outro? [S/N]: ')).upper()
    count += 1
    n2 += n1
    if count == 1:
        maior = n1
        menor = n1
    if n1 > menor:
        maior = n1
    elif n1 < menor:
        menor = n1

print(f'O maior numero foi: {maior} \n'
      f'O menor numero foi {menor} \n'
      f'A media é: {n2 / count:.2f} ')