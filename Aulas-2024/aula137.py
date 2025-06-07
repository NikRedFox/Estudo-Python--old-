# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto 'pai' for apagado, todas as referências dos objetos filhos também são apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('\nAPAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('\nAPAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Av Brasil', 54)
cliente1.inserir_enderecos('Rua B', 6745)
endereco_externo = Endereco('AV Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print('\n--->>AQUI TERMINA O CODIGO<<---')