termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = termo + (10 -1) * razao
while termo <= decimo:
    termo += razao
    print(termo)
    if termo > decimo:
        r = int(input('Quantos termos a mais quer mostrar? [0 pra sair]: '))
        decimo = termo + (r -1) * razao
print('Fim')
