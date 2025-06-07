import os
import json
import platform


def abrir(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        return dados
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def listar(lista):
    if len(lista) <= 0:
        print('Não há nada para listar')
        return

    print('\nTAREFAS:')
    for i in lista:
        print("\t-" + i)


def desfazer(lista, lista_d):
    if len(lista) <= 0:
        print('Não há nada para desfazer')
        return

    ultimo = lista.pop()
    print(f'\nTarefa "{ultimo}" removida da lista')
    lista_d.append(ultimo)


def refazer(lista, lista_d):
    if len(lista_d) <= 0:
        print('Não há nada para refazer')
        return
    refaz = lista_d.pop()
    print(f'\nTarefa "{refaz}" restaurada a lista')
    lista.append(refaz)


def adicionar(lista, entrada):
    print(f'{entrada=} adicionada na lista')
    lista.append(entrada)
    print()


lista = []
lista_d = []
while True:
    entrada = str(input('\nComandos: listar, desfazer, refazer, clear e sair\nDigite uma tarefa ou comando: ')).lower()

    # comandos = {   # versão com guard clause
    #     'listar': lambda: listar(lista),
    #     'desfazer': lambda: desfazer(lista, lista_d),
    #     'refazer': lambda: refazer(lista, lista_d),
    #     'clear': lambda: os.system('clear'),
    #     'adicionar': lambda: adicionar(lista, lista),
    #}
    # comando = comandos.get(lista) if comandos.get(lista) is not None else \
    #     comandos['adicionar']
    # comando()

    if entrada == 'listar':
        listar(lista)


    elif entrada == 'desfazer':
        desfazer(lista, lista_d)

    elif entrada == 'refazer':
        refazer(lista, lista_d)

    elif entrada == 'clear':
        clear_screen()

    elif entrada == 'sair':
        nome_arquivo = "lista_de_tarefas.json"
        with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
            json.dump(lista, arquivo, indent=2, ensure_ascii=False)
            print(f'Arquivo {nome_arquivo} salvo com sucesso.')
        print('\nOperação concluida')
        break

    else:
        lista.append(entrada)

