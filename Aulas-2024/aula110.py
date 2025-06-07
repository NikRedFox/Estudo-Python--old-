# Combinations, Permutations e Product - Itertools
# Combination - Ordem não importa - iteravel + tamanho do grupo
# Permutation - ordem importa
# Product - ordem importa e repete valores unicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino',]
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))