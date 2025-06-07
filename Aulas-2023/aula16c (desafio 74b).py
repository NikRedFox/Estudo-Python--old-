from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = tupla[0]
menor = tupla[0]

for c in range(5):
    if tupla[c] > maior:
        maior = tupla[c]
    elif tupla[c] < menor:
        menor = tupla[c]
print(tupla)
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')