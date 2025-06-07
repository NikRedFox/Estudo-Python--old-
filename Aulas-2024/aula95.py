# raise - lançando exceções (erros)
def nada_de_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você tentou dividir por zero')

    return True


def int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float\n'
                        f'{tipo_n} enviado')
    return True


def divide(n, d):
    int_ou_float(n)
    int_ou_float(d)
    nada_de_zero(d)
    return n / d


print(divide(8, '0'))