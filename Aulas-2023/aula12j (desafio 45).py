import random
import time
jo = int(input('1 - Pedra\n'
               '2 - Papel\n'
               '3 - Tesoura\n'
               'Escolha um: '))
print('PROCESSANDO...')
pc = random.randint(1,3)
time.sleep(3)
if jo == 1 and pc == 2:
    print('Papel ganha de pedra. Você Perdeu!')
elif jo == 2 and pc == 3:
    print('Tesoura ganha de papel. Você Perdeu!')
elif jo == 3 and pc == 1:
    print('Pedra ganha de tesoura. Você Perdeu!')
elif jo == 1 and pc == 3:
    print('Pedra ganha de tesoura. Você Venceu!')
elif jo == 2 and pc == 1:
    print('Papel ganha de pedra. Você Venceu!')
elif jo == 3 and pc == 2:
    print('Tesoura ganha de papel. Você Venceu!')
elif jo == pc:
    print('Empate!')
else:
    print('Opção Invalida!')
