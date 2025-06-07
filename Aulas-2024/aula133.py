# @property + @setter = getter e setter no modo Pythonico
# - como getter
# - para evitar quebrar codigo cliente
# - para habilitar setter
# - para executar ações ao obter um atributo
# Atributos que começarem com um ou dois underlines não devem ser usados fora da classe.
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no Getter')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('Estou no Setter')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)