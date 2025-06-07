n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n1 >= n2:
    ma = n1
    me = n2
else:
    ma = n2
    me = n1
if n3 > ma:
    ma = n3
if n3 < me:
    me = n3
print(f'O maior numero é {ma} e o menor é {me}')

