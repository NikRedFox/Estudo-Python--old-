"""
Dicionarios em Python (tipo dict)
Dicionarios são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o "indice" que vimos na lista e podem ser de tipos imutaveis como:
str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionario.
Usamos as chaves {} ou a classe dict para criar dicionarios.
Imutaives: str, int, float, bool, tuple
Mutaveis: dict, list
"""
pessoa = {
    'nome': 'Nikolas',
    'sobrenome': 'Barbosa',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'X', 'numero': 123},
        {'rua': 'Y', 'numero': 456},
    ]
}

print(pessoa, type(pessoa))
print(pessoa['nome'])