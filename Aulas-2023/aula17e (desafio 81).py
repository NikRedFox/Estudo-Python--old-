valores = []
r = 's'
count = 0
while r != 'n':
    valores.append(int(input('Digite um valor: ')))
    count += 1
    r = str(input('Deseja continuar? [S/N] ')).lower()
valores.sort(reverse=True)
if 5 in valores:
    print('O numero 5 está na lista')
else:
    print('O numero 5 não está na lista')
print(f'Foram digitados {count} numeros na lista')
print(valores)
