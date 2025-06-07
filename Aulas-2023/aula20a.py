def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma é {soma}')


titulo( '    Ata')
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
soma(a, b)