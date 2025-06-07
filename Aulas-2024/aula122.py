# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instancias) que podem ter seus proprios atributos e metodos.
# Os objetos gerados pela classe podem usar seus dados internos para realizar varias ações.
# Por convenção, usamos PascalCase para nomes de classes.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Nikolas', 'Barbosa')
#p1.nome = 'Nikolas'
#p1.sobrenome = 'Barbosa'

p2 = Pessoa('Salokin', 'Santos')
#p2.nome = 'Salokin'
#p2.sobrenome = 'Santos'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)