a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
d = int(input('Quarto valor: '))
tupla = (a, b, c, d)
print(tupla)
print(f'O numero 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O numero 3 está na posição {tupla.index(3)}')
else:
    print('O valor 3 não aparece')
for c in range(4):
    if (tupla[c] % 2) == 0:
        print(f'Os valores pares foram: {tupla[c]}')

