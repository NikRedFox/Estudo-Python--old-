"""
Argumentos nomeados e não-nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não-nomeado recebe apenas o argumento (valor)
"""


def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)


soma(1, 2)
soma(x=1, y=2)