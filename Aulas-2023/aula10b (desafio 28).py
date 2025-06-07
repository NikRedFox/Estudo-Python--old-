import random
n = [1, 2, 3, 4, 5]
a = random.choice(n)
print('Qual numero entre 1 a 5 foi escolhido?')
r = int(input('Digite a resposta: '))
if r == a:
    print('Resposta correta!')
else:
    print(('Resposta errada!'))