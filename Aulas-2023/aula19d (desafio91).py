import random
import operator
jogo = {'Jogador 1' : random.randint(1, 6),
        'Jogador 2' : random.randint(1, 6),
        'Jogador 3' : random.randint(1, 6),
        'Jogador 4' : random.randint(1, 6)}

ranking = list()

print('Valores sorteados: ')
for chave, valores in jogo.items():
    print(f'{chave} tirou {valores} no dado')
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    print(f'{indice+1}° lugar: {valor[0]} com {valor[1]} pontos')