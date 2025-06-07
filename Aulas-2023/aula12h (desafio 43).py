a = float(input('Digite a altura em metros: '))
p = float(input('Digite o peso em kg: '))
imc = p / (a ** 2)
if imc < 18.5:
    print(f'IMC {imc}. ABAIXO DO PESO')
elif 18.5 < imc < 25:
    print(f'IMC {imc}. PESO IDEAL')
elif 25 < imc < 30:
    print(f'IMC {imc}. SOBREPESO')
elif 30 < imc < 40:
    print(f'IMC {imc}. OBESIDADE')
elif imc > 40:
    print(f'IMC {imc}. OBESIDADE MORBIDA')