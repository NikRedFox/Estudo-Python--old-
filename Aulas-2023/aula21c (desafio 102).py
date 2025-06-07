def fatorial(num=1, show=False):
    """
    Calcula o Fatorial de um número.
    :param num: O numero a ser calculado.
    :param show: (opcional) Mostra a ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
