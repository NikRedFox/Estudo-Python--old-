gen = str(input('Digite seu genero [M/F]: ')).upper()
while gen != 'M' and gen != 'F':
    print('Opção invalida, tente novamente!')
    gen = str(input('Digite seu genero [M/F]: ')).upper()
print('Fim')