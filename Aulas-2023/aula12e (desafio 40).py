n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Media {m}. REPROVADO.')
elif m > 5  and m < 6.9:
    print(f'Media {m}. RECUPERAÇÃO.')
else:
    print(f'Media {m}. APROVADO.')