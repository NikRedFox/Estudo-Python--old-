n = int(input('Digite um numero inteiro: '))
e = int(input(('1 - Transformar em binario\n'
               '2 - Transformar em octal\n'
               '3 - Transformar em hexadecimal\n'
               'Escolha uma das opções: ')))
if e == 1:
   nb = bin(n)
   print(f'O numero {n} em binario é {nb}')
elif e == 2:
    no = oct(n)
    print(f'O numero {n} em octal é {no}')
elif e == 3:
    nh = hex(n)
    print(f'O numero {n} em hexadecimal é {nh}')
else:
    print('Opção invalida.')