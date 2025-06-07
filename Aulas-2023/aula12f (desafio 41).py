import datetime
ano = int(input('Digite o ano de nascimento: '))
date = datetime.datetime.today().year
c = date - ano
if c <= 9:
    print(f"Idade {c}. MIRIM")
elif c > 9 and c <= 14:
    print(f'Idade {c}. INFANTIL')
elif c > 14 and c <= 19:
    print(f'Idade {c}. JUNIOR')
elif c == 20:
    print(f'Idade {c}. SENIOR')
else:
    print(f'Idade {c}. MASTER')