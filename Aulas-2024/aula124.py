# Escopo da classe e de metodos da classe
class Animal:

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        print(f'O {self.nome} está comendo {alimento}')

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('maçã, limão e pera'))