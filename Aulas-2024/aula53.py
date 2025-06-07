"""
enumerate - enumera iteraveis (indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

#lista_enumerada = enumerate(lista)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])