def ficha(nome="<desconhecido>", gol=0):
    jogo = dict()
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    if not nome.strip():
        nome = "<desconhecido>"
    jogo["nome"] = nome
    jogo["gol"] = gol
    return jogo


nome = str(input('Digite o nome: '))
gol = str(input('Digite o numero de gols feitos: '))
jogador = ficha(nome, gol)
print(f'Nome: {jogador["nome"]}')
print(f'Gols: {jogador["gol"]}')

