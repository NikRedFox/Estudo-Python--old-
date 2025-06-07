# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *args (ilimitado de argumentos posicionais)
# **kwargs (imilitado de argumentos nomeados)
# Positional-onlyy Parameters (/) - Tudo antes da barra deve ser APENAS posicional:
# PEP 570 - Python Positional-Only Parameters
#     https://peps.python.org/pep-0570/
# Keyword-only Arguments (*) - * sozinho NÃO SUGA valores.
# PEP 3102 - Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def soma(x, y, /, *, z):
    print(x + y + z)


soma(1, 2)
#soma(x=1, y=2)
soma(1, 2, z=3)