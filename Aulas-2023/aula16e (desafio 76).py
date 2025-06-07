tupla = ('Pão', '1.00', 'Cafézinho', '2.00', 'Coxinha', '1.50')
#print(f'{tupla[0]}: R${tupla[1]}\n'
      #f'{tupla[2]}: R${tupla[3]}\n'
      #f'{tupla[4]}: R${tupla[5]}')
print(f'{tupla[0]}' + "." * (20 - len(tupla[0])) + f'R${tupla[1]}\n'
      f'{tupla[2]}' + "." * (20 - len(tupla[2])) + f'R${tupla[3]}\n'
      f'{tupla[4]}' + "." * (20 - len(tupla[4])) + f'R${tupla[5]}\n')
