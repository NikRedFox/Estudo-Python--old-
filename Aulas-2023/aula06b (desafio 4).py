cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'peb': '\033[7;30m'}
n = input('Digite algo: ')
print(type(n), '\nÉ um número? {} \n' 'É uma letra? {} \n''É maiusculo? {} \n' 'É minusculo? {} \n'.format(n .isdigit(),
n .isalpha(), n .isupper(), n .islower()))