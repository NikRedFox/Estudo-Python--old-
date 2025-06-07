perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
for pergunta in perguntas:
    opcoes = pergunta['Opções']
    print(f"Pergunta: {pergunta['Pergunta']}")
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")

    #resposta = opcoes[int(input('Resposta (Digite a opção): '))]
    #if resposta == pergunta['Resposta']:
    #    print('Resposta correta!\n')
    #else:
    #    print('Resposta incorreta!\n')

    # Versão com tratamento de erros
    try:
        resposta_usuario = int(input('Resposta (Digite o número da opção): '))
    except ValueError:
        print('Por favor, insira um número válido como resposta.')
        continue

    if 0 <= resposta_usuario < len(opcoes):
        resposta = opcoes[resposta_usuario]
        if resposta == pergunta['Resposta']:
            acertos += 1
            print('Resposta correta!\n')
        else:
            print('Resposta incorreta!\n')
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.\n')

print(f'Você acertou {acertos} de 3 perguntas!')