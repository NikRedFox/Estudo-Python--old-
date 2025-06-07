import datetime
ano = int(input('Digite o ano em que nasceu: '))
date = datetime.datetime.today().year
c = date - ano
if c < 18:
    print(f'Voce ainda vai se alistar em {18 - c} anos.')
elif c == 18:
    print('Vai se alistar esse ano.')
else:
    print(f'Você ja passou do tempo de alistamento por {c - 18} anos')
