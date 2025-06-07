"""
Imprecisão de ponto flutuante
Double-Precision Floating-Point format IEEE 754
"""
import decimal

n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print(n3)
print(f'{n3:.2f}')
print(round(n3, 10))

print( )

n4 = decimal.Decimal('0.1')
n5 = decimal.Decimal('0.7')
n6 = n4 + n5
print(n6)
print(f'{n6:.2f}')
print(round(n6, 2))
