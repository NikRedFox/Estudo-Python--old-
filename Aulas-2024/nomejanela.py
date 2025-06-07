import pygetwindow as gw


def titulo():
    titulos = [janela.title for janela in gw.getAllTitles()]
    return titulos


titulos = titulo()
print('Titulos:')
for titulo in titulos:
    print(titulo())