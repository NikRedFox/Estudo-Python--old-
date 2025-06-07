cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'peb': '\033[7;30m'}
print ('=== Desafio 2 ===')
nome = input ('Qual seu nome?')
dia = input ('Em que dia nasceu?')
mes = input ('Em que mês nasceu?')
ano = input ('De qual ano?')
print (f'{cores["azul"]}Olá', nome, '!', 'Você nasceu no dia', dia, "de", mes, "de", ano, '.', f'Correto?{cores["limpa"]}')
