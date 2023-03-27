L = [-8, -29, 100, 2, -2, 40, 23, -8, -7, 77]
L.sort()
def menorNumero(lista):
    menor = lista[0]

    for i in lista:
        if (i < menor):
            menor = i

    return menor


def maiorNumero(lista):
    maior = lista[0]
    for i in lista:
        if (i > maior):
            maior = i
    return maior


def media(lista):
    return sum(lista) / len(lista)

def listaInversa(lista):
    lista.reverse()
    print(lista)

listaInversa(L)
print(media(L))
print(menorNumero(L))
print(maiorNumero(L))
