# Variaveis livres + nonlocal
def fora(x):
    a = x

    def dentro():
        #print(locals())
        #print(dentro.__code__.co_freevars)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final  # nonlocal permite que uma função interna mude uma variavel livre do escopo externo
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar("a")
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)