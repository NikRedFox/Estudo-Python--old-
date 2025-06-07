n = input('Digite algo: ')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'peb': '\033[7;30m'}
print(f'Ola, {cores["azul"]}{n}{cores["limpa"]}')