# try, except, else e finally
try:
    print('Abrir Arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por Zero')
else:
    print('Não deu certo')

finally:
    print('Fechar Arquivo')