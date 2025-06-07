import random
count = 0
pc = random.randint(1,5)
p = int(input('Qual numero entre 1 e 5 foi escolhido? '))
while p != pc:
    print('Resposta errada! Tente novamente')
    count += 1
    p = int(input('Qual numero entre 1 e 5 foi escolhido? '))
print(f'Resposta certa \nErros: {count}')