contador = 0

while contador <= 20:
    contador += 1
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if 10 <= contador <= 17:
        print('Não vou mostrar esse numero.')
        continue

    print(contador)

    if contador == 20:
        break

print('Acabou')