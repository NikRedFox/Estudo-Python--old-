nome = 'Luiz Gustavo'
contador = 0
while contador <= len(nome):
    if contador == len(nome):
        print('*', end='')
        break

    print('*', end='')
    print(nome[contador], end='')
    contador += 1
