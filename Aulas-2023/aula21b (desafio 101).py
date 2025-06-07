def voto(idade):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    if 18 <= idade < 70:
        return f"Com {idade} anos voce é obrigado a votar"
    if idade < 16:
        return f"Com {idade} anos você não é elegivel para votar"
    if (16 <= idade < 18) or idade >= 70:
        return f"Com {idade} anos seu voto é opcional"


ano_nasc = int(input('Digite o ano em que voce nasceu: '))
print(voto(ano_nasc))