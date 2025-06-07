def descoberta():
    for lista in lista_de_listas:
        digitos_encontrados = set()
        count = 0
        for digito in lista:
            if digito in digitos_encontrados:
                count += 1
                print(f'O primeiro digito repetido é {digito}')
                break
            else:
                digitos_encontrados.add(digito)

        if count == 0:
            print(-1)


lista_de_listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    # Sem repetição
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],     # 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],     # 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],     # 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],    # 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],     # 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  # 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],     # 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],    # 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],     # 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],     # 5
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],    # Sem repetição
]

descoberta()