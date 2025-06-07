# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneca',
    'preço': 2.5,
    'categoria': 'Escritorio',
}

for chave, valor in produto.items():
    print(chave, valor)


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(s1)