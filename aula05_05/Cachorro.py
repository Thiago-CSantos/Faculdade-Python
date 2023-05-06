from builtins import print

from Animal import Animal


class Cachorro(Animal):

    def __init__(self, nome, peso):
        # super(nome, peso)
        Animal.__init__(self, nome, peso)

    def enterrarOsso(self):
        print("Enterrando osso ....")