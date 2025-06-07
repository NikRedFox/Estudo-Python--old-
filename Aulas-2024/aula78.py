"""
Metodos uteis dos dicionarios em Python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""
import copy

pessoa = {
    'nome': 'Nikolas',
    'sobrenome': 'Barbosa',
}
pessoa.setdefault('idade', 0)
print(len(pessoa))
print(pessoa.keys())
print(list(pessoa.values()))
print(list(pessoa.items()))
print(pessoa['idade'])
print()

# Shallow copy (copia valores imutaveis, mas apenas linka valores mutaveis)
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = copy.copy(d1)

d2['c1'] = 100
d2['l1'][1] = 999999

print(d1)
print(d2)

# Deep copy (copia completa para uma lista separada)
d3 = {
    'c3': 3,
    'c4': 4,
    'l2': [3, 4, 5],
}
d4 = copy.deepcopy(d3)

d4['c3'] = 100
d4['l2'][1] = 999999

print()
print(d3)
print(d4)
print()

# pop e popitem
p1 = {
    'nome': 'Nikolas',
    'sobrenome': 'Barbosa',
}
print(p1.get('nome'))
print(p1.get('idade', 'Não existe\n'))

nome = p1.pop('nome')
print(nome)
print(p1)
print()

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
print()

# update (pode mudar valor de chaves ou criar novas)
p1.update({
    'nome': 'Maria',
    'idade': 30,
})
print(p1)