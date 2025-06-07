"""
pessoa = {
    'nome': ' Nikolas',
    'sobrenome': 'Barbosa',
    'enderecos': [{'rua': 'R1', 'numero': 32}, {'rua': 'R2', 'numero': 55}],
    'altura': 1.7,
    'numeros_escolhidos': (2, 5, 6, 42),
    'dev': False,
    'nada': None,
}"""
import json

#with open('aula118.json', 'w') as arquivo:
#    json.dump(pessoa, arquivo, indent=2)

with open('aula118.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))

