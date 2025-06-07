"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)


#def soma(x, y):
#    return x + y


def soma(*args): #*args empacota o que foi enviado para a função dentro de uma tupla
    total = 0
    for numero in args:
        #print(f'Total = {total} + {numero}')
        total = total + numero
        #print(f'Total = {total}')
    return total


soma6 = soma(1, 2, 3, 4, 5, 6)
print(soma6)

soma123 = soma(1, 2, 3)
print(soma123)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) #aqui ele desempacota a tupla para enviar como parametros para a função
print(outra_soma)

print(sum(numeros))