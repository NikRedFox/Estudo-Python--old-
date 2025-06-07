"""
Operadores logicos
and, or, not
    and - Todas as condições precisam ser verdadeiras
    Se qualquer valor for considerado falso, a expressão inteira sera
avaliada naquele valor
    São considerados falsy
    0 0.0 ' False
    Também existe o None que é usado para representar um não-valor
"""
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_correta = '123456'

if entrada == 'E' and senha == senha_correta:
    print('Entrar')

else:
    print('Sair')