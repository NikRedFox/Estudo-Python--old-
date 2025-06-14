import random
contador_regressivo_1 = 10
resultado_digito_1 = 0
contador_regressivo_2 = 11
resultado_digito_2 = 0
cpf_list = [random.randint(0, 9) for _ in range(9)]

for digito_1 in cpf_list[:9]:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

for digito_2 in cpf_list[:10]:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_list.append(digito_1)
cpf_list.append(digito_2)

cpf = ''.join(map(str, cpf_list))
print(cpf)