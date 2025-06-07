cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pc = 0
while True:
    pc = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= pc <= 20:
       break
    print('Erro. Tente novamente.')
print(f'Voce digitou o numero {cont[pc]}')