frase = 'O python é uma linguagem' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'
i = 0
apareceu_mais = 0
letra = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes = frase.count(letra_atual)

    if apareceu_mais < quantas_vezes:
        apareceu_mais = quantas_vezes
        letra = letra_atual

    print(letra_atual, quantas_vezes)
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra.upper()}", que apareceu {apareceu_mais}')