"""
Exercicio - Unir listas
Crie uma função zipper (como ziper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
Ex.: ['Salvador', 'Ubatuba', 'Belo Horizonte']
     ['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""


def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))


l3 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l4 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l3, l4)))