# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - uteils p/ dividir problemas grandes em partes menores
# Toda funções recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

# import sys
# sys.setrecursionlimit(1004)
# Isso aumenta o limite de segurança de call stack do programa (PERIGOSO MEXER NISSO)
def recursiva(inicio=0, fim=10):
    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao fim
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())
print()


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f'Fatorial: {factorial(5)}')