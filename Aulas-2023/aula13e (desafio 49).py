n = int(input('Escolha uma tabuada: '))
r = 0
for i in range(10):
    r = n * (i + 1)
    print(f'{n} X {i+1} = {r}')