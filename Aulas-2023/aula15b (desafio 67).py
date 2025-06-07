r = 0
while True:
    n = int(input('Digite a tabuada desejada: '))
    if n < 0:
        break
    for i in range(10):
        r = n * (i+1)
        print(f'{n} X {i+1} = {r}')
