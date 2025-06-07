valores= []
r = 's'
while r != 'n':
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado. Não adicionado.')
    r = input('Quer continuar? [S/N] ').lower()

valores.sort()
print(valores)