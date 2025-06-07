temp = list()
par = list()
impar = list()
for p in range(0,7):
    temp.append(int(input(f'Digite o {p+1}° valor: ')))
    if temp[p] % 2 == 0:
        par.append(temp[p])
    if temp[p] % 2 != 0:
        impar.append(temp[p])
par.sort()
impar.sort()
print(f'Foram digitados os seguintes valores pares: {par}')
print(f'Foram digitados os seguintes valores impáres {impar}')

