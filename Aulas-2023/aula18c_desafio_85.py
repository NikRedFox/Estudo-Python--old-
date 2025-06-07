temp = list()
par = list()
impar = list()
for p in range(0,3):
    temp.append(int(input('Digite um valor: ')))
    test = temp[p] % 2
    
    if test == 0:
        par.append(temp[p])
    if test != 0:
        impar.append(temp[p])

print(par)
print(impar)

