cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'peb': '\033[7;30m'}
print ('=== Desafio 1 ===')
nome = input ('Qual seu nome?')
print (f'{cores["amarelo"]}Seja bem vindo!', nome, f', tenha um bom dia!{cores["limpa"]}')
