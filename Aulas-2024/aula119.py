# Problema dos parametros mutaveis em funções Python
def adiciona_clientes(nome, lista=None):  # Sempre verificar se os parametros são mutaveis.
    if lista is None:                     # Se for mutavel, nao colocar valor padrão        
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')


cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

print(cliente1)
print(cliente2)