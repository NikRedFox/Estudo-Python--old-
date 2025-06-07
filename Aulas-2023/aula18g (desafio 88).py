import random
jogos = []
num = int(input('Quantos jogos quer que sejam sorteados? '))

for c in range(num):
    jogo = random.sample(range(1, 61), 6)
    jogos.append(jogo)

for i, jogo in enumerate(jogos):
    print(f'Jogo N°{i+1}: {jogo}')
print(jogos)