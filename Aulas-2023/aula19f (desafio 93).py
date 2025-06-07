jogo = dict()
gols = list()
jogo["nome"] = str(input('Nome: '))
jogo["partida"] = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for jogos in range(jogo["partida"]):
    gols.append(int(input(f'Quantos gols na partida {jogos+1}? ')))
print()

jogo["gol"] = gols
soma = 0
for num in gols:
    soma += num
jogo["total"] = soma
print(f'O jogador {jogo["nome"]} jogou {jogo["partida"]} partidas.')
print()

for partidas in range(len(gols)):
    print(f'Partida {partidas+1}: Numero de gols: {gols[partidas]}')

print(jogo)
print(gols)
print(soma)