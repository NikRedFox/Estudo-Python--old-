import os

lista_compras = []
while True:
    os.system('cls')
    escolha = int(input('------------OPÇÕES------------\n'
                        '\n[1] - Inserir itens\n'
                        '[2] - Apagar um item da lista\n'
                        '[3] - Mostrar lista\n'
                        '[4] - Encerrar programa\n'
                        '\nSelecione uma opção: '))
    if escolha == 1:
        while True:
            itens_lista = str(input('Insira um item ["Fim" para sair]: ')).strip().upper()
            if itens_lista == 'FIM':
                break
            lista_compras.append(itens_lista)

    elif escolha == 2:
        if len(lista_compras) == 0:
            print('-' * 31)
            print('\nA lista ainda está vazia')
        else:
            print('Itens na lista:')
            for indice, nome in enumerate(lista_compras):
                print('\t', indice, nome)

            apagar = int(input('\nDigite o indice que deseja apagar: '))

            if 0 <= apagar < len(lista_compras):
                del lista_compras[apagar]
                print('-' * 31)
                print('Item removido com sucesso.')
            else:
                print('O indice esta fora dos limites da lista.')

    elif escolha == 3:
        if not lista_compras:
            print('-' * 31)
            print('A lista ainda está vazia')
        else:
            print('Lista de compras:')
            for indice, nome in enumerate(lista_compras):
                print('\t', indice, nome)

    elif escolha == 4:
        print('-' * 31)
        print('PROGRAMA ENCERRADO. BOAS COMPRAS\n')
        break

    else:
        print('Opção invalida!')

print(lista_compras)