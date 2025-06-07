r = 's'

while r !='n':
    numeros = list()
    soma = 0

    num = int(input('Quantos numeros quer digitar? '))
    for n in range(num):
        num_s = int(input(f'Digite o numero {n+1}: '))
        numeros.append(num_s)
        soma += num_s
    media = soma / num

    r = str(input('Deseja continuar? [S/N] ')).lower()
print(media)