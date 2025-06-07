try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não foi possivel dividir por zero.')

except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados.')

except Exception as erro:
    print(f'Infelizmente tivemos um problema {erro.__cause__}')

else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre!')