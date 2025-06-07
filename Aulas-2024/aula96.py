# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# import sys
# print(sys.platform)
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes


# partes - from nome_modulo import objeto1, objeto2
# from sys import exit, platform
# print(platform)
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo


# alias 1 - import nome_modulo as apelido
# import sys as s
# s = 'Algo'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf
# print(pf)
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem


# má prática - from nome_modulo import *
# from sys import *
# print(platform)
# exit()
# Vantagens: importa tudo de um modulo
# Desvantagens: importa tudo de um modulo