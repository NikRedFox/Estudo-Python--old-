"""
Listas em Python
tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice
    clear - limpa a lista
    extend - extende a lista
    + - concatena listas

"""
#        +01234
#        -54321
string = 'ABCDE'   # caracteres (len)
lista_a = [123, True, 'Nikolas', 1.2, []]

lista_b = [1, 2, 3]
lista_c = [4, 5, 6]
lista_d = lista_b + lista_c
lista_b. extend((lista_c))
print(lista_b)
print(lista_d)

print(lista_a[2], type(lista_a[3]))

lista_a[2] = 'Salokin'
print(lista_a[2])

del lista_a[2]
print(lista_a)

lista_a.append(50)
print(lista_a)

lista_a.pop()
print(lista_a)