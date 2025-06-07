n1 = 0
n2 = 0
count = 0
while True:
    n1 = int(input('Digite um numero: '))
    count += 1
    if n1 == 999:
        break
    n2 += n1
print(f'Foram digitados {count - 1} numeros \n'
      f'A soma entre eles é {n2}')