import time
def contador(inicio, fim, passo):
    if passo < 0:
        print('Numero negativo detectado!')
        time.sleep(0.5)
        passo *= -1
    if passo == 0:
        print('O valor do passo não pode ser zero.')
        return

    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}: ')
    if inicio <= fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
            time.sleep(0.3)
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
            time.sleep(0.3)
        print()

contador(1, 10, 1)
contador(10, 0, 2)
print()
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)

