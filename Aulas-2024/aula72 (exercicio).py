def multiplica(*args):
    total = 1
    for numero in args:
        print(f'Total = {total} X {numero}')
        total *= numero
        print(f'Total = {total}')
    return total


def fala(numeros):
    if numeros % 2 == 0:
        print(f'O resultado é par')
        return
    print('O resultado é impar')
    return


numeros = multiplica(1, 3, 5)
print(numeros)
fala(numeros)
