lista = []

for i in range(5):
    num = int(input(f"numero{i + 1}º"))

x= int(input("Digite um numero:"))

if (lista.count(x) == 0):
    print('Numero existente')
else:
    print('numero inexistente')
