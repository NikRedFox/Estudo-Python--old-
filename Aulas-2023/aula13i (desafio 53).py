frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = frase.replace(' ', '')
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
#metodo sem for
#string = str(input('Frase: '))
#stringSemEspacos = string.replace(' ', '')
#stringTodaMinuscula = stringSemEspacos.lower()
#stringInvertida = stringTodaMinuscula[::-1]
#if stringInvertida == stringTodaMinuscula:
#    print("SIM")
#else:
#    print("NAO")