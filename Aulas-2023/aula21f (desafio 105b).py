def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param n: uma ou mais notas do aluno.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação do aluno.
    """
    notas_dict = dict()
    notas_dict['Total'] = len(n)
    notas_dict['Maior nota'] = max(n)
    notas_dict['Menor nota'] = min(n)
    notas_dict['Media'] = sum(n) / len(n)
    if sit:
        situacao = ''
        if notas_dict['Media'] >= 7:
            situacao = 'Aprovado'
        elif notas_dict['Media'] >= 5:
            situacao = 'Razoavel'
        else:
            situacao = 'Reprovado'

        notas_dict['Situação'] = situacao

    return notas_dict


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)