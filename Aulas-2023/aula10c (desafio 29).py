v = float(input("Digite a velocidade do veiculo: "))
if v >= 80:
    vel = float(v - 80)
    m = float(vel * 7.00)
    print(f'Por estar a {v}Km/h você será multado em R${m}!')
else:
    print('Não elegivel para multa.')