"""
    Flag - Marcar um local
    None = Não-valor
    is e is not = (tipo, valor, identidade)
    id = Identidade
"""
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
print('-' * 30)

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça nada')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')