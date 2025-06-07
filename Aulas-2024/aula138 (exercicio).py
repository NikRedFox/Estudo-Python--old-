# 1- Crie uma classe Carro
# 2- Crie uma classe Motor
# 3- Crie uma classe Fabricante
# 4- Faça uma ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de varios carros
# 5- Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e fabricantes na tela
class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

    def adicionar_motor(self, motor):
        self.motor = motor


class Motor:
    def __init__(self, modelo):
        self.modelo = modelo


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros_fabricados = []

    def fabricar_carro(self, carro):
        self.carros_fabricados.append(carro)
        carro.fabricante = self

    def listar_carros(self):
        for carro in self.carros_fabricados:
            print('Nome:', carro.nome)
            print('Fabricante:', carro.fabricante.nome)
            print('Motor:', carro.motor.modelo, '\n')


fabricante1 = Fabricante('Ford')
fabricante2 = Fabricante('Chevrolet')

motor1 = Motor('1.8v')
motor2 = Motor('2.0v')

carro1 = Carro('Corola', motor1, fabricante1)
carro2 = Carro('Fista', motor2, fabricante2)
carro3 = Carro('Pontiac Aztec', motor1, fabricante2)

fabricante1.fabricar_carro(carro1)
fabricante2.fabricar_carro(carro2)
fabricante2.fabricar_carro(carro3)

print('Carros fabricados pela', fabricante1.nome)
fabricante1.listar_carros()

print('Carros fabricados pela', fabricante2.nome)
fabricante2.listar_carros()


