maior = 0
menor = 0
valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1.isalpha() or valor2.isalpha():
    print('Voce digitou uma letra!')

else:
    valor1 = int(valor1)
    valor2 = int(valor2)
    if valor1 > valor2:
        maior = valor1
        menor = valor2
        print(f'{maior} é maior que {menor}')

    elif valor1 < valor2:
        maior = valor2
        menor = valor1
        print(f'{maior} é maior que {menor}')

    else:
        print('Os valores são iguais')

