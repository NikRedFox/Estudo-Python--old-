def area(a, b):
    print(f'A largura é {a} e o comprimento é {b}')
    area = a * b
    print(f'Sua área é {area} metros quadrados.')


a = float(input('Digite a Largura (m): '))
b = float(input('Digite o comprimento (m): '))
area(a, b)