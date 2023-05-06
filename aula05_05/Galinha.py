from Animal import Animal


class Galinha(Animal):
    def __init__(self, nome, peso):
        Animal.__init__(self,nome, peso)



    def botar(self):
        print("Botando ovo...")
