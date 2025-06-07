#Desempacotamento em chamadas de metodos e funções

string = "ABCD"
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python', 'é', 'legal')

a, *_, ap, u = lista
print(a, u, ap)
print(*string)