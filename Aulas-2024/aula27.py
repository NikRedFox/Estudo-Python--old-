"""
Fatiamento de strings
    012345678
    Ola Mundo
   -987654321
   Fatiamento [i:f:p] [::]
   Obs: A função len retorna a qtd de caracteres da str
"""

variavel = 'Ola mundo'
print(variavel[5])
print(variavel[4:])
print(variavel[:5])
print(variavel[-8:-2])
print(len(variavel))
print(variavel[0:len(variavel):2])
print(variavel[-1:-10:-1])