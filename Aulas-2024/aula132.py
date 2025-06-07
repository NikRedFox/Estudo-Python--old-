# @property - um getter no modo Pythonico
# getter -  um metodo para obter um atributo
# cor -> get_cor()
# modo pythonico - modo do Python de fazer as coisas
# @property é uma propriedade do objeto, ela é um metdodo que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - para evitar quebrar codigo cliente
# - para habilitar setter
# - para executar ações ao obter um atributo
# Codigo cliente - é o codigo que usa seu codigo
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('Property')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
