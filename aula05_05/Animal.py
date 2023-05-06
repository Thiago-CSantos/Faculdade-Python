class Animal:

    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def dormir(self):
        return "...Dormindo"


