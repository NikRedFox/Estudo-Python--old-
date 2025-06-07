# -Funções do exercicio 107
def metade(n, fmt=False):
    res = n / 2
    return res if fmt is False else moeda(n)


def dobro(n=0, fmt=False):
    res = n * 2
    return res if fmt is False else moeda(n)


def aumentar(n=0, percent=0, fmt=False):
    res = n + (n * percent / 100)
    return res if fmt is False else moeda(res)


def diminuir(n=0, percent=0, fmt=False):
    res = n - (n * percent / 100)
    return res if fmt is False else moeda(res)


# -Função adicionada no exercicio 108
# -Adicionado as condições nas funções no exercicio 109
def moeda(n=0, moeda='R$', fmt=True):
        return f'{moeda}{n:.2f}'.replace('.', ',')


# -Função adicionada no exercicio 110
def resumo(n=0, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO'.center(30))
    print('-' * 30)

    print('Preço analisado:', moeda(n))
    print('Dobro do preço: ', dobro(n, True))
    print('Metade do preço:', metade(n, True))
    print(f'{aumento}% de aumento:', aumentar(n, aumento, True))
    print(f'{reducao}% de redução:', diminuir(n, reducao, True))

    print('-' * 30)
