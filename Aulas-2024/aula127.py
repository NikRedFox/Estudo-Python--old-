# __dict__ e varts para atributos de instancia

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


# p1 = Pessoa('João', 37)
# print(p1.__dict__)
# print(vars(p1))

# p1.__dict__['outra'] = 'coisa'
# print(p1.outra)

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

print(vars(p1))
print(p1.nome)