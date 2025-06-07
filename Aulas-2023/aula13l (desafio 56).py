count = 0
velho = 0
anos = 0
mvelho = 'Z'
for c in range(1,5):
    nome = str(input('Seu nome: '))
    idade = int(input('Sua idade: '))
    gen = str(input('Seu genero [M/F]: '))
    anos += idade
    if gen == 'F' and idade < 20:
        count += 1
    if c == 1 and gen == 'M':
        velho = idade
        mvelho = nome
    if gen == 'M' and idade > velho:
        velho = idade
        mvelho = nome

print(f'A media de idade é: {anos / 4:.2f}\n'
      f'O homem mais velho é {mvelho} e tem {velho} anos\n'
      f'{count} mulher(es) tem mais de 20 anos')
