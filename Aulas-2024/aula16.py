# if / elif / else
entrada = input('Voce quer "entrar" ou "sair"? [S/N]').upper()

if entrada == "S":
    print('Voce entrou!')

elif entrada == "N":
    print('Voce saiu!')

else:
    print('Resposta invalida')