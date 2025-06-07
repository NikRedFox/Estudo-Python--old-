"""
Interpolação basica de strings
    s - string
    d e i - int
    f - float
    x & X - Hexadecimal (ABDCEF0123456789)
"""

nome = 'Luiz'
preço = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preço)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))