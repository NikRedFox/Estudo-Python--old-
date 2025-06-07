termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (11 -1) * razao
for c in range(termo, decimo, razao):
    print(f'{c}')