import math
an = float(input('Digite um angulo: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print(f'Angulo {int(an)}° \nSeu seno é: {s:.2f} \nSeu cosseno é: {c:.2f} \nSua tangente é: {t:.2f}')