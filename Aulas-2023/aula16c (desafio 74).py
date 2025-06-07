import random
a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
d = random.randint(0,10)
e = random.randint(0,10)
maior = a
menor = a
tupla = (a, b, c, d, e)
if maior < b:
    maior = b
if maior < c:
    maior = c
if maior < d:
    maior = d
if maior < e:
    maior = e
if menor > b:
    menor = b
if menor > c:
    menor = c
if menor > d:
    menor = d
if menor > e:
    menor = e
print(tupla)
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')