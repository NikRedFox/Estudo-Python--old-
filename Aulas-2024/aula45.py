"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entrege o proximo valor
iter -> me entregue seu iterador
"""

texto = 'Nikolas' #iteravel
iterador = iter(texto) #iterador

#while True:
#    try:
#        letra = next(iterador)
#        print(letra)
#    except StopIteration:
#        break
# Esse é o processo feito pelo for abaixo no passo a passo

for letra in texto:
    print(letra)