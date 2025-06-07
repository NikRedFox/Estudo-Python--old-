# dir, hasattr e getattr em Python (dir é usado no console de debug)
string = 'Nikolas'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
    #print(string.upper())

else:
    print('Não existe o metodo', metodo)