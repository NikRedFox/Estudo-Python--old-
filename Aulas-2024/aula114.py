# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]


# metodo reduce
def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preço']


total = reduce(
    funcao_do_reduce, produtos, 0
)
print('total é', total)

# metodo reduce com lambda
total = reduce(
    lambda ac, p: ac + p['preço'], produtos, 0
)
print('\ntotal é', total)


# Metodo normal sem reduce
# total = 0
# for p in produtos:
#    total += p['preço']

# print(total)

# List comprehension
# print(sum([p['preço'] for p in produtos]))

