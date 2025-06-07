p = float(input("Informe o preço: R$"))
d = float(0.05)
c = float(p * d)
pf = float(p - c)
print(f'O produto custa: R${p} \nPreço final: R${pf}')

# pf = p - (p * 5 / 100) também funcionaria