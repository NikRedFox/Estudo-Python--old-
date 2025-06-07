jogadores = list()

while True:
    jogo = dict()
    jogo["nome"] = str(input('Nome: '))
    jogo["partida"] = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
    gols = list()
    for jogos in range(jogo["partida"]):
        gols.append(int(input(f'Quantos gols na partida {jogos+1}? ')))
    jogo["gol"] = gols
    jogo["total"] = sum(gols)
    jogadores.append(jogo)
    while True:
        resp = str(input('Deseja adicionar outro?: [S/N] ')).upper()[0]
        if resp in "SN":
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print("-=" * 40)
print('cod ', end='')
for i in jogadores[0].keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, jogador in enumerate(jogadores):
    print(f'{k:<4}', end='')
    for d in jogador.values():
        print(f'{str(d):<15}', end='')
    print()
print("-=" * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do Jogador {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]["gol"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-=' * 40)
print(jogadores)