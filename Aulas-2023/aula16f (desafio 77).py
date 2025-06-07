tupla = ('porra', 'desgraça', 'miseria', 'caralho', 'maldiçao', 'puta merda')

for v in tupla:
    print(f'\nNa palavra {v} temos:')
    for letra in v:
        if letra in 'aeiouAEIOU':
           print(letra, end = ' ')
