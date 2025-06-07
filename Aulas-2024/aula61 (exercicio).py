"""
Calculo do primeiro digito do CPF
"""
cpf_formatado = "437.926.238-38"
cpf_sem_formatacao = ''.join(filter(str.isdigit, cpf_formatado))
contador_regressivo_1 = 10
resultado_digito_1 = 0

if len(cpf_sem_formatacao) == 11:
    cpf_int = int(cpf_sem_formatacao)
    cpf_list = [int(digito) for digito in str(cpf_int)]

    nove_digitos = cpf_list[:9]

    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    if cpf_sem_formatacao[-2] == str(digito_1):
        print(f'O primeiro dígito do CPF é válido: {digito_1}')
    else:
        print('CPF invalido')
else:
    print(f'CPF inválido devido ao comprimento incorreto.')


#cpf = '74682489070'
#nove_digitos = cpf[:9]
#contador_regressivo_1 = 10

#resultador_digito_1 = 0
#for digito_1 in nove_digitos:
#    resultador_digito_1 += int(digito_1) * contador_regressivo_1
#    contador_regressivo_1 -= 1
#digito_1 = (resultador_digito_1 * 10) % 11
#digito_1 = digito_1 if digito_1 <= 9 else 0
#print(digito_1)








