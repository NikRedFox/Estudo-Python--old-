aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = int(input(f'Media do {aluno["nome"]}: '))

if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

print(f'Nome = {aluno["nome"]}')
print(f'Media = {aluno["media"]}')
print(f'Situação = {aluno["situacao"]}')

