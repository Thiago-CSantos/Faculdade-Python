lista = []
soma = 0
for i in range(4):
    nota = int(input(f"nota{i + 1}º"))
    lista.append(nota)
    soma = soma + nota

media = soma / len(lista)
print(media, lista)
