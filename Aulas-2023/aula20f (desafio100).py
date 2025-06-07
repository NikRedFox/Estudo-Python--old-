from random import randint
from time import sleep


def sorteia(lista, quantidade):
    print('Sorteando os valores da lista... ', end='')
    for num in range(quantidade):
        lista.append(randint(1, 10))
        sleep(0.3)
    print('Pronto!')
    return lista


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
           soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros, 5)
somapar(numeros)