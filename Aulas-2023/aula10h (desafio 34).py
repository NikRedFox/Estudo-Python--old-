s = float(input('Digite o salario: '))
if s > 1250:
    a = (s * 0.10) + s
else:
    a = (s * 0.15) + s
print(f'Seu novo salario é: R${a}')