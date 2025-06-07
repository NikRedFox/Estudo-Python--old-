def escreva(txt):
    tam = len(txt) + 2
    print('~' * tam)
    print(txt)
    print('~' * tam)


r = 's'
while r != 'n':
    txt = str(input('Digite algo: '))
    escreva(f'  {txt}')
    r = str(input('Deseja continuar? [S/N] ')).lower()