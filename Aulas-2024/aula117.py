"""
Criando arquivos com Python
Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
Modos:
r (leitura), w (escrita), x (para criação), a (escreve ao final), b (binario), t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)

Metodos uteis:
write, read (escrever e ler)
writelines (escrever varias linhas)
seek (move o crusor)
readline (ler linha)
readlines (ler linhas

Vamos falar mais sobre o medulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o modulo json, mas:
json.dump - Gera um arquivo json
json.load
"""
import os
caminho1 = 'aula117.txt'  # sem espeficicar o caminho inteiro, ele vai abrir o arquivo na mesma pasta do projeto

caminho2 = 'D:\\Python\\Aula_Python\\'  # no windows é preciso colocar duas "\" para ele pegar o caminho
caminho2 += 'aula117.txt'

# arquivo = open(caminho2, 'w')
#
# arquivo.close()

with open(caminho2, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Olá mundo\n')
    print('O arquivo vai ser fechado')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')

with open(caminho2, 'r') as arquivo:
    print(arquivo.read())

# os.remove(caminho2)
# os.rename(caminho2, 'aula117-2.txt')