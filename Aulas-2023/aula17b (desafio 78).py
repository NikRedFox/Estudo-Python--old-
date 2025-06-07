valores = []
maior = menor = 0

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    maior = menor = valores[0]

for c in range(5):
    if valores[c] > maior:
        maior = valores[c]
    elif valores[c] < menor:
        menor = valores[c]
print(valores)
print(f'O maior foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')