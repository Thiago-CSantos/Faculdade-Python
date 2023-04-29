class Aluno:
    __nome: str
    __ra: int
    __nota1: float
    __nota2: float
    __media: float

    def __init__(self,nome,ra, nota1, nota2):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome

    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2) /2
        return self.media

    def descricao(self):
        print("Aluno: ",self.__nome)
        print("RA: ", self.__ra)
        print("Media: ", self.__calcularMedia())

