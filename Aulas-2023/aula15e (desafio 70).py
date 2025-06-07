i1 = 0
count = 0
n1 = 0
barato = ' '
while True:
    item = str(input('Nome do item: '))
    custo = float(input('Preço do item: '))
    i1 += custo
    con = ' '
    while con not in 'SN':
        con = str(input('Deseja continuar? [S/N] ')).upper()
    if custo > 1000:
        count += 1
    if count == 1:
        barato = item
        n1 = custo
    if custo < n1:
        barato = item
        n1 = custo
    if con == 'N':
        break
print(f'Total gasto: R${i1} \n'
      f'Itens acima de R$1000: {count} \n'
      f'Item mais barato: {barato} ')