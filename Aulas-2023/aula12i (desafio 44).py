p = float(input('Digite o valor do produto: R$'))
pg = int(input('1 - Cartão de debito / credito\n'
               '2 - Dinheiro\n'
               '3 - Cheque\n'
               'Selecione a opção de pagamento: '))
if pg == 1:
   car = int(input('4 - Parcelar em 2x\n'
         '5 - Parcelar em 3x ou mais\n'
         '6 - À vista\n'
         'Selecione a opção:  '))
   if car == 4:
       print(f'O pagamento será feito em duas parcelas de R${p / 2:.2f}')
   elif car == 5:
       ju = int(input('Informe o numero de parcelas: '))
       print(f'O pagamento será feito em {ju} parcelas de R${p / ju:.2f}')
   elif car == 6:
       print(f'O pagamento à vista é de R${p:.2f}')
   else:
       print('Opção Invalida.')

elif pg == 2 or pg == 3:
    print(f'A opção vem com 10% de desconto.\n'
          f'Valor final: R${p - (p*0.10):.2f}')