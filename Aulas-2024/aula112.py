from functools import partial
# map - para mapear dados


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},

]


def aumentar(valor, porcentagem):
    return round(valor * porcentagem, 2)


dez_por_cento = partial(
    aumentar, porcentagem=1.1
)


# novos_produtos = [
#    {**p, 'preço': aumentar(p['preço'], 1.1)}
#    for p in produtos
# ]


def muda_preço(produto):
    return {
        **produto, 'preço': aumentar(
            produto['preço']
        )
    }


novos_produtos = map(
    muda_preço,
    produtos
)

print(produtos)
print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))