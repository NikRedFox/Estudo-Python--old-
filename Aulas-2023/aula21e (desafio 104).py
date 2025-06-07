#def leiaInt():
 #   while True:
  #      try:
   #         numero = int(input('Digite um numero inteiro: '))
   #         return numero
     #   except ValueError:
     #       print('Entrada invalida. Digite um numero inteiro valido.')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'O numero digitado foi: {n}')