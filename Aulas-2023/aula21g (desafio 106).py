def mensagen(msg):
    print('\033[34m-\033[0m' * 45)
def halp():
    from time import sleep
    while True:
        mensagen('Manual')
        ajuda = input('\033[32m  Função ou Biblioteca: [N para sair] \033[0m').lower()
        mensagen('Manual')
        if ajuda == 'n':
            print('\33[32m  Até logo!\033[0m')
            break

        print(f'  \033[33mAcessando o manual do comando {ajuda}\033[0m')
        mensagen('Manual')
        sleep(1)
        help(ajuda)
    return ajuda


halp()