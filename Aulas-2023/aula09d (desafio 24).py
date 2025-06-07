c = input('Digite o nome de uma cidade: ')
C = c.upper()
C = C.split()
s = 'SANTO' in C[0]
print(f'O nome da cidade começa com SANTO? {"Sim" if s else "Não"}')
