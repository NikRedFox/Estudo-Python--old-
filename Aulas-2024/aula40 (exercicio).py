"""Calculadora While"""
print('-' * 5, 'Calculadora', '-' * 5)
while True:
    try:
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        break
    except ValueError:
        print('Não são permitidas letras ou caracteres especiais')

while True:
    print('-' * 25)
    conta = int(input('[1] - Soma'
                      '\n[2] - Subtração'
                      '\n[3] - Multiplicação'
                      '\n[4] - Divisão'
                      '\n[5] - Potencia'
                      '\n[6] - Novos numeros'
                      '\n[7] - Sair'
                      '\nSelecione a operação: '))
    print('-' * 25)

    if conta not in [1, 2, 3, 4, 5, 6, 7]:
        print('Opção invalida! Tente novamente')

    if conta == 7:
        print('Finalizado')
        break

    elif conta == 1:
        soma = n1 + n2
        print(f'A soma é: {soma}')

    elif conta == 2:
        sub = n1 - n2
        print(f'A subtração é: {sub}')

    elif conta == 3:
        mult = n1 * n2
        print(f'A multiplicação é: {mult}')

    elif conta == 4:
        if n2 == 0:
            print('Divisão por Zero. Invalida')
        else:
            div = n1 / n2
            print(f'A Divisão é: {div:.2f}')

    elif conta == 5:
        poten = n1 ** n2
        print(f'A potenciação é: {poten}')

    elif conta == 6:
        while True:
            try:
                n1 = float(input('Digite o primeiro numero: '))
                n2 = float(input('Digite o segundo numero: '))
                break
            except ValueError:
                print('Não são permitidas letras ou caracteres especiais')
