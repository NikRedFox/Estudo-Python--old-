import json
from aula128_a import CAMINHO_ARQUIVO, TantoFaz, fazer_dump

fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = TantoFaz(**pessoas[0])
    p2 = TantoFaz(**pessoas[1])
    p3 = TantoFaz(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)


print(__name__)