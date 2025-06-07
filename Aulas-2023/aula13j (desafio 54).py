import datetime
date = datetime.datetime.today().year
ma = 0
me = 0
for year in range(1,8):
    nome = str(input('Digite seu nome: '))
    ano = int(input('Digite o ano em que voce nasceu: '))
    if (date - ano) >= 18:
        ma += 1
    else:
        me += 1
print(f'MAIOR DE IDADE: {ma} \nMENOR DE IDADE: {me}')
