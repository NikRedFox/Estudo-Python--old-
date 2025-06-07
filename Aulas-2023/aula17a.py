#num = [5, 2, 5, 1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 0)
#num.pop(1)
#if 4 in num:
#    num.remove(4)
#else:
#    print('Não existe na lista')
#print(num)
#print(f'Essa lista tem {len(num)} elementos')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
b = valores[:]
b[2] = 8

#for cont in range(0, 5):
    #valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print(valores)
print(b)
print('Fim da lista')