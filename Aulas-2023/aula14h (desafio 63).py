n = int(input('Digite o numero de termos que quer ver: '))
f1 = 0
f2 = 1
termo = 0
count = 0
while count <= n-1:
    count += 1
    f1 = f2
    f2 = termo
    termo = f1 + f2
    print(termo)
