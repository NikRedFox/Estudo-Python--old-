"""
Sets - Conjuntos em Python (tipo set)
Conjunto são ensinados na matematica
Representados graficamente pelo diagrama de Venn
Sets em Python são mutaveis, porem aceitam apenas tipos imutaveis como valor

Criando um set
set(iteravel) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados de iteraveis
- Eles não tem indexes;
- Eles não garantem ordem;
- Eles são iteraveis (for, in, not in)

Metodos uteis
add, update, clear, discard

Operadores uteis
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simetrica ^ - itens que não estão em ambos
"""
s0 = set()  # Set vazio
s1 = {1, 2, 3}  # Set com dados
print(s1)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]  # Uma lista transformada em um set para remoção de numeros repetidos
s2 = set(l1)                   # e depois novamente transformada em uma lista
l2 = list(s2)
print(l2)

print(3 in s1)  # Um metodo para procurar algo dentro de um set ja que não tem indexes
print()

s0.add('Nikolas')
s0.add(1)  # Adiciona uma coisa por vez
s0.update(('Ola mundo', 1, 2, 3, 4))  # Adiciona varias coisas por vez
print(s0)
s0.clear()  # Limpa o set inteiro
print(s0)
s0.update(('Funciona', 'Agora'))
print(s0)
s0.discard('Agora')  # Limpa algo especifico do set
print(s0)
print()

s3 = {1, 2, 3}
s4 = {2, 3, 4}
s5 = s3 | s4  # União de 2 sets em um
s6 = s3 & s4  # Intersecção dos sets, mostrando apenas o que aparece em ambos
s7 = s3 - s4  # Mostra apenas o que for diferente no set da esquerda (a ordem importa)
s8 = s3 ^ s4  # Mostra o que for diferente entre os dois sets (a ordem não importa)
print(s5)
print(s6)
print(s7)
print(s8)