km = float(input('Digite a distancia em Km da viagem: '))
if km >= 201:
    p = (km * 0.45)
    print(f'Para sua viagem de {km}Km, sua passagem fica R${p}.')
else:
    p = (km * 0.50)
    print(f'Para sua viagem de {km}, sua passagem fica R${p}')