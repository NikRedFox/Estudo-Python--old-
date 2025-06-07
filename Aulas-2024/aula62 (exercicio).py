"""
Calculo do segundo digito do CPF
"""
import sys
cpf_formatado = "437.926.238-38"
cpf_sem_formatacao = ''.join(filter(str.isdigit, cpf_formatado))
contador_regressivo_1 = 10
resultado_digito_1 = 0
contador_regressivo_2 = 11
resultado_digito_2 = 0

entrada_sequencial = cpf_formatado == cpf_formatado[0] * len(cpf_formatado)
if entrada_sequencial:
    print('Você enviou dados sequenciais invalidos.')
    sys.exit()

if len(cpf_sem_formatacao) == 11:
    cpf_int = int(cpf_sem_formatacao)
    cpf_list = [int(digito) for digito in str(cpf_int)]

    for digito_1 in cpf_list[:9]:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    if cpf_sem_formatacao[-2] == str(digito_1):
        print(f'O primeiro dígito do CPF é válido: {digito_1}')
    else:
        print('CPF invalido')

    for digito_2 in cpf_list[:10]:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    if cpf_sem_formatacao[-1] == str(digito_2):
        print(f'O segundo digito do CPF é valido: {digito_2}')
    else:
        print('CPF invalido')
else:
    print(f'CPF inválido devido ao comprimento incorreto.')
