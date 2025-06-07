#Empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completas = {**pessoa, **dados_pessoa}

for chave, valor in pessoa.items():
    print(chave, valor)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(**pessoas_completas)