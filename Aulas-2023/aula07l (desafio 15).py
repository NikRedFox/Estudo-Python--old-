print('---Alguel de carros---')
d = int(input('Por quantos dias foi alugado? '))
km = float(input('Quantos Km rodados? '))
p1 = float(d * 60)
p2 = float(km * 0.15)
t = float(p1 + p2)
print(f'Preço por dia: R$60 \nPreço por Km rodado: R$0.15 \n'
      f'O carro foi alugado por {d} dias, e, percorreu {km} Km \n'
      f'R${p1} pelo tempo + R${p2} por Km percorrido \nTotal: R${t}')