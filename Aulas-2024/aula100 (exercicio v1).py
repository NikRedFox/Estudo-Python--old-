import copy


def formatacao(lista):
    for produto in lista:
        print(f'{produto["nome"]}: R${produto["preco"]:.2f}')
    return


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos = copy.deepcopy(produtos)  # Criar uma deepcopy da lista original

for produto in novos_produtos:
    produto['preco'] = produto['preco'] * (1 + (10/100))  # Aumentar 10% dos preços


produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)  # Deepcopy da lista com os preços novos
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)   # Ordenar os nomes por ordem decrescente

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)  # Deepcopy da lista com ordem decrescente
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])  # Ordenar os preços por ordem crescente


print('Produtos Originais:')
formatacao(produtos)

print('\nNovos Produtos:')
formatacao(novos_produtos)

print('\nProdutos Ordenados por nome:')
formatacao(produtos_ordenados_por_nome)

print('\nProdutos Ordenados por preço:')
formatacao(produtos_ordenados_por_preco)