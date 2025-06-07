# Exercicio - Salve a sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instancias da classe com os dados salvos
# Faça em arquivos separados
import json


class TantoFaz:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


CAMINHO_ARQUIVO = 'aula128a.json'

objeto1 = TantoFaz('Julio', 30)
objeto2 = TantoFaz('Maria', 25)
objeto3 = TantoFaz('Jenny', 34)
lista = [vars(objeto1), objeto2.__dict__, vars(objeto3)]


def fazer_dump():
    print('Fazendo Dump')
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
       json.dump(lista, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE É O MAIN')
    fazer_dump()