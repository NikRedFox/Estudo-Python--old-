grupo = list()
grupo_f = list()
grupo_m = list()
count = 0
soma = 0
r = "s"
while r != 'n':
    pessoa = dict()
    pessoa["nome"] = str(input('Nome: '))
    pessoa["sexo"] = str(input('Sexo [F/M] ')).lower()
    pessoa["idade"] = int(input('Idade: '))

    grupo.append(pessoa.copy())
    if pessoa["sexo"] == "f":
        grupo_f.append(pessoa.copy())
    count += 1
    r = str(input('Deseja adicionar outra pessoa? [S/N] ').lower())

for pessoa in grupo:
    soma += pessoa["idade"]

if len(grupo) != 0:
    media = soma / len(grupo)

for pessoa in grupo:
    if pessoa["idade"] > media:
        grupo_m.append(pessoa.copy())

print(grupo)
print(f'O grupo tem {count} pessoas.')
print(f'A media de idade é de {media} anos.')
print(f'As mulheres cadastradas foram:')
for pessoa in grupo_f:
    print(f'Nome: {pessoa["nome"]}, ')
print()
print(f'Lista das pessoas que estão acima da média:')
for pessoa in grupo_m:
    print(f'Nome = {pessoa["nome"]}, Sexo = {pessoa["sexo"]}, Idade = {pessoa["idade"]}')


