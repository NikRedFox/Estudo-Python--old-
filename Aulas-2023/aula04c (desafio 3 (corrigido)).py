cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'peb': '\033[7;30m'}
print ('=== Desafio 3 ===')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
n3 = n1 + n2
print (f'A soma é: {cores["azul"]}{n3}')
