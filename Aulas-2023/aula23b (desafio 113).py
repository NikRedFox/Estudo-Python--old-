def leiaInt(msg):
    while True:
        try:
            numero1 = int(input(msg))
            return numero1
        except KeyboardInterrupt:
            print('\033[0;31mO usuario preferiu não digitar esse numero.\033[m')
            return 0
        except ValueError:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')


def leiaFloat(msg):
    while True:
        try:
            numero2 = float(input(msg))
            return numero2
        except KeyboardInterrupt:
            print('\033[0;31mO usuario preferiu não digitar esse numero.\033[m')
            return 0.0
        except ValueError:
            print('\033[0;31mErro! Digite um numero real valido.\033[m')


n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um numero real: ')
print(f'O numero inteiro digitado foi {n} e o real foi {m}')

