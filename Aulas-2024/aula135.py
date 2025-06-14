# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição.
# Geralmente, temos uma associação quando um objeto tem um atrivuto que referencia outro objeto.
# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Nikolas')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina = FerramentaDeEscrever('Maquina')
escritor.ferramenta
escritor.ferramenta = maquina

print(caneta.escrever())
print(maquina.escrever())
# print(escritor.ferramenta.escrever())
