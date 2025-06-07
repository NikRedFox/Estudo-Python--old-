r1 = float(input('Digite o primeiro numero: '))
r2 = float(input('Digite o segudno numero: '))
r3 = float(input('Digite o terceiro numero: '))
if (r1+r2>r3) and (r2+r3>r1) and (r3+r1>r2):
    print('É um triangulo.')
else:
    print('Não é um triangulo.')
