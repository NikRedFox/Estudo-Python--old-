"""
List comprehension em Python
List comprehension é uma forma rapida para criar listas a partir de iteraveis
print(list(range(10)))
"""

lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

#lista = [numero for numero in range(10)]
lista = [numero * 2 for numero in range(10)]
print(list(range(10)))
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 20,},
    {'nome': 'p2', 'preço': 10,},
    {'nome': 'p3', 'preço': 30,},
]

novos_produtos = [
    # {'nome': produto['nome'], 'preço': produto['preço']}
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05) > 10
]
print(novos_produtos)
print(*novos_produtos, sep='\n')

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]
print(lista)