"""
Introdução às funções (def) em Python
Funções são trechos de codigo usados para replicar determinada ação ao logo do codigo
Elas podem receber valores para paramtros (argumentos) e retornar um valor especifico.
Por padrão, funções Python retornam None (nada)
"""


def imprimir(a=7, b=8, c=9):
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)
imprimir()