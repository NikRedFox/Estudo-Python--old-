ced = 50
total = 0
saque = int(input('Bem vindo usuario! \n'
                  'Informe o valor do saque: R$'))
while True:
    if saque >= ced:
        saque -= ced
        total += 1
    else:
        if total > 0:
            print(f'Total de {total} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total = 0
        if saque == 0:
            break