n = input('Digite um nome completo: ')
s = n.split()
print(f'Nome: {n} \nPrimeiro nome: {s[0]} \nUltimo nome: {s[len(s)-1]}')