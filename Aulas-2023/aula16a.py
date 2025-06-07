lanche = ('hamburger', 'suco', 'pizza', 'pudim')
#for cont in range(0, len(lanche)):
 #   print(f'Eu vou comer {lanche[cont]}')

for cont in lanche:
    print(f'Eu vou comer {cont}')

for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont} na posição {pos}')

print('To cheio')
#Tuplas são imutaveis