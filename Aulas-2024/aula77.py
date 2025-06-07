"""
Manipulando chaves e valores em dicionarios
"""
pessoa = {}
chave = 'nome'

pessoa[chave] = 'Nikolas'
pessoa['sobrenome'] = 'Barbosa'
print(pessoa)

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])