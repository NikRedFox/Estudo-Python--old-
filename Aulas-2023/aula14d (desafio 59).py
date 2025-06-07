r = 0
es = 0
n1 = float(input('1° Numero: '))
n2 = float(input('2° Numero: '))
while es != 5:
    es = int(input('[1] Somar \n'
      '[2] Multiplicar \n'
      '[3] Maior \n'
      '[4] Novos numeros \n'
      '[5] Sair do programa \n'
      'Escolha uma opção: '))
    if es == 4:
        n1 = float(input('1° Numero: '))
        n2 = float(input('2° Numero: '))
        es = int(input('[1] Somar \n'
          '[2] Multiplicar \n'
          '[3] Maior \n'
          '[4] Novos numeros \n'
          '[5] Sair do programa \n'
          'Escolha uma opção: '))
    elif es == 1:
       r = n1 + n2
       print(f'A soma de {n1} com {n2} é: {r}')
    elif es == 2:
       r = n1 * n2
       print(f'A multiplicação de {n1} com {n2} é: {r}')
    elif es == 3:
        if n1 > n2:
            print (f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else :
            print('Os dois são iguais')
print('Fim')