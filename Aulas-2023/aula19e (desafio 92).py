import datetime
data = datetime.date.today()
ano = data.year
trabalho = dict()
trabalho["nome"] = str(input('Nome: '))
trabalho["nascimento"] = int(input('Ano de nascimento: '))
trabalho["ctps"] = int(input('Carteira de trabalho: '))

if trabalho["ctps"] != 0:
    trabalho["contrato"] = int(input('Ano de contratação: '))
    trabalho["salario"] = float(input('Salario: R$'))
    tempo_trabalho = 35 - (ano - trabalho["contrato"])
    trabalho["aposentar"] = tempo_trabalho + (ano - trabalho["nascimento"])

print()
print(f'Nome: {trabalho["nome"]}\n'
      f'Idade: {ano - trabalho["nascimento"]}\n'
      f'CTPS: {trabalho["ctps"]}\n')

if trabalho["ctps"] !=0:
    print(f'Ano de contratação: {trabalho["contrato"]}\n'
          f'Salario: R${trabalho["salario"]}\n'
          f'Aposentará com {trabalho["aposentar"]} anos')


