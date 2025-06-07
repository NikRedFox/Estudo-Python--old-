count = 0
man = 0
fem = 0
while True:
    age = int(input('Idade: '))
    gen = ' '
    while gen not in 'MF':
        gen = str(input('Genero [M/F]: ')).upper()
    con = ' '
    while con not in 'SN':
        con = str(input('Deseja continuar? [S/N]: ')).upper()
    if age > 18:
        count += 1
    if gen == 'M':
        man += 1
    if gen == 'F' and age < 20:
        fem += 1
    if con != 'S':
        break
print(f'{count} pessoas tem mais de 18 anos \n'
      f'{man} homens foram cadastrados \n'
      f'{fem} mulheres cadastradas tem menos de 20 anos')