"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

resultado
lista_soma = [2, 4, 6, 8]
"""


def soma(la, lb):
    intervalo_maximo = min(len(la), len(lb))
    return [
        (la[i] + lb[i]) for i in range(intervalo_maximo)
    ]


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print(soma(lista_a, lista_b))

# Solução generica
# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = []             #   lista_soma = [x + y for x, y in zip(lista_a, lista_b)] dispensa o for abaixo,
#                                 mas é uma maneira mais python de resolver e não deve funcionar em outras linguas
# for i in range(len(lista_b)):
#   lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)
