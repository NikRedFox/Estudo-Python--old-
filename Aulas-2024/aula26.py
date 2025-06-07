"""
Formatação basica de strings
    s - string
    d - int
    f - float
    .<numero de digitos>f
    x ou X - Hexadecimal (ABDCEF0123456789)
    (Caractere) (><^) (quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro
    = - Força o numero a aparecer antes dos zeros
    Sinal - + ou -
    Ex.: 0>-100,.1f
    Conversion flags - !r !s !a
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:0^10}')
print(f'{1000.4238762346:+,.2f}')
print(f'O hexadecimal de 1500 é: {1500:08x}')