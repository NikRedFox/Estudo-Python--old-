# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c2.filmar()

c1.fotografar()
c2.fotografar()

c1.parar_filmagem()
c2.parar_filmagem()

c1.fotografar()
c2.fotografar()