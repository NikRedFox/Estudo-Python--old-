import math
n1 = float(input('Digite o cateto adjacente: '))
n2 = float(input('Digite o cateto oposto: '))
ca = n1 * n1
co = n2 * n2
h1 = ca + co
h2 = math.sqrt(h1)
print(f'O quadrado da hipoternusa seria {h1}, e, sua raiz quadrada é: {int(h2)}')

#import math
#co = float(input('Digite o cateto adjacente'))
#ca = float(input('Digite o cateto adjacente'))
#h = math.hypot(ca, co)
#print(f'A hipotenusa vai medir {h}')