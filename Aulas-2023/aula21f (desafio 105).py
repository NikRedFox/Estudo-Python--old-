def notas():
    alunos = list()
    while True:
        q_notas = int(input('Digite a quantidade de notas [0 para sair]: '))
        if q_notas == 0:
            break

        for num in range(q_notas):
            nome = str(input('Digite o nome: '))
            nota = float(input('Digite a nota: '))
            aluno = {'nome': nome, 'nota': nota}
            alunos.append(aluno)

        break

    return alunos


dados_alunos = notas()
print(dados_alunos)