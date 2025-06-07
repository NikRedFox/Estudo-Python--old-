r1 = float(input('Digite o primeiro numero: '))
r2 = float(input('Digite o segudno numero: '))
r3 = float(input('Digite o terceiro numero: '))
if (r1 == r2) and (r1 == r3) and (r2 == r3):
    print('É um triangulo equilatero.')
elif (r1 == r2) or (r2 == r3):
    print('É um triangulo isosceles.')
elif (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Não é um triangulo.')
else:
    print('É um triangulo escaleno.')
