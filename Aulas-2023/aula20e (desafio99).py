from time import sleep
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' \n{cont} valores foram informados.')
    print(f'O maior valor informado foi {maior}.\n')


maior(9, 2, 5, 6, 2, 7, 10)
maior(34, 65, 23)