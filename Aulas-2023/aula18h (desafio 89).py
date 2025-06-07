c = 's'
alunos = []
count = -1
while c != 'n':
    temp = []
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append(temp)
    c = str(input('Deseja continuar? [S/N] ')).lower()

for aluno in alunos:
    count += 1
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (nota1 + nota2) / 2
    print(f'{count}  Nome: {nome}      Media: {media}\n')

a = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe) '))
while a != 999:
    if a >= 0 and a < len(alunos):
        aluno = alunos[a]
        nome = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        print(f'Nome: {nome}\n'
              f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n')
       
    else:
        print('Aluno não encontrado\n')
    a = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe) '))