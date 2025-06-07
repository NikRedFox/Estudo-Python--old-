palavra_secreta = 'abacate'
letras_certas = ''
contador = 0

while True:
    contador += 1
    letra_digitada = input('\nDigite uma letra:')

    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada

    palavra_formada = ''

    for letras_secretas in palavra_secreta:
        if letras_secretas in letras_certas:
            palavra_formada += letras_secretas
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_secreta == palavra_formada:
        break


print('-' * 30)
print(f'Foram feitas {contador} tentativas')
print('-' * 30)
