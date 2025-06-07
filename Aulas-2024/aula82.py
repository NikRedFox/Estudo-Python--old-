"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python. Porém, são funções anonimas que contem
apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
lista = [
    {'nome': 'Maria', 'sobrenome': 'miranda'},
    {'nome': 'Luiz', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'MOreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
"""
lista = [
    {'nome': 'Maria', 'sobrenome': 'Miranda'},
    {'nome': 'Luiz', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
