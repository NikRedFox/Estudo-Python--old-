termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
while termo <= decimo:
    termo += razao
    print(termo)
    
