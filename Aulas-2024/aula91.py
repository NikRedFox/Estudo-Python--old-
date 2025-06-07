# Introdução às Generator functions em Python
# generator = (n for n in range(100000)


def generator(n=0):
    yield 1  # Pausa
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Mais uma...')
    return 'Acabou'


def generator2(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator(n=0)
for n in gen:
    print(n)

gen2 = generator2(maximum=100000)
for n in gen2:
    print(n)


