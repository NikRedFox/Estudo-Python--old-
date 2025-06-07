num = int(input('Digite um numero: '))
o = 0
for c in range(1, num + 1):
    if num % c == 0:
        o += 1
print(f'O numero {num} foi divisivel {o} vezes. ')
if o == 2:
    print('O numero é primo.')
else:
    print('O numero não é primo.')
