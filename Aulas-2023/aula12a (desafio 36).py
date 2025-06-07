vc = float(input('O valor da casa a ser adquirida: R$'))
s = float(input("Informe seu salario: R$"))
p = float(input('Em quantos anos pretende pagar? '))
m = vc / (p * 12)
ex = s * 0.3
if ex > m:
    print(f'Emprestimo aprovado! \nA prestação de R${m:.2f} não excede 30% do salario (R${ex:.2f})')
else:
    print(f'Emprestimo negado! \nA prestação de R${m:.2f} excede 30% do salario (R${ex:.2f})')