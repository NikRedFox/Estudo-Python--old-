# Métodos em instancias de classes Python
# Hard coded é algo que foi escrito diretamente no codigo
# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instancia da class (objeto) - Tem os dados
# Uma classe pode gerar varias instancias.
# Na classe o self é a propria instancia.

class Carro:
    def __init__(self, nome):
        # self.nome = 'Fusca'  # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()