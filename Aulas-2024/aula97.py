"""
Entendendo os seus proprios modulos Python
O primeiro modulo executado se chama __main__
Voce pode importar outro modulo inteiro ou partes do modulo
O python conhece a pasta onde o __main__ está e as pastas
abaixo dele
Ele não reconhece pastas e modulos acima do __main__ por
padrão
O Python conhece todos os modulos e pacotes presentes
nos caminhos de sys.path
"""
import sys

import aula97_m
from aula97_m import soma, variavel_modulo

print('Este modulo se chama', __name__)
print(*sys.path, sep='\n')

print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))