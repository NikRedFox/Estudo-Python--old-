# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NAÕ TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
# (sem underline) = public
#       pode ser usado em qualquer lugar.
# _ (um underline) = protected
#       não deve ser usado fora da classe ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só deve ser usado na classe em que foi declarado.
class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return'_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
print(f.metodo_publico())
