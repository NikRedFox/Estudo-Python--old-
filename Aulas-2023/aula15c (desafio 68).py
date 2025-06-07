import random
count = 0
v = 0
r = 0
while True:
    pc = random.randint(1,10)
    v = int(input('Diga um valor: '))
    p1 = str(input('Par ou Impar [P/I]: ')).upper()
    r = v + pc
    if (r % 2) != 0  and p1 == 'I' or (r % 2) == 0 and p1 == 'P':
        count += 1
    elif (r % 2) == 0 and p1 == 'I' or (r % 2) != 0 and p1 == 'P':
        print(f'Perdeu! \n'
              f'Vce jogou {v} e o Pc jogou {pc}. Total: {r} \n'
              f'Vitorias contra PC: {count}')
        break