#n = input('Digite algo: ')
#if n.isnumeric():
#    print(f"{n} é um numero.")

#else:
#    print(f'{n} é uma letra.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a seunda nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print(f'{m} Nota passavel')
else:
    print(f'{m} Nota insuficiente')