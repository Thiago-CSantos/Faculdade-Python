from Animal import *
from Cachorro import Cachorro
from Galinha import Galinha

obj1 = Cachorro("Totó", 50)

print("Cachorro", obj1.getNome())
obj1.enterrarOsso()

print(obj1.getNome(), obj1.dormir())

obj2 = Galinha("Dangola", 5)
print("Galinha" , obj2.getNome())
obj2.botar()
print(obj2.getNome(), obj2.dormir())


