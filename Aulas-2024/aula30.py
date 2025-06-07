"""
    Constante = "Variaveis" que não vão mudar
    Muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim)

"""
velocidade = 61          # velocidade atual do carro
local_carro = 101        # local em que o carro está na estrada

RADAR_1 = 60             # velocidade maxima do radar 1
LOCAL_1 = 100            # local onde o radar 1 está
RADAR_RANGE = 1          # a distancia onde o radar pega

vel_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and vel_carro_passou_radar1

if vel_carro_passou_radar1:
    print('Velocidade do carro ultrapassou do limite do radar')

if carro_passou_radar1:
    print('Carro passou pelo radar')