valores = []
r = 's'
while r != 'n':
    valores.append(int(input('Digite um valor: ')))
    r = input('Deseja continuar? [S/N] ').lower()

par = []
impar = []
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Lista A: {valores}\n'
      f'Lista Par: {par}\n'
      f'Lista Impar: {impar}')